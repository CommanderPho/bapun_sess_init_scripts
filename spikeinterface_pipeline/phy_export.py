from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd
import spikeinterface.full as si
from spikeinterface.core.template_tools import get_template_extremum_channel
from spikeinterface.exporters import export_to_phy

from spikeinterface_pipeline.analyzer import phy_job_kwargs
from spikeinterface_pipeline.paths import SessionPaths, SortingSessionPaths

PhyExportOverwriteMode = Literal["if_missing", "always"]


def export_curation_review_csv(comparison: pd.DataFrame, good_units: pd.Index, output_path: Path) -> Path:
    comparison_out = comparison.copy()
    comparison_out["good_unit"] = comparison_out.index.isin(good_units)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    comparison_out.to_csv(output_path)
    return output_path


def write_phy_cluster_info(paths: SessionPaths, all_labels: pd.DataFrame, good_units: pd.Index, *, strategy: str, require_cluster_info: bool = True, q_labels: pd.Series | None = None, preserve_human_labels: bool = True) -> Path | None:
    return write_cluster_info_at_path(paths.phy_gui_dir / "cluster_info.tsv", all_labels=all_labels, good_units=good_units, strategy=strategy, require_cluster_info=require_cluster_info, q_labels=q_labels, preserve_human_labels=preserve_human_labels, include_mua_in_phy=True)


def _cluster_id_value_map(unit_id_to_cluster_id: dict, value_by_unit_id: dict) -> dict:
    return {unit_id_to_cluster_id[uid]: value_by_unit_id[uid] for uid in unit_id_to_cluster_id if uid in value_by_unit_id}


def _phy_curated_export_exists(phy_folder: Path) -> bool:
    if not phy_folder.is_dir():
        return False
    if not (phy_folder / "params.py").is_file():
        return False
    return (phy_folder / "spike_clusters.npy").is_file() or (phy_folder / "cluster_si_unit_ids.tsv").is_file()


def bootstrap_cluster_info(phy_folder: Path, sorting_analyzer: object) -> pd.DataFrame:
    templates_ext = sorting_analyzer.get_extension("templates")
    if templates_ext is None:
        raise RuntimeError("SortingAnalyzer has no 'templates' extension; compute templates before bootstrapping cluster_info.tsv.")
    sorting = sorting_analyzer.sorting
    unit_ids = list(sorting.unit_ids)
    templates = templates_ext.get_data()
    if isinstance(templates, dict):
        templates = templates["average"] if "average" in templates else next(iter(templates.values()))
    extremum_channels = get_template_extremum_channel(sorting_analyzer, peak_sign="neg", outputs="id", operator="average")
    rows = []
    for cluster_id, unit_id in enumerate(unit_ids):
        unit_index = sorting.id_to_index(unit_id)
        unit_template = np.asarray(templates[unit_index])
        ch = int(extremum_channels[unit_id])
        amp = float(np.max(np.abs(unit_template)))
        sh = 0
        if sorting_analyzer.has_extension("unit_locations"):
            unit_locations = sorting_analyzer.get_extension("unit_locations").get_data()
            if hasattr(unit_locations, "columns") and "shank" in unit_locations.columns:
                sh = int(unit_locations.loc[unit_id, "shank"])
            elif getattr(unit_locations, "dtype", None) is not None and unit_locations.dtype.names and "shank" in unit_locations.dtype.names:
                sh = int(unit_locations[unit_index]["shank"])
        rows.append({"cluster_id": cluster_id, "group": "unsorted", "ch": ch, "sh": sh, "amp": amp, "si_unit_id": unit_id})
    cluster_info = pd.DataFrame(rows)
    cluster_info_path = phy_folder / "cluster_info.tsv"
    cluster_info.to_csv(cluster_info_path, sep="\t", index=False)
    return cluster_info


def _unit_id_to_phy_group(unit_id: object, all_labels: pd.DataFrame, good_units: pd.Index, *, include_mua_in_phy: bool) -> str:
    if unit_id in good_units:
        return "good"
    prediction = str(all_labels.loc[unit_id, "prediction"]).lower() if unit_id in all_labels.index else ""
    if include_mua_in_phy and prediction == "mua":
        return "mua"
    return "noise"


def _build_unit_id_to_cluster_id(cluster_info: pd.DataFrame, cluster_id_col: str, all_labels: pd.DataFrame) -> dict:
    if "si_unit_id" in cluster_info.columns:
        return {row.si_unit_id: int(getattr(row, cluster_id_col)) for row in cluster_info.itertuples()}
    return {uid: int(cid) for uid, cid in zip(all_labels.index, cluster_info[cluster_id_col].values)}


def write_cluster_info_at_path(cluster_info_path: Path, all_labels: pd.DataFrame, good_units: pd.Index, *, strategy: str, require_cluster_info: bool = True, q_labels: pd.Series | None = None, preserve_human_labels: bool = True, include_mua_in_phy: bool = True, unit_id_to_cluster_id: dict | None = None) -> Path | None:
    if not (cluster_info_path.exists() and cluster_info_path.is_file()):
        message = f"cluster_info.tsv does not exist: {cluster_info_path}"
        if require_cluster_info:
            raise FileNotFoundError(message)
        print(f"WARNING: {message}")
        return None
    if "prediction" not in all_labels.columns:
        raise ValueError("all_labels must contain a 'prediction' column for cluster_info export.")
    shutil.copy(cluster_info_path, cluster_info_path.with_suffix(".tsv.bak"))
    cluster_info = pd.read_csv(cluster_info_path, sep="\t")
    cluster_id_col = "cluster_id" if "cluster_id" in cluster_info.columns else "id"
    if unit_id_to_cluster_id is None:
        unit_id_to_cluster_id = _build_unit_id_to_cluster_id(cluster_info, cluster_id_col, all_labels)
    if not unit_id_to_cluster_id:
        raise ValueError("unit_id_to_cluster_id is empty; cannot annotate cluster_info.tsv.")
    cluster_ids = cluster_info[cluster_id_col]
    existing_group = cluster_info.get("group", pd.Series("", index=cluster_info.index)).fillna("").astype(str).str.strip().str.lower()
    existing_q = cluster_info.get("q", pd.Series("", index=cluster_info.index)).fillna("").astype(str).str.strip()
    manual_groups = {"good", "mua", "noise"}
    manual_label_mask = existing_group.isin(manual_groups) | existing_q.ne("")
    group_by_unit = {uid: _unit_id_to_phy_group(uid, all_labels, good_units, include_mua_in_phy=include_mua_in_phy) for uid in unit_id_to_cluster_id}
    mapped_group = cluster_ids.map(_cluster_id_value_map(unit_id_to_cluster_id, group_by_unit))
    if preserve_human_labels:
        cluster_info["group"] = cluster_info.get("group", pd.Series("", index=cluster_info.index)).where(manual_label_mask, mapped_group)
    else:
        cluster_info["group"] = mapped_group
    prediction_by_unit = {uid: all_labels.loc[uid, "prediction"] for uid in unit_id_to_cluster_id if uid in all_labels.index}
    cluster_info["model_prediction"] = cluster_ids.map(_cluster_id_value_map(unit_id_to_cluster_id, prediction_by_unit))
    if "probability" in all_labels.columns:
        probability_by_unit = {uid: all_labels.loc[uid, "probability"] for uid in unit_id_to_cluster_id if uid in all_labels.index}
        cluster_info["model_probability"] = cluster_ids.map(_cluster_id_value_map(unit_id_to_cluster_id, probability_by_unit))
    else:
        cluster_info["model_probability"] = np.nan
    cluster_info["curation_strategy"] = strategy
    good_unit_by_unit = {uid: uid in good_units for uid in unit_id_to_cluster_id}
    cluster_info["good_unit"] = cluster_ids.map(_cluster_id_value_map(unit_id_to_cluster_id, good_unit_by_unit))
    if q_labels is not None:
        q_by_unit = {uid: q_labels.get(uid, "") for uid in unit_id_to_cluster_id if uid in q_labels.index}
        mapped_q = cluster_ids.map(_cluster_id_value_map(unit_id_to_cluster_id, q_by_unit))
        if preserve_human_labels:
            cluster_info["q"] = existing_q.where(manual_label_mask, mapped_q)
        else:
            cluster_info["q"] = mapped_q
    tmp_path = cluster_info_path.with_suffix(".tsv.tmp")
    cluster_info.to_csv(tmp_path, sep="\t", index=False)
    tmp_path.replace(cluster_info_path)
    return cluster_info_path


def write_bapun_params_py(phy_folder: Path, dat_path: Path, *, n_channels: int, sampling_rate: float, dtype: str = "int16", n_features_per_channel: int = 5) -> Path:
    params_path = phy_folder / "params.py"
    with params_path.open("w") as f:
        f.write(f'dat_path = r"{dat_path.as_posix()}"\n')
        f.write(f"n_channels_dat = {n_channels}\n")
        f.write(f"n_features_per_channel = {n_features_per_channel}\n")
        f.write(f'dtype = r"{dtype}"\n')
        f.write("offset = 0\n")
        f.write(f"sample_rate = {float(sampling_rate)}\n")
        f.write(f'dir_path = r"{phy_folder.as_posix()}"\n')
        f.write("hp_filtered = True\n")
    return params_path


def export_good_units_tsv(good_units: pd.Index, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"unit_id": list(good_units)}).to_csv(output_path, sep="\t", index=False)
    return output_path


def export_good_units_json(good_units: pd.Index, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps([str(u) for u in good_units], indent=2))
    return output_path


def export_curated_phy_folder(sorting_analyzer: object, paths: SortingSessionPaths, all_labels: pd.DataFrame, good_units: pd.Index, q_labels: pd.Series, *, strategy: str, n_channels: int, sampling_rate: float, n_jobs: int = 8, include_mua_in_phy: bool = True, preserve_human_phy_labels: bool = True, verbose: bool = True, phy_export_overwrite: PhyExportOverwriteMode = "if_missing") -> Path:
    job_kwargs = phy_job_kwargs(n_jobs=n_jobs)
    phy_folder = paths.phy_curated_folder
    run_phy_export = phy_export_overwrite == "always" or not _phy_curated_export_exists(phy_folder)
    if run_phy_export:
        sparsity = si.compute_sparsity(sorting_analyzer) if sorting_analyzer.get_num_channels() > 64 else None
        export_to_phy(sorting_analyzer=sorting_analyzer, output_folder=phy_folder, copy_binary=False, remove_if_exists=True, sparsity=sparsity, verbose=verbose, **job_kwargs)
    else:
        print(f"Skipping export_to_phy; existing Phy export found at {phy_folder}")
    write_bapun_params_py(phy_folder, paths.concatenated_dat_file, n_channels=n_channels, sampling_rate=sampling_rate)
    cluster_info_path = phy_folder / "cluster_info.tsv"
    if not cluster_info_path.exists():
        bootstrap_cluster_info(phy_folder, sorting_analyzer)
    si_unit_ids_path = phy_folder / "cluster_si_unit_ids.tsv"
    unit_id_to_cluster_id = {}
    if si_unit_ids_path.exists():
        si_unit_df = pd.read_csv(si_unit_ids_path, sep="\t")
        unit_id_to_cluster_id = {row.si_unit_id: int(row.cluster_id) for row in si_unit_df.itertuples()}
    else:
        unit_id_to_cluster_id = {uid: i for i, uid in enumerate(sorting_analyzer.sorting.unit_ids)}
    write_cluster_info_at_path(cluster_info_path, all_labels=all_labels, good_units=good_units, strategy=strategy, require_cluster_info=True, q_labels=q_labels, preserve_human_labels=preserve_human_phy_labels, include_mua_in_phy=include_mua_in_phy, unit_id_to_cluster_id=unit_id_to_cluster_id)
    return phy_folder

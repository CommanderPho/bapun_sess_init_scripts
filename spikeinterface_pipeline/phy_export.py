from __future__ import annotations

import shutil
from pathlib import Path

import pandas as pd

from spikeinterface_pipeline.curation import PHY_LABEL_MAP
from spikeinterface_pipeline.paths import SessionPaths


def export_curation_review_csv(comparison: pd.DataFrame, good_units: pd.Index, output_path: Path) -> Path:
    comparison_out = comparison.copy()
    comparison_out["good_unit"] = comparison_out.index.isin(good_units)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    comparison_out.to_csv(output_path)
    return output_path


def write_phy_cluster_info(paths: SessionPaths, all_labels: pd.DataFrame, good_units: pd.Index, *, strategy: str, require_cluster_info: bool = True, q_labels: pd.Series | None = None) -> Path | None:
    cluster_info_path = paths.phy_gui_dir / "cluster_info.tsv"
    if not (cluster_info_path.exists() and cluster_info_path.is_file()):
        message = f"cluster_info.tsv does not exist: {cluster_info_path}. Launch Phy to create this file."
        if require_cluster_info:
            raise FileNotFoundError(message)
        print(f"WARNING: {message}")
        return None
    shutil.copy(cluster_info_path, cluster_info_path.with_suffix(".tsv.bak"))
    cluster_info = pd.read_csv(cluster_info_path, sep="\t")
    cluster_id_col = "cluster_id" if "cluster_id" in cluster_info.columns else "id"
    phy_groups = all_labels["prediction"].map(PHY_LABEL_MAP).fillna("")
    cluster_ids = cluster_info[cluster_id_col]
    cluster_info["group"] = cluster_ids.map(phy_groups).fillna(cluster_info["group"])
    cluster_info["model_prediction"] = cluster_ids.map(all_labels["prediction"])
    cluster_info["model_probability"] = cluster_ids.map(all_labels["probability"])
    cluster_info["curation_strategy"] = strategy
    cluster_info["good_unit"] = cluster_ids.isin(good_units)
    if q_labels is not None:
        cluster_info["q"] = cluster_ids.map(q_labels).fillna("")
    cluster_info.to_csv(cluster_info_path, sep="\t", index=False)
    return cluster_info_path

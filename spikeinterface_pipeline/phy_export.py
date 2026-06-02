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


def write_phy_cluster_info(paths: SessionPaths, all_labels: pd.DataFrame, good_units: pd.Index, *, strategy: str, require_cluster_info: bool = True) -> Path | None:
    cluster_info_path = paths.phy_gui_dir / "cluster_info.tsv"
    if not (cluster_info_path.exists() and cluster_info_path.is_file()):
        message = f"cluster_info.tsv does not exist: {cluster_info_path}. Launch Phy to create this file."
        if require_cluster_info:
            raise FileNotFoundError(message)
        print(f"WARNING: {message}")
        return None
    shutil.copy(cluster_info_path, cluster_info_path.with_suffix(".tsv.bak"))
    cluster_info = pd.read_csv(cluster_info_path, sep="\t")
    phy_groups = all_labels["prediction"].map(PHY_LABEL_MAP).fillna("")
    cluster_info["group"] = cluster_info["cluster_id"].map(phy_groups).fillna(cluster_info["group"])
    cluster_info["model_prediction"] = cluster_info["cluster_id"].map(all_labels["prediction"])
    cluster_info["model_probability"] = cluster_info["cluster_id"].map(all_labels["probability"])
    cluster_info["curation_strategy"] = strategy
    cluster_info["good_unit"] = cluster_info["cluster_id"].isin(good_units)
    cluster_info.to_csv(cluster_info_path, sep="\t", index=False)
    return cluster_info_path

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from spikeinterface_pipeline.phy_export import _cluster_id_value_map, _phy_curated_export_exists, write_cluster_info_at_path


def test_cluster_id_value_map():
    unit_to_cluster = {"u1": 0, "u2": 1}
    values = {"u1": True, "u2": False}
    assert _cluster_id_value_map(unit_to_cluster, values) == {0: True, 1: False}


def test_phy_curated_export_exists(tmp_path: Path):
    assert not _phy_curated_export_exists(tmp_path)
    (tmp_path / "params.py").write_text("x")
    assert not _phy_curated_export_exists(tmp_path)
    (tmp_path / "spike_clusters.npy").write_bytes(b"")
    assert _phy_curated_export_exists(tmp_path)


def test_write_cluster_info_good_unit(tmp_path: Path):
    cluster_info_path = tmp_path / "cluster_info.tsv"
    cluster_info_path.write_text("cluster_id\tgroup\tsi_unit_id\n0\tunsorted\tu1\n1\tunsorted\tu2\n", encoding="utf-8")
    all_labels = pd.DataFrame({"prediction": ["sua", "noise"], "probability": [0.9, 0.3]}, index=["u1", "u2"])
    good_units = pd.Index(["u1"])
    unit_id_to_cluster_id = {"u1": 0, "u2": 1}
    write_cluster_info_at_path(cluster_info_path, all_labels=all_labels, good_units=good_units, strategy="sua_relaxed_prob", unit_id_to_cluster_id=unit_id_to_cluster_id, preserve_human_labels=False)
    result = pd.read_csv(cluster_info_path, sep="\t")
    assert list(result["good_unit"]) == [True, False]
    assert list(result["group"]) == ["good", "noise"]


def test_write_cluster_info_requires_prediction(tmp_path: Path):
    cluster_info_path = tmp_path / "cluster_info.tsv"
    cluster_info_path.write_text("cluster_id\tgroup\n0\tunsorted\n", encoding="utf-8")
    all_labels = pd.DataFrame({"score": [1.0]}, index=["u1"])
    with pytest.raises(ValueError, match="prediction"):
        write_cluster_info_at_path(cluster_info_path, all_labels=all_labels, good_units=pd.Index([]), strategy="sua", unit_id_to_cluster_id={"u1": 0})

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from spikeinterface_pipeline.config import NeuronLoadConfig
from spikeinterface_pipeline.neuron_loading import detect_neuron_source_type, inspect_phy_folder, load_neurons_from_sorting_phy, load_neurons_from_spyk_circ_phy, resolve_neuron_load_paths


def _write_legacy_phy_folder(phy_folder: Path) -> None:
    phy_folder.mkdir(parents=True, exist_ok=True)
    (phy_folder / "params.py").write_text('sample_rate = 30000\nn_channels_dat = 4\nn_features_per_channel = 5\n', encoding="utf-8")
    cluster_info = pd.DataFrame({"id": [0, 1, 2], "group": ["good", "mua", "noise"], "ch": [1, 2, 3], "sh": [0, 0, 0], "amp": [1.0, 2.0, 3.0]})
    cluster_info.to_csv(phy_folder / "cluster_info.tsv", sep="\t", index=False)
    spike_times = np.array([[100], [200], [300], [400]], dtype=np.uint64)
    spike_clusters = np.array([0, 0, 1, 2], dtype=np.int32)
    spike_templates = np.array([0, 0, 1, 2], dtype=np.int32)
    templates = np.ones((3, 4, 10), dtype=np.float32)
    np.save(phy_folder / "spike_times.npy", spike_times)
    np.save(phy_folder / "spike_clusters.npy", spike_clusters)
    np.save(phy_folder / "spike_templates.npy", spike_templates)
    np.save(phy_folder / "templates.npy", templates)
    np.save(phy_folder / "similar_templates.npy", np.eye(3, dtype=np.float32))


def _write_si_phy_folder(phy_folder: Path) -> None:
    _write_legacy_phy_folder(phy_folder)
    cluster_info = pd.read_csv(phy_folder / "cluster_info.tsv", sep="\t")
    cluster_info["cluster_id"] = cluster_info["id"]
    cluster_info["si_unit_id"] = [10, 20, 30]
    cluster_info.to_csv(phy_folder / "cluster_info.tsv", sep="\t", index=False)
    pd.DataFrame({"cluster_id": [0, 1, 2], "si_unit_id": [10, 20, 30]}).to_csv(phy_folder / "cluster_si_unit_ids.tsv", sep="\t", index=False)


def _write_minimal_sorting_phy_folder(phy_folder: Path, review_path: Path) -> None:
    _write_si_phy_folder(phy_folder)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(",prediction,probability,qm_good\n10,sua,0.9,good\n20,noise,0.1,noise\n30,sua,0.8,good\n", encoding="utf-8")


def test_inspect_phy_folder_legacy_contents(tmp_path: Path):
    phy_folder = tmp_path / "arbitrary_legacy_name"
    _write_legacy_phy_folder(phy_folder)
    assert inspect_phy_folder(phy_folder) == "spyk_circ_phy_export"


def test_inspect_phy_folder_si_contents(tmp_path: Path):
    phy_folder = tmp_path / "arbitrary_si_name"
    _write_si_phy_folder(phy_folder)
    assert inspect_phy_folder(phy_folder) == "si_phy_export"


def test_inspect_phy_folder_invalid(tmp_path: Path):
    phy_folder = tmp_path / "empty_folder"
    phy_folder.mkdir()
    assert inspect_phy_folder(phy_folder) == "invalid"


def test_detect_source_type_phyio_without_csv(tmp_path: Path):
    phy_folder = tmp_path / "any_folder"
    _write_legacy_phy_folder(phy_folder)
    assert detect_neuron_source_type(phy_folder) == "spyk_circ"


def test_detect_source_type_with_explicit_review_csv(tmp_path: Path):
    phy_folder = tmp_path / "any_folder"
    review_path = tmp_path / "review.csv"
    _write_legacy_phy_folder(phy_folder)
    review_path.write_text(",prediction\n1,sua\n", encoding="utf-8")
    assert detect_neuron_source_type(phy_folder, review_path) == "sorting"


def test_resolve_paths_from_run_name(tmp_path: Path):
    basedir = tmp_path / "Day4Openfield"
    sorting_root = basedir / "SORTING"
    phy_curated = sorting_root / "folder_KS4_v1_phy_curated"
    review_csv = sorting_root / "folder_KS4_v1_curation_review.csv"
    xml_path = basedir / "RatS-Day4Openfield.xml"
    _write_si_phy_folder(phy_curated)
    review_csv.write_text(",prediction\n68,sua\n", encoding="utf-8")
    xml_path.write_text("<xml/>", encoding="utf-8")
    config = NeuronLoadConfig(run_name="folder_KS4_v1")
    phy_folder, curation_review_path, source_type = resolve_neuron_load_paths(config, basedir=basedir, basename="RatS-Day4Openfield")
    assert phy_folder == phy_curated.resolve()
    assert curation_review_path == review_csv.resolve()
    assert source_type == "sorting"


def test_resolve_paths_direct_phy_folder_uses_phyio(tmp_path: Path):
    phy_folder = tmp_path / "custom_phy_export"
    _write_si_phy_folder(phy_folder)
    config = NeuronLoadConfig(phy_folder=phy_folder)
    resolved_phy, curation_review_path, source_type = resolve_neuron_load_paths(config, basedir=tmp_path, basename="ignored")
    assert resolved_phy == phy_folder.resolve()
    assert curation_review_path is None
    assert source_type == "spyk_circ"


def test_resolve_paths_explicit_review_triggers_csv_loader(tmp_path: Path):
    phy_folder = tmp_path / "custom_phy_export"
    review_path = tmp_path / "review.csv"
    _write_minimal_sorting_phy_folder(phy_folder, review_path)
    config = NeuronLoadConfig(phy_folder=phy_folder, curation_review_path=review_path)
    resolved_phy, resolved_review, source_type = resolve_neuron_load_paths(config, basedir=tmp_path, basename="ignored")
    assert resolved_phy == phy_folder.resolve()
    assert resolved_review == review_path.resolve()
    assert source_type == "sorting"


def test_sorting_unit_filter_query(tmp_path: Path):
    phy_folder = tmp_path / "custom_phy_export"
    review_path = tmp_path / "review.csv"
    _write_minimal_sorting_phy_folder(phy_folder, review_path)
    neurons = load_neurons_from_sorting_phy(phy_folder, review_path, t_stop=10.0, unit_filter='prediction == "sua"')
    assert neurons.n_neurons == 2
    assert list(neurons.neuron_ids) == [10, 30]
    assert neurons._extended_neuron_properties_df.shape[0] == 2


def test_si_phy_folder_loads_via_phyio_without_csv(tmp_path: Path):
    phy_folder = tmp_path / "custom_si_export"
    _write_si_phy_folder(phy_folder)
    neurons = load_neurons_from_spyk_circ_phy(phy_folder, t_stop=10.0, include_groups=("good", "mua"))
    assert neurons.n_neurons == 2
    assert list(neurons.neuron_ids) == [10, 20]


def test_legacy_delegates_to_phyio_groups(tmp_path: Path):
    phy_folder = tmp_path / "custom_legacy_export"
    _write_legacy_phy_folder(phy_folder)
    neurons = load_neurons_from_spyk_circ_phy(phy_folder, t_stop=10.0, include_groups=("good", "mua"))
    assert neurons.n_neurons == 2


def test_sorting_unit_filter_empty_raises(tmp_path: Path):
    phy_folder = tmp_path / "custom_phy_export"
    review_path = tmp_path / "review.csv"
    _write_minimal_sorting_phy_folder(phy_folder, review_path)
    with pytest.raises(ValueError, match="matched no units"):
        load_neurons_from_sorting_phy(phy_folder, review_path, t_stop=10.0, unit_filter='prediction == "nonexistent"')

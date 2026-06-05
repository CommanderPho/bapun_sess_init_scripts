from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from spikeinterface_pipeline.config import BapunSessionConfig, NeuronLoadConfig
from spikeinterface_pipeline.neuron_loading import detect_neuron_source_type, load_neurons_from_sorting_phy, load_neurons_from_spyk_circ_phy, resolve_neuron_load_paths


def test_detect_source_type_merged_gui():
    phy_folder = Path("/data/spyk-circ/RatS-Day1/RatS-Day1-merged.GUI")
    assert detect_neuron_source_type(phy_folder) == "spyk_circ"


def test_detect_source_type_phy_curated():
    phy_folder = Path("/data/SORTING/folder_KS4_v1_phy_curated")
    assert detect_neuron_source_type(phy_folder) == "sorting"


def test_detect_source_type_with_review_csv(tmp_path: Path):
    phy_folder = tmp_path / "any_phy_folder"
    review_path = tmp_path / "review.csv"
    review_path.write_text("si_unit_id,prediction\n1,sua\n", encoding="utf-8")
    assert detect_neuron_source_type(phy_folder, review_path) == "sorting"


def test_resolve_paths_from_run_name(tmp_path: Path):
    basedir = tmp_path / "Day4Openfield"
    sorting_root = basedir / "SORTING"
    phy_curated = sorting_root / "folder_KS4_v1_phy_curated"
    review_csv = sorting_root / "folder_KS4_v1_curation_review.csv"
    xml_path = basedir / "RatS-Day4Openfield.xml"
    phy_curated.mkdir(parents=True)
    review_csv.write_text(",prediction\n68,sua\n", encoding="utf-8")
    xml_path.write_text("<xml/>", encoding="utf-8")
    config = NeuronLoadConfig(run_name="folder_KS4_v1")
    phy_folder, curation_review_path, source_type = resolve_neuron_load_paths(config, basedir=basedir, basename="RatS-Day4Openfield")
    assert phy_folder == phy_curated.resolve()
    assert curation_review_path == review_csv.resolve()
    assert source_type == "sorting"


def _write_minimal_sorting_phy_folder(phy_folder: Path, review_path: Path) -> None:
    phy_folder.mkdir(parents=True, exist_ok=True)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(",prediction,probability,qm_good\n10,sua,0.9,good\n20,noise,0.1,noise\n30,sua,0.8,good\n", encoding="utf-8")
    (phy_folder / "params.py").write_text('sample_rate = 30000\nn_channels_dat = 4\nn_features_per_channel = 5\n', encoding="utf-8")
    cluster_info = pd.DataFrame({"cluster_id": [0, 1, 2], "group": ["good", "noise", "good"], "ch": [1, 2, 3], "sh": [0, 0, 0], "amp": [1.0, 2.0, 3.0], "si_unit_id": [10, 20, 30]})
    cluster_info.to_csv(phy_folder / "cluster_info.tsv", sep="\t", index=False)
    pd.DataFrame({"cluster_id": [0, 1, 2], "si_unit_id": [10, 20, 30]}).to_csv(phy_folder / "cluster_si_unit_ids.tsv", sep="\t", index=False)
    spike_times = np.array([[100], [200], [300], [400], [500]], dtype=np.uint64)
    spike_clusters = np.array([0, 0, 1, 2, 2], dtype=np.int32)
    spike_templates = np.array([0, 0, 1, 2, 2], dtype=np.int32)
    templates = np.ones((3, 4, 10), dtype=np.float32)
    np.save(phy_folder / "spike_times.npy", spike_times)
    np.save(phy_folder / "spike_clusters.npy", spike_clusters)
    np.save(phy_folder / "spike_templates.npy", spike_templates)
    np.save(phy_folder / "templates.npy", templates)
    np.save(phy_folder / "similar_templates.npy", np.eye(3, dtype=np.float32))


def test_sorting_unit_filter_query(tmp_path: Path):
    phy_folder = tmp_path / "folder_KS4_v1_phy_curated"
    review_path = tmp_path / "folder_KS4_v1_curation_review.csv"
    _write_minimal_sorting_phy_folder(phy_folder, review_path)
    neurons = load_neurons_from_sorting_phy(phy_folder, review_path, t_stop=10.0, unit_filter='prediction == "sua"')
    assert neurons.n_neurons == 2
    assert list(neurons.neuron_ids) == [10, 30]
    assert neurons._extended_neuron_properties_df.shape[0] == 2


def test_legacy_delegates_to_phyio_groups(tmp_path: Path):
    phy_folder = tmp_path / "RatS-Day1-merged.GUI"
    phy_folder.mkdir(parents=True)
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
    neurons = load_neurons_from_spyk_circ_phy(phy_folder, t_stop=10.0, include_groups=("good", "mua"))
    assert neurons.n_neurons == 2


def test_sorting_unit_filter_empty_raises(tmp_path: Path):
    phy_folder = tmp_path / "folder_KS4_v1_phy_curated"
    review_path = tmp_path / "folder_KS4_v1_curation_review.csv"
    _write_minimal_sorting_phy_folder(phy_folder, review_path)
    with pytest.raises(ValueError, match="matched no units"):
        load_neurons_from_sorting_phy(phy_folder, review_path, t_stop=10.0, unit_filter='prediction == "nonexistent"')

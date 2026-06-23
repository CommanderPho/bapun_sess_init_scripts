from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

from neuropy.core.session.init_from_raw_data import NeuronLoadConfig, RawDataInitializationMixin


def _write_sorter_folder(sorter_folder: Path) -> None:
    sorter_folder.mkdir(parents=True, exist_ok=True)
    log = {"error": False, "sorter_name": "kilosort4"}
    (sorter_folder / "spikeinterface_log.json").write_text(json.dumps(log), encoding="utf-8")


def _write_review_csv(review_path: Path) -> None:
    review_path.write_text(',prediction,probability\n10,sua,0.9\n20,noise,0.1\n30,sua,0.8\n', encoding="utf-8")


def _mock_sorting(unit_ids: list[int], sampling_rate: float = 30000.0) -> MagicMock:
    sorting = MagicMock()
    sorting.unit_ids = unit_ids
    sorting.get_sampling_frequency.return_value = sampling_rate
    sorting.get_num_units.return_value = len(unit_ids)
    spike_trains = {unit_id: np.array([100 * (unit_id + 1), 200 * (unit_id + 1)], dtype=np.int64) for unit_id in unit_ids}
    sorting.get_unit_spike_train.side_effect = lambda unit_id, segment_index=0, return_times=False: spike_trains[unit_id]
    return sorting


def test_resolve_sorter_paths_from_run_name(tmp_path: Path):
    basedir = tmp_path / "Day3TwoNovel"
    sorting_root = basedir / "SORTING"
    sorter_folder = sorting_root / "folder_KS4_v1"
    analyzer_folder = sorting_root / "folder_KS4_v1_sorting_analyzer"
    review_csv = sorting_root / "folder_KS4_v1_curation_review.csv"
    _write_sorter_folder(sorter_folder)
    analyzer_folder.mkdir(parents=True)
    _write_review_csv(review_csv)
    config = NeuronLoadConfig(run_name="folder_KS4_v1")
    resolved_sorter, resolved_analyzer, resolved_review = RawDataInitializationMixin._resolve_sorter_neuron_load_paths(config, basedir=basedir)
    assert resolved_sorter == sorter_folder.resolve()
    assert resolved_analyzer == analyzer_folder.resolve()
    assert resolved_review == review_csv.resolve()


def test_resolve_sorter_paths_explicit_folder(tmp_path: Path):
    sorter_folder = tmp_path / "custom_sorter"
    _write_sorter_folder(sorter_folder)
    config = NeuronLoadConfig(sorter_folder=sorter_folder)
    resolved_sorter, resolved_analyzer, resolved_review = RawDataInitializationMixin._resolve_sorter_neuron_load_paths(config, basedir=tmp_path)
    assert resolved_sorter == sorter_folder.resolve()
    assert resolved_analyzer is None
    assert resolved_review is None


def test_resolve_sorter_paths_invalid_folder_raises(tmp_path: Path):
    sorter_folder = tmp_path / "empty_sorter"
    sorter_folder.mkdir()
    config = NeuronLoadConfig(sorter_folder=sorter_folder)
    with pytest.raises(FileNotFoundError, match="not a valid SpikeInterface sorter output"):
        RawDataInitializationMixin._resolve_sorter_neuron_load_paths(config, basedir=tmp_path)


@patch("spikeinterface.full.read_sorter_folder")
def test_sorter_unit_filter_query(read_sorter_folder: MagicMock, tmp_path: Path):
    sorter_folder = tmp_path / "folder_KS4_v1"
    review_path = tmp_path / "review.csv"
    _write_sorter_folder(sorter_folder)
    _write_review_csv(review_path)
    read_sorter_folder.return_value = _mock_sorting([10, 20, 30])
    neurons = RawDataInitializationMixin._load_neurons_from_spikeinterface_sorter(sorter_folder, sorting_analyzer_folder=None, curation_review_path=review_path, t_stop=10.0, unit_filter='prediction == "sua"')
    assert neurons.n_neurons == 2
    assert list(neurons.neuron_ids) == [10, 30]
    assert neurons._extended_neuron_properties_df.shape[0] == 2


@patch("spikeinterface.full.read_sorter_folder")
def test_sorter_loads_all_units_without_review_csv(read_sorter_folder: MagicMock, tmp_path: Path, capsys):
    sorter_folder = tmp_path / "folder_KS4_v1"
    _write_sorter_folder(sorter_folder)
    read_sorter_folder.return_value = _mock_sorting([0, 1, 2])
    neurons = RawDataInitializationMixin._load_neurons_from_spikeinterface_sorter(sorter_folder, sorting_analyzer_folder=None, curation_review_path=None, t_stop=10.0, unit_filter='prediction == "sua"')
    assert neurons.n_neurons == 3
    assert "loading all 3 units" in capsys.readouterr().out


@patch("spikeinterface.full.read_sorter_folder")
def test_sorter_unit_filter_empty_raises(read_sorter_folder: MagicMock, tmp_path: Path):
    sorter_folder = tmp_path / "folder_KS4_v1"
    review_path = tmp_path / "review.csv"
    _write_sorter_folder(sorter_folder)
    review_path.write_text(',prediction\n10,noise\n', encoding="utf-8")
    read_sorter_folder.return_value = _mock_sorting([10])
    with pytest.raises(ValueError, match="matched no units"):
        RawDataInitializationMixin._load_neurons_from_spikeinterface_sorter(sorter_folder, sorting_analyzer_folder=None, curation_review_path=review_path, t_stop=10.0, unit_filter='prediction == "sua"')


def test_build_neurons_from_spikinginterface_sorter_invalid_folder_returns_none(tmp_path: Path, capsys):
    class DummySess:
        name = "TestSession"
        filePrefix = tmp_path / "TestSession"
        eegfile = MagicMock(duration=100.0)
        neurons = None

    result = RawDataInitializationMixin.build_neurons_from_spikinginterface_sorter(DummySess(), tmp_path, sorter_folder=tmp_path / "missing_sorter")
    assert result is None
    assert "not a valid SpikeInterface sorter output" in capsys.readouterr().out


def _write_kilosort4_sorter_tree(basedir: Path, run_name: str = "folder_KS4_v1") -> tuple[Path, Path]:
    sorter_folder = basedir / "SORTING" / run_name
    sorter_output = sorter_folder / "sorter_output"
    sorter_output.mkdir(parents=True, exist_ok=True)
    (sorter_folder / "spikeinterface_log.json").write_text(json.dumps({"error": False, "sorter_name": "kilosort4"}), encoding="utf-8")
    (sorter_output / "params.py").write_text("n_channels = 4\n", encoding="utf-8")
    return sorter_folder, sorter_output


def test_resolve_kilosort4_paths_from_run_name(tmp_path: Path):
    basedir = tmp_path / "Day3TwoNovel"
    sorter_folder, sorter_output = _write_kilosort4_sorter_tree(basedir)
    config = NeuronLoadConfig(run_name="folder_KS4_v1")
    resolved = RawDataInitializationMixin._resolve_kilosort4_sorter_output_path(config, basedir=basedir)
    assert resolved == sorter_output.resolve()


def test_resolve_kilosort4_paths_from_sorter_folder(tmp_path: Path):
    basedir = tmp_path / "Day3TwoNovel"
    sorter_folder, sorter_output = _write_kilosort4_sorter_tree(basedir)
    config = NeuronLoadConfig(sorter_folder=sorter_folder)
    resolved = RawDataInitializationMixin._resolve_kilosort4_sorter_output_path(config, basedir=basedir)
    assert resolved == sorter_output.resolve()


def test_resolve_kilosort4_wrong_sorter_raises(tmp_path: Path):
    sorter_folder = tmp_path / "SORTING" / "folder_SC2"
    sorter_output = sorter_folder / "sorter_output"
    sorter_output.mkdir(parents=True)
    (sorter_folder / "spikeinterface_log.json").write_text(json.dumps({"error": False, "sorter_name": "spykingcircus2"}), encoding="utf-8")
    (sorter_output / "params.py").write_text("n_channels = 4\n", encoding="utf-8")
    config = NeuronLoadConfig(run_name="folder_SC2")
    with pytest.raises(ValueError, match="expected kilosort4"):
        RawDataInitializationMixin._resolve_kilosort4_sorter_output_path(config, basedir=tmp_path)


@patch("spikeinterface.extractors.read_kilosort")
def test_kilosort4_good_only_load(read_kilosort: MagicMock, tmp_path: Path):
    _, sorter_output = _write_kilosort4_sorter_tree(tmp_path)
    read_kilosort.return_value = _mock_sorting(list(range(34)))
    neurons = RawDataInitializationMixin._load_neurons_from_spikinginterface_kilosort4(sorter_output, t_stop=10.0)
    read_kilosort.assert_called_once_with(sorter_output, keep_good_only=True)
    assert neurons.n_neurons == 34
    assert list(neurons.neuron_ids) == list(range(34))


@patch("spikeinterface.extractors.read_kilosort")
def test_kilosort4_no_good_units_raises(read_kilosort: MagicMock, tmp_path: Path):
    _, sorter_output = _write_kilosort4_sorter_tree(tmp_path)
    read_kilosort.return_value = _mock_sorting([])
    with pytest.raises(ValueError, match="no Kilosort good units"):
        RawDataInitializationMixin._load_neurons_from_spikinginterface_kilosort4(sorter_output, t_stop=10.0)


def test_build_neurons_from_spikinginterface_kilosort4_invalid_folder_returns_none(tmp_path: Path, capsys):
    class DummySess:
        name = "TestSession"
        filePrefix = tmp_path / "TestSession"
        eegfile = MagicMock(duration=100.0)
        neurons = None

    result = RawDataInitializationMixin.build_neurons_from_spikinginterface_kilosort4(DummySess(), tmp_path, sorter_folder=tmp_path / "missing_sorter")
    assert result is None
    assert "kilosort4" in capsys.readouterr().out

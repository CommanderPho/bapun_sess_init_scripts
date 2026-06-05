from __future__ import annotations

from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd

from spikeinterface_pipeline.config import BapunSessionConfig, NeuronLoadConfig, NeuronSourceType
from spikeinterface_pipeline.paths import resolve_session_paths, resolve_sorting_paths

NeuronSourceTypeResolved = Literal["spyk_circ", "sorting"]
PhyFolderKind = Literal["invalid", "si_phy_export", "spyk_circ_phy_export"]
_PHY_REQUIRED_FILES = ("params.py", "spike_times.npy", "spike_clusters.npy", "cluster_info.tsv")


def inspect_phy_folder(phy_folder: Path) -> PhyFolderKind:
    if not phy_folder.is_dir():
        return "invalid"
    for filename in _PHY_REQUIRED_FILES:
        if not (phy_folder / filename).is_file():
            return "invalid"
    if (phy_folder / "cluster_si_unit_ids.tsv").is_file():
        return "si_phy_export"
    return "spyk_circ_phy_export"


def detect_neuron_source_type(phy_folder: Path, curation_review_path: Path | None = None) -> NeuronSourceTypeResolved:
    if curation_review_path is not None and curation_review_path.is_file():
        return "sorting"
    if inspect_phy_folder(phy_folder) == "invalid":
        raise FileNotFoundError(f"phy_folder is not a valid Phy export: {phy_folder}")
    return "spyk_circ"


def resolve_neuron_load_paths(config: NeuronLoadConfig, basedir: Path, basename: str) -> tuple[Path, Path | None, NeuronSourceTypeResolved]:
    session_config = BapunSessionConfig(basedir=basedir, basename=basename)
    if config.run_name is not None:
        sorting_paths = resolve_sorting_paths(session_config, config.run_name)
        phy_folder = config.phy_folder.resolve() if config.phy_folder is not None else sorting_paths.phy_curated_folder
        curation_review_path = config.curation_review_path.resolve() if config.curation_review_path is not None else sorting_paths.curation_review_path
        if not curation_review_path.is_file():
            raise FileNotFoundError(f"sorting neuron source requires curation_review_path; phy_folder={phy_folder}")
        return phy_folder, curation_review_path, "sorting"
    phy_folder = config.phy_folder
    curation_review_path = config.curation_review_path
    if phy_folder is None:
        session_paths = resolve_session_paths(session_config)
        phy_folder = session_paths.phy_gui_dir
    else:
        phy_folder = phy_folder.resolve()
    if curation_review_path is not None:
        curation_review_path = curation_review_path.resolve()
    if config.source_type == "sorting":
        if curation_review_path is None or not curation_review_path.is_file():
            raise FileNotFoundError(f"sorting neuron source requires curation_review_path; phy_folder={phy_folder}")
        return phy_folder, curation_review_path, "sorting"
    if config.source_type == "spyk_circ":
        if inspect_phy_folder(phy_folder) == "invalid":
            raise FileNotFoundError(f"phy_folder is not a valid Phy export: {phy_folder}")
        return phy_folder, None, "spyk_circ"
    source_type = detect_neuron_source_type(phy_folder, curation_review_path)
    return phy_folder, curation_review_path if source_type == "sorting" else None, source_type


def _read_phy_params(phy_folder: Path) -> dict[str, str]:
    params: dict[str, str] = {}
    with (phy_folder / "params.py").open("r") as f:
        for line in f:
            line_values = line.replace("\n", "").replace('r"', '"').replace('"', "").split("=")
            params[line_values[0].strip()] = line_values[1].strip()
    return params


def load_neurons_from_spyk_circ_phy(phy_folder: Path, *, t_stop: float, include_groups: tuple[str, ...] = ("good", "mua")) -> object:
    from neuropy.core import Neurons
    from neuropy.io import PhyIO

    if inspect_phy_folder(phy_folder) == "invalid":
        raise FileNotFoundError(f"phy_folder is not a valid Phy export: {phy_folder}")
    phy_data = PhyIO(phy_folder, include_groups=include_groups)
    if phy_data.spiketrains is None or len(phy_data.spiketrains) == 0:
        raise ValueError(f"no spiketrains found in Phy output at {phy_folder}")
    neuron_ids = phy_data.cluster_info["si_unit_id"].astype(int).values if "si_unit_id" in phy_data.cluster_info.columns else None
    return Neurons(
        np.array(phy_data.spiketrains, dtype=object),
        t_stop=t_stop,
        sampling_rate=phy_data.sampling_rate,
        peak_channels=phy_data.peak_channels,
        waveforms=np.array(phy_data.peak_waveforms, dtype="object"),
        shank_ids=np.array([int(v) for v in phy_data.shank_ids]),
        neuron_ids=neuron_ids,
    )


def load_neurons_from_sorting_phy(phy_folder: Path, curation_review_path: Path, *, t_stop: float, unit_filter: str) -> object:
    from neuropy.core import Neurons

    if inspect_phy_folder(phy_folder) == "invalid":
        raise FileNotFoundError(f"phy_folder is not a valid Phy export: {phy_folder}")
    if not curation_review_path.is_file():
        raise FileNotFoundError(f"curation_review_path does not exist: {curation_review_path}")
    review = pd.read_csv(curation_review_path, index_col=0)
    review.index.name = "si_unit_id"
    selected_review = review.query(unit_filter)
    if selected_review.empty:
        raise ValueError(f"unit_filter={unit_filter!r} matched no units in {curation_review_path}")
    selected_si_unit_ids = selected_review.index.astype(int)
    params = _read_phy_params(phy_folder)
    sampling_rate = int(float(params["sample_rate"]))
    spktime = np.load(phy_folder / "spike_times.npy")
    clu_ids = np.load(phy_folder / "spike_clusters.npy")
    spk_templates_id = np.load(phy_folder / "spike_templates.npy")
    spk_templates = np.load(phy_folder / "templates.npy")
    cluster_info = pd.read_csv(phy_folder / "cluster_info.tsv", sep="\t")
    cluster_si = pd.read_csv(phy_folder / "cluster_si_unit_ids.tsv", sep="\t")
    selected_clusters = cluster_si[cluster_si["si_unit_id"].isin(selected_si_unit_ids)]
    missing_ids = set(selected_si_unit_ids) - set(selected_clusters["si_unit_id"].astype(int))
    if missing_ids:
        raise ValueError(f"Missing cluster mappings for si_unit_ids: {sorted(missing_ids)}")
    spiketrains, peak_waveforms, peak_channels, shank_ids, neuron_ids = [], [], [], [], []
    for row in selected_clusters.itertuples():
        clu_id, si_unit_id = int(row.cluster_id), int(row.si_unit_id)
        info_rows = cluster_info[cluster_info["si_unit_id"] == si_unit_id]
        if info_rows.empty:
            raise ValueError(f"cluster_info missing si_unit_id={si_unit_id}")
        info = info_rows.iloc[0]
        spike_locs = np.where(clu_ids == clu_id)[0]
        cell_template_id, counts = np.unique(spk_templates_id[spike_locs], return_counts=True)
        template = spk_templates[cell_template_id[np.argmax(counts)]].squeeze().T
        spiketrains.append(spktime[spike_locs] / sampling_rate)
        peak_waveforms.append(template[np.argmax(np.max(template, axis=1))])
        peak_channels.append(int(info["ch"]))
        shank_ids.append(int(info["sh"]))
        neuron_ids.append(si_unit_id)
    neurons = Neurons(
        np.array(spiketrains, dtype=object),
        t_stop=t_stop,
        sampling_rate=sampling_rate,
        peak_channels=np.array(peak_channels),
        waveforms=np.array(peak_waveforms, dtype=object),
        shank_ids=np.array(shank_ids),
        neuron_ids=np.array(neuron_ids),
        extended_neuron_properties_df=selected_review.copy(),
    )
    return neurons


def build_neurons_for_session(sess: object, basedir: Path, config: NeuronLoadConfig | None = None) -> object | None:
    config = config or NeuronLoadConfig()
    basename = getattr(sess, "name", None) or getattr(getattr(sess, "config", None), "session_name", None)
    if basename is None and config.phy_folder is None and config.run_name is None:
        raise ValueError("sess must have .name or .config.session_name when phy_folder and run_name are not set")
    if basename is None:
        basename = "session"
    if sess.eegfile is None:
        print("WARNING: build_neurons_for_session: sess.eegfile is None; cannot determine t_stop for Neurons")
        return None
    t_stop = sess.eegfile.duration
    try:
        phy_folder, curation_review_path, source_type = resolve_neuron_load_paths(config, basedir=Path(basedir), basename=basename)
    except FileNotFoundError as exc:
        print(f"WARNING: build_neurons_for_session: {exc}")
        return None
    try:
        if source_type == "sorting":
            if curation_review_path is None:
                raise FileNotFoundError(f"sorting source requires curation_review_path; phy_folder={phy_folder}")
            neurons = load_neurons_from_sorting_phy(phy_folder, curation_review_path, t_stop=t_stop, unit_filter=config.unit_filter)
            print(f"Loaded {neurons.n_neurons} neurons from sorting phy ({phy_folder.name}) using filter {config.unit_filter!r}")
        else:
            folder_kind = inspect_phy_folder(phy_folder)
            neurons = load_neurons_from_spyk_circ_phy(phy_folder, t_stop=t_stop, include_groups=config.include_groups)
            print(f"Loaded {neurons.n_neurons} neurons from phy export ({phy_folder.name}, kind={folder_kind}) groups={config.include_groups}")
    except (FileNotFoundError, ValueError) as exc:
        print(f"WARNING: build_neurons_for_session: failed to load neurons from {phy_folder}: {exc}")
        return None
    sess.neurons = neurons
    if config.estimate_neuron_type:
        try:
            from neuropy.utils import neurons_util
            neuron_type = neurons_util.estimate_neuron_type(sess.neurons, plot=False)
            neurons.neuron_type = neuron_type[0]
        except Exception as exc:
            print(f"WARNING: build_neurons_for_session: failed to estimate neuron type: {exc}")
    if config.save_neurons:
        neurons.filename = sess.filePrefix.with_suffix(".neurons")
        try:
            print(f"saving out to {neurons.filename.as_posix()}...")
            neurons.save()
            print("\tdone.")
        except Exception as exc:
            print(f"WARNING: build_neurons_for_session: failed to save neurons to {neurons.filename}: {exc}")
    return neurons

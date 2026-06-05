from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

AnalyzerOverwriteMode = Literal["if_missing", "always", "never"]
PhyExportOverwriteMode = Literal["if_missing", "always"]
GoodUnitStrategy = Literal["phy", "sua", "sua_relaxed_prob", "sua_high_conf", "hybrid_phy_sua", "qm_and_sua"]
NeuronSourceType = Literal["spyk_circ", "sorting", "auto"]

DEFAULT_GAIN_TO_UV = 0.19499999284744263
DEFAULT_QM_THRESHOLDS = {"snr": {"greater": 5}, "firing_rate": {"greater": 0.1, "less": 200}, "isi_violations_ratio": {"less": 0.5}}
PHY_JOB_KWARGS = {"n_jobs": 8, "progress_bar": True, "chunk_duration": "4s"}


@dataclass
class BapunSessionConfig:
    basedir: Path
    basename: str
    n_channels: int = 195
    dat_file_sampling_rate: int = 30000
    eeg_sampling_rate: int = 1250
    gain_to_uV: float = DEFAULT_GAIN_TO_UV
    excluded_data_datetimes: list[str] = field(default_factory=list)


@dataclass
class SortingConfig:
    sorter_name: str
    output_folder: Path | None = None
    run_name: str | None = None
    use_filtered_recording: bool = False
    remove_existing_folder: bool = False
    delete_output_folder: bool = False
    verbose: bool = True
    export_phy: bool = False
    phy_export_folder: Path | None = None
    analyzer_overwrite: AnalyzerOverwriteMode = "if_missing"
    n_jobs: int = 8
    sorter_params: dict[str, object] = field(default_factory=dict)
    docker_image: bool | str | None = False
    singularity_image: bool | str | None = False
    delete_container_files: bool = True


@dataclass
class CurationConfig:
    strategy: GoodUnitStrategy = "sua_relaxed_prob"
    prob_default: float = 0.65
    prob_high: float = 0.8
    analyzer_overwrite: AnalyzerOverwriteMode = "if_missing"
    n_jobs: int = 8
    qm_thresholds: dict = field(default_factory=lambda: dict(DEFAULT_QM_THRESHOLDS))
    write_cluster_info: bool = True
    require_cluster_info: bool = True
    export_review_csv: bool = True
    preserve_human_phy_labels: bool = True


@dataclass
class RefinementConfig:
    apply_mahalanobis: bool = True
    apply_gmm: bool = True
    mahalanobis_threshold_std: float = 14.0
    gmm_n_components: int = 2
    min_spikes_for_split: int = 50
    min_outlier_spikes: int = 10
    min_subcluster_spikes: int = 10
    max_splits_per_unit: int = 1
    pca_n_components: int = 3


@dataclass
class QLabelConfig:
    amazing_snr: float = 8.0
    amazing_isi_violations_ratio: float = 0.1
    amazing_probability: float = 0.8
    sad_probability: float = 0.65
    interneuron_firing_rate_hz: float = 5.0
    interneuron_peak_to_valley_s: float = 0.00035


@dataclass
class PhyCurationResult:
    sorting: object
    sorting_analyzer: object
    analyzer_neural: object
    all_labels: object
    comparison: object
    good_units: object
    sorting_curated: object
    paths: object
    curation_review_path: Path | None = None
    cluster_info_path: Path | None = None


@dataclass
class SortingResult:
    sorter_name: str
    output_folder: Path
    phy_export_folder: Path | None = None
    analyzer_folder: Path | None = None
    sorting: object | None = None


@dataclass
class SorterCurationConfig:
    run_name: str
    strategy: GoodUnitStrategy = "sua_relaxed_prob"
    prob_default: float = 0.65
    prob_high: float = 0.8
    analyzer_overwrite: AnalyzerOverwriteMode = "if_missing"
    n_jobs: int = 8
    qm_thresholds: dict = field(default_factory=lambda: dict(DEFAULT_QM_THRESHOLDS))
    export_review_csv: bool = True
    preserve_human_phy_labels: bool = True
    apply_auto_merge: bool = True
    merge_preset: str = "similarity_correlograms"
    merge_recursive: bool = False
    apply_bombcell: bool = True
    include_mua_in_phy: bool = True
    remove_duplicated_spikes: bool = False
    remove_redundant_units: bool = False
    phy_export_overwrite: PhyExportOverwriteMode = "if_missing"


@dataclass
class NeuronLoadConfig:
    source_type: NeuronSourceType = "auto"
    phy_folder: Path | None = None
    curation_review_path: Path | None = None
    run_name: str | None = None
    include_groups: tuple[str, ...] = ("good", "mua")
    unit_filter: str = 'prediction == "sua"'
    save_neurons: bool = True
    estimate_neuron_type: bool = True


@dataclass
class SorterCurationResult:
    sorting: object
    sorting_analyzer: object
    analyzer_neural: object
    all_labels: object
    comparison: object
    good_units: object
    sorting_curated: object
    paths: object
    q_labels: object
    merge_log: list[dict[str, object]]
    split_log: list[dict[str, object]]
    curation_review_path: Path | None = None
    phy_curated_folder: Path | None = None
    good_units_path: Path | None = None
    num_units_initial: int = 0
    num_units_final: int = 0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

AnalyzerOverwriteMode = Literal["if_missing", "always", "never"]
GoodUnitStrategy = Literal["phy", "sua", "sua_relaxed_prob", "sua_high_conf", "hybrid_phy_sua", "qm_and_sua"]

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

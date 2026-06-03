from __future__ import annotations

import spikeinterface.curation as sc
import spikeinterface.full as si

from spikeinterface_pipeline.config import AnalyzerOverwriteMode, PHY_JOB_KWARGS

PHY_ANALYZER_EXTENSIONS = ["noise_levels", "random_spikes", "waveforms", "templates", "spike_locations", "spike_amplitudes", "correlograms", "principal_components", "quality_metrics", "template_metrics"]
SORTER_ANALYZER_EXTRA_EXTENSIONS = ["unit_locations", "template_similarity", "isi_histograms"]
METRIC_NAME_ALIASES = {"peak_to_trough_duration": "peak_to_valley", "trough_half_width": "half_width", "peak_after_to_trough_ratio": "peak_trough_ratio"}
LEGACY_TO_TEMPLATE_METRIC = {"peak_trough_ratio": "peak_after_to_trough_ratio", "half_width": "trough_half_width", "peak_to_valley": "peak_to_trough_duration"}
NOISE_NEURAL_MODEL = "SpikeInterface/UnitRefine_noise_neural_classifier"
SUA_MUA_MODEL = "SpikeInterface/UnitRefine_sua_mua_classifier"


def phy_job_kwargs(n_jobs: int = 8) -> dict:
    return {**PHY_JOB_KWARGS, "n_jobs": n_jobs}


def ensure_phy_analyzer_extensions(sorting_analyzer: object, *, n_jobs: int = 8) -> object:
    job_kwargs = phy_job_kwargs(n_jobs=n_jobs)
    missing = [ext for ext in PHY_ANALYZER_EXTENSIONS if ext != "template_metrics" and not sorting_analyzer.has_extension(ext)]
    if missing:
        sorting_analyzer.compute(missing, **job_kwargs)
    if not sorting_analyzer.has_extension("template_metrics"):
        sorting_analyzer.compute("template_metrics", include_multi_channel_metrics=True, **job_kwargs)
    if hasattr(sorting_analyzer, "save"):
        sorting_analyzer.save()
    return sorting_analyzer


def _available_metric_names(sorting_analyzer: object) -> set[str]:
    quality_metrics_ext = sorting_analyzer.get_extension("quality_metrics")
    template_metrics_ext = sorting_analyzer.get_extension("template_metrics")
    if quality_metrics_ext is None or template_metrics_ext is None:
        raise RuntimeError("quality_metrics and template_metrics must be computed before reading metric names; call ensure_phy_analyzer_extensions first.")
    quality_metrics = quality_metrics_ext.get_data()
    template_metrics = template_metrics_ext.get_data()
    names = set(quality_metrics.keys()) | set(template_metrics.keys())
    for new_name, old_name in METRIC_NAME_ALIASES.items():
        if new_name in names:
            names.add(old_name)
    return names


def build_phy_sorting_analyzer(sorting: object, recording_filtered: object, folder: object, *, analyzer_overwrite: AnalyzerOverwriteMode, n_jobs: int = 8) -> object:
    job_kwargs = phy_job_kwargs(n_jobs=n_jobs)
    folder_path = folder
    if analyzer_overwrite == "always" or (analyzer_overwrite == "if_missing" and not folder_path.exists()):
        sorting_analyzer = si.create_sorting_analyzer(sorting=sorting, recording=recording_filtered, format="binary_folder", folder=folder_path.as_posix(), overwrite=True)
        sorting_analyzer.compute(PHY_ANALYZER_EXTENSIONS, **job_kwargs)
        sorting_analyzer.compute("template_metrics", include_multi_channel_metrics=True)
        if hasattr(sorting_analyzer, "save"):
            sorting_analyzer.save()
    elif folder_path.exists():
        if analyzer_overwrite == "never":
            sorting_analyzer = si.load_sorting_analyzer(folder_path)
        else:
            sorting_analyzer = si.load_sorting_analyzer(folder_path)
    else:
        raise FileNotFoundError(f"SortingAnalyzer folder does not exist: {folder_path}")
    return ensure_phy_analyzer_extensions(sorting_analyzer, n_jobs=n_jobs)


def build_sorter_sorting_analyzer(sorting: object, recording_filtered: object, folder: object, *, analyzer_overwrite: AnalyzerOverwriteMode, n_jobs: int = 8) -> object:
    sorting_analyzer = build_phy_sorting_analyzer(sorting, recording_filtered, folder, analyzer_overwrite=analyzer_overwrite, n_jobs=n_jobs)
    return ensure_sorter_analyzer_extensions(sorting_analyzer, n_jobs=n_jobs)


def ensure_sorter_analyzer_extensions(sorting_analyzer: object, *, n_jobs: int = 8) -> object:
    job_kwargs = phy_job_kwargs(n_jobs=n_jobs)
    if not sorting_analyzer.has_extension("unit_locations"):
        sorting_analyzer.compute("unit_locations", method="monopolar_triangulation", **job_kwargs)
    if not sorting_analyzer.has_extension("template_similarity"):
        sorting_analyzer.compute("template_similarity", **job_kwargs)
    if not sorting_analyzer.has_extension("isi_histograms"):
        sorting_analyzer.compute("isi_histograms")
    return ensure_unitrefine_metrics(sorting_analyzer, n_jobs=n_jobs)


def ensure_unitrefine_metrics(sorting_analyzer: object, *, n_jobs: int = 8) -> object:
    job_kwargs = phy_job_kwargs(n_jobs=n_jobs)
    model, _model_info = sc.load_model(repo_id=NOISE_NEURAL_MODEL, trust_model=True)
    available = _available_metric_names(sorting_analyzer)
    missing = set(model.feature_names_in_) - available
    if not missing:
        return sorting_analyzer
    template_metric_names = [LEGACY_TO_TEMPLATE_METRIC[name] for name in missing if name in LEGACY_TO_TEMPLATE_METRIC]
    if template_metric_names:
        sorting_analyzer.compute("template_metrics", metric_names=template_metric_names, delete_existing_metrics=False, **job_kwargs)
    return sorting_analyzer

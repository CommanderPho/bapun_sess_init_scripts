from __future__ import annotations

from spikeinterface_pipeline.analyzer import build_phy_sorting_analyzer, ensure_unitrefine_metrics
from spikeinterface_pipeline.compat import patch_spikeinterface_metric_formatters
from spikeinterface_pipeline.config import BapunSessionConfig, CurationConfig, PhyCurationResult
from spikeinterface_pipeline.curation import apply_auto_quality_property, build_comparison_df, curate_sorting, resolve_good_units, run_unitrefine_two_stage
from spikeinterface_pipeline.paths import resolve_session_paths
from spikeinterface_pipeline.phy_export import export_curation_review_csv, write_phy_cluster_info
from spikeinterface_pipeline.recording import load_bapun_recording
from spikeinterface_pipeline.sorting_io import load_phy_sorting


def run_phy_curation_pipeline(session: BapunSessionConfig, curation: CurationConfig, *, patch_pandas_compat: bool = False) -> PhyCurationResult:
    if patch_pandas_compat:
        patch_spikeinterface_metric_formatters()
    paths = resolve_session_paths(session)
    _recording, recording_filtered = load_bapun_recording(session, paths)
    sorting = load_phy_sorting(paths)
    sorting_analyzer = build_phy_sorting_analyzer(sorting, recording_filtered, paths.phy_sorting_analyzer_folder, analyzer_overwrite=curation.analyzer_overwrite, n_jobs=curation.n_jobs)
    sorting_analyzer = ensure_unitrefine_metrics(sorting_analyzer, n_jobs=curation.n_jobs)
    all_labels, analyzer_neural, _noise_neural_labels = run_unitrefine_two_stage(sorting_analyzer)
    comparison = build_comparison_df(sorting, all_labels)
    good_units = resolve_good_units(sorting, sorting_analyzer, all_labels, curation)
    apply_auto_quality_property(sorting, all_labels)
    sorting_curated = curate_sorting(sorting, good_units)
    curation_review_path = None
    cluster_info_path = None
    if curation.export_review_csv:
        curation_review_path = export_curation_review_csv(comparison, good_units, paths.curation_review_path)
    if curation.write_cluster_info:
        cluster_info_path = write_phy_cluster_info(paths, all_labels, good_units, strategy=curation.strategy, require_cluster_info=curation.require_cluster_info)
    return PhyCurationResult(sorting=sorting, sorting_analyzer=sorting_analyzer, analyzer_neural=analyzer_neural, all_labels=all_labels, comparison=comparison, good_units=good_units, sorting_curated=sorting_curated, paths=paths, curation_review_path=curation_review_path, cluster_info_path=cluster_info_path)

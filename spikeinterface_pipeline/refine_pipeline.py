from __future__ import annotations

from pathlib import Path

import pandas as pd

from spikeinterface_pipeline.analyzer import build_phy_sorting_analyzer, ensure_unitrefine_metrics
from spikeinterface_pipeline.compat import patch_spikeinterface_metric_formatters
from spikeinterface_pipeline.config import BapunSessionConfig, CurationConfig, PhyCurationResult, QLabelConfig, RefinementConfig
from spikeinterface_pipeline.curation import apply_auto_quality_property, build_comparison_df, curate_sorting, resolve_good_units, run_unitrefine_two_stage
from spikeinterface_pipeline.paths import resolve_session_paths
from spikeinterface_pipeline.phy_export import write_phy_cluster_info
from spikeinterface_pipeline.q_labels import assign_q_labels
from spikeinterface_pipeline.recording import load_bapun_recording
from spikeinterface_pipeline.refinement import refine_units_with_splits
from spikeinterface_pipeline.sorting_io import load_phy_sorting


def run_phy_refinement_pipeline(session: BapunSessionConfig, curation: CurationConfig, refinement: RefinementConfig, q_config: QLabelConfig, *, patch_pandas_compat: bool = False, dry_run: bool = False) -> PhyCurationResult:
    if patch_pandas_compat:
        patch_spikeinterface_metric_formatters()

    paths = resolve_session_paths(session)
    _recording, recording_filtered = load_bapun_recording(session, paths)
    sorting = load_phy_sorting(paths)
    sorting_analyzer = build_phy_sorting_analyzer(sorting, recording_filtered, paths.phy_sorting_analyzer_folder, analyzer_overwrite=curation.analyzer_overwrite, n_jobs=curation.n_jobs)
    sorting_analyzer = ensure_unitrefine_metrics(sorting_analyzer, n_jobs=curation.n_jobs)

    sorting_analyzer, split_log = refine_units_with_splits(sorting_analyzer, refinement, n_jobs=curation.n_jobs, cache_folder=paths.phy_sorting_analyzer_folder, apply_splits=not dry_run)
    if not dry_run:
        sorting_analyzer = ensure_unitrefine_metrics(sorting_analyzer, n_jobs=curation.n_jobs)

    all_labels, analyzer_neural, _noise_neural_labels = run_unitrefine_two_stage(sorting_analyzer)
    refined_sorting = sorting_analyzer.sorting
    comparison = build_comparison_df(refined_sorting, all_labels)
    good_units = resolve_good_units(refined_sorting, sorting_analyzer, all_labels, curation)
    apply_auto_quality_property(refined_sorting, all_labels)
    sorting_curated = curate_sorting(refined_sorting, good_units)
    q_labels = assign_q_labels(all_labels, sorting_analyzer, good_units, q_config)

    review_path = None
    if curation.export_review_csv:
        review_path = _write_refinement_review_csv(comparison=comparison, q_labels=q_labels, good_units=good_units, split_log=split_log, output_path=Path(paths.basedir) / "spyk-circ" / f"{paths.basename}-refinement_review.csv")

    cluster_info_path = None
    if curation.write_cluster_info and not dry_run:
        cluster_info_path = write_phy_cluster_info(paths, all_labels, good_units, strategy=curation.strategy, require_cluster_info=curation.require_cluster_info, q_labels=q_labels, preserve_human_labels=curation.preserve_human_phy_labels)

    return PhyCurationResult(sorting=refined_sorting, sorting_analyzer=sorting_analyzer, analyzer_neural=analyzer_neural, all_labels=all_labels, comparison=comparison, good_units=good_units, sorting_curated=sorting_curated, paths=paths, curation_review_path=review_path, cluster_info_path=cluster_info_path)


def _write_refinement_review_csv(*, comparison: pd.DataFrame, q_labels: pd.Series, good_units: pd.Index, split_log: list[dict[str, object]], output_path: Path) -> Path:
    review = comparison.copy()
    review["good_unit"] = review.index.isin(good_units)
    review["q"] = q_labels.reindex(review.index).fillna("")
    split_df = pd.DataFrame(split_log)
    if not split_df.empty:
        split_counts = split_df.groupby("unit_id").size().rename("split_events")
        review["split_events"] = split_counts.reindex(review.index).fillna(0).astype(int)
    else:
        review["split_events"] = 0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    review.to_csv(output_path)
    return output_path

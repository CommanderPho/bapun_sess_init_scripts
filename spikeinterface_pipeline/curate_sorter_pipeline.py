from __future__ import annotations

from pathlib import Path

import pandas as pd
import spikeinterface.curation as sc

from spikeinterface_pipeline.analyzer import build_sorter_sorting_analyzer, ensure_sorter_analyzer_extensions
from spikeinterface_pipeline.compat import patch_spikeinterface_metric_formatters
from spikeinterface_pipeline.config import BapunSessionConfig, CurationConfig, QLabelConfig, RefinementConfig, SorterCurationConfig, SorterCurationResult
from spikeinterface_pipeline.curation import apply_auto_quality_property, build_comparison_df, compute_qm_labels, curate_sorting, resolve_good_units, run_unitrefine_two_stage
from spikeinterface_pipeline.merge_curation import apply_merge_curation, apply_pre_analyzer_sorting_cleanup, apply_redundant_unit_removal
from spikeinterface_pipeline.paths import resolve_session_paths, resolve_sorting_paths
from spikeinterface_pipeline.phy_export import export_curation_review_csv, export_curated_phy_folder, export_good_units_json, export_good_units_tsv
from spikeinterface_pipeline.q_labels import assign_q_labels
from spikeinterface_pipeline.recording import load_bapun_recording
from spikeinterface_pipeline.refinement import refine_units_with_splits
from spikeinterface_pipeline.sorting_io import load_sorter_folder


def run_sorter_curation_pipeline(session: BapunSessionConfig, sorter_curation: SorterCurationConfig, refinement: RefinementConfig, q_config: QLabelConfig, *, patch_pandas_compat: bool = False, dry_run: bool = False) -> SorterCurationResult:
    if patch_pandas_compat:
        patch_spikeinterface_metric_formatters()

    paths = resolve_sorting_paths(session, sorter_curation.run_name)
    if dry_run:
        _print_dry_run_plan(session, sorter_curation, refinement, paths)
        return SorterCurationResult(sorting=None, sorting_analyzer=None, analyzer_neural=None, all_labels=pd.DataFrame(), comparison=pd.DataFrame(), good_units=pd.Index([]), sorting_curated=None, paths=paths, q_labels=pd.Series(dtype=object), merge_log=[], split_log=[], phy_curated_folder=paths.phy_curated_folder, num_units_initial=0, num_units_final=0)

    if not paths.sorter_output_folder.exists():
        raise FileNotFoundError(f"sorter output not found: {paths.sorter_output_folder}. Run si-run-sorter first.")

    session_paths = resolve_session_paths(session)
    _recording, recording_filtered = load_bapun_recording(session, session_paths)
    sorting = load_sorter_folder(paths)
    num_units_initial = sorting.get_num_units()
    sorting = apply_pre_analyzer_sorting_cleanup(sorting, sorter_curation)

    curation = CurationConfig(strategy=sorter_curation.strategy, prob_default=sorter_curation.prob_default, prob_high=sorter_curation.prob_high, analyzer_overwrite=sorter_curation.analyzer_overwrite, n_jobs=sorter_curation.n_jobs, qm_thresholds=sorter_curation.qm_thresholds, export_review_csv=sorter_curation.export_review_csv, preserve_human_phy_labels=sorter_curation.preserve_human_phy_labels, write_cluster_info=False, require_cluster_info=False)

    sorting_analyzer = build_sorter_sorting_analyzer(sorting, recording_filtered, paths.sorting_analyzer_folder, analyzer_overwrite=sorter_curation.analyzer_overwrite, n_jobs=sorter_curation.n_jobs)
    sorting_analyzer = apply_redundant_unit_removal(sorting_analyzer, sorter_curation)
    sorting_analyzer, merge_log = apply_merge_curation(sorting_analyzer, sorter_curation, n_jobs=sorter_curation.n_jobs, dry_run=False)
    sorting_analyzer = ensure_sorter_analyzer_extensions(sorting_analyzer, n_jobs=sorter_curation.n_jobs)

    sorting_analyzer, split_log = refine_units_with_splits(sorting_analyzer, refinement, n_jobs=sorter_curation.n_jobs, cache_folder=paths.sorting_analyzer_folder, apply_splits=True)
    sorting_analyzer = ensure_sorter_analyzer_extensions(sorting_analyzer, n_jobs=sorter_curation.n_jobs)

    all_labels, analyzer_neural, _noise_neural_labels = run_unitrefine_two_stage(sorting_analyzer)
    refined_sorting = sorting_analyzer.sorting
    comparison = build_comparison_df(refined_sorting, all_labels)

    qm_labels = compute_qm_labels(sorting_analyzer, sorter_curation.qm_thresholds)
    comparison = comparison.join(qm_labels, how="left")

    if sorter_curation.apply_bombcell:
        try:
            bc_labels = sc.bombcell_label_units(sorting_analyzer=sorting_analyzer)
            comparison = comparison.join(bc_labels, how="left", rsuffix="_bombcell")
        except Exception as exc:
            print(f"Bombcell skipped: {exc}")

    good_units = resolve_good_units(refined_sorting, sorting_analyzer, all_labels, curation)
    apply_auto_quality_property(refined_sorting, all_labels)
    sorting_curated = curate_sorting(refined_sorting, good_units)
    q_labels = assign_q_labels(all_labels, sorting_analyzer, good_units, q_config)

    review_path = None
    if sorter_curation.export_review_csv:
        review = comparison.copy()
        review["good_unit"] = review.index.isin(good_units)
        review["q"] = q_labels.reindex(review.index).fillna("")
        split_df = pd.DataFrame(split_log)
        if not split_df.empty:
            split_counts = split_df.groupby("unit_id").size().rename("split_events")
            review["split_events"] = split_counts.reindex(review.index).fillna(0).astype(int)
        else:
            review["split_events"] = 0
        if merge_log:
            review["merge_events"] = len(merge_log)
        review_path = export_curation_review_csv(review, good_units, paths.curation_review_path)

    good_units_tsv_path = export_good_units_tsv(good_units, paths.good_units_path)
    export_good_units_json(good_units, paths.good_units_path.with_suffix(".json"))
    export_curated_phy_folder(sorting_analyzer, paths, all_labels, good_units, q_labels, strategy=sorter_curation.strategy, n_channels=session.n_channels, sampling_rate=session.dat_file_sampling_rate, n_jobs=sorter_curation.n_jobs, include_mua_in_phy=sorter_curation.include_mua_in_phy, preserve_human_phy_labels=sorter_curation.preserve_human_phy_labels, phy_export_overwrite=sorter_curation.phy_export_overwrite)

    num_units_final = len(good_units)
    print(f"Units: {num_units_initial} (sorter) -> {refined_sorting.get_num_units()} (after merge/split) -> {num_units_final} good (+ mua in phy if enabled)")
    print(f"Phy curated folder: {paths.phy_curated_folder}")
    print(f"Review CSV: {review_path}")
    print(f"Good units: {good_units_tsv_path}")

    return SorterCurationResult(sorting=refined_sorting, sorting_analyzer=sorting_analyzer, analyzer_neural=analyzer_neural, all_labels=all_labels, comparison=comparison, good_units=good_units, sorting_curated=sorting_curated, paths=paths, q_labels=q_labels, merge_log=merge_log, split_log=split_log, curation_review_path=review_path, phy_curated_folder=paths.phy_curated_folder, good_units_path=good_units_tsv_path, num_units_initial=num_units_initial, num_units_final=num_units_final)


def _print_dry_run_plan(session: BapunSessionConfig, sorter_curation: SorterCurationConfig, refinement: RefinementConfig, paths: object) -> None:
    print("dry_run=True")
    print(f"sorter_output_folder={paths.sorter_output_folder}")
    print(f"sorting_analyzer_folder={paths.sorting_analyzer_folder}")
    print(f"phy_curated_folder={paths.phy_curated_folder}")
    print(f"curation_review_path={paths.curation_review_path}")
    print(f"strategy={sorter_curation.strategy}")
    print(f"apply_auto_merge={sorter_curation.apply_auto_merge} preset={sorter_curation.merge_preset}")
    print(f"apply_mahalanobis={refinement.apply_mahalanobis} apply_gmm={refinement.apply_gmm}")
    print(f"apply_bombcell={sorter_curation.apply_bombcell} include_mua_in_phy={sorter_curation.include_mua_in_phy}")
    print(f"dat_file={paths.concatenated_dat_file}")

from __future__ import annotations

import spikeinterface.curation as sc

from spikeinterface_pipeline.analyzer import phy_job_kwargs
from spikeinterface_pipeline.config import SorterCurationConfig


def apply_pre_analyzer_sorting_cleanup(sorting: object, curation: SorterCurationConfig) -> object:
    if curation.remove_duplicated_spikes:
        sorting = sc.remove_duplicated_spikes(sorting)
    return sorting


def apply_merge_curation(sorting_analyzer: object, curation: SorterCurationConfig, *, n_jobs: int = 8, dry_run: bool = False) -> tuple[object, list[dict[str, object]]]:
    merge_log: list[dict[str, object]] = []
    if not curation.apply_auto_merge or dry_run:
        return sorting_analyzer, merge_log
    num_units_before = sorting_analyzer.sorting.get_num_units()
    sorting_analyzer = sc.auto_merge_units(sorting_analyzer, presets=[curation.merge_preset], recursive=curation.merge_recursive, **phy_job_kwargs(n_jobs=n_jobs))
    num_units_after = sorting_analyzer.sorting.get_num_units()
    merge_log.append({"stage": "auto_merge", "preset": curation.merge_preset, "recursive": curation.merge_recursive, "num_units_before": num_units_before, "num_units_after": num_units_after})
    return sorting_analyzer, merge_log


def apply_redundant_unit_removal(sorting_analyzer: object, curation: SorterCurationConfig) -> object:
    if not curation.remove_redundant_units:
        return sorting_analyzer
    return sc.remove_redundant_units(sorting_analyzer)

from __future__ import annotations

import pandas as pd
import spikeinterface.curation as sc

from spikeinterface_pipeline.analyzer import NOISE_NEURAL_MODEL, SUA_MUA_MODEL
from spikeinterface_pipeline.config import CurationConfig, GoodUnitStrategy

PHY_LABEL_MAP = {"sua": "good", "mua": "mua", "neural": "unclassified", "noise": "noise"}
AUTO_QUALITY_LABEL_MAP = {"sua": "good", "mua": "mua", "neural": "unclassified", "noise": "noise"}


def run_unitrefine_two_stage(sorting_analyzer: object) -> tuple[pd.DataFrame, object, pd.DataFrame]:
    noise_neural_labels = sc.model_based_label_units(sorting_analyzer=sorting_analyzer, repo_id=NOISE_NEURAL_MODEL, trust_model=True)
    noise_units = noise_neural_labels[noise_neural_labels["prediction"] == "noise"]
    analyzer_neural = sorting_analyzer.remove_units(noise_units.index)
    sua_mua_labels = sc.model_based_label_units(sorting_analyzer=analyzer_neural, repo_id=SUA_MUA_MODEL, trust_model=True)
    all_labels = pd.concat([sua_mua_labels, noise_units]).sort_index()
    return all_labels, analyzer_neural, noise_neural_labels


def _sorting_quality_series(sorting: object) -> pd.Series:
    quality = sorting.get_property("quality")
    if quality is None:
        return pd.Series("", index=sorting.unit_ids, dtype=object)
    return pd.Series(quality, index=sorting.unit_ids)


def build_comparison_df(sorting: object, all_labels: pd.DataFrame) -> pd.DataFrame:
    comparison = all_labels.copy()
    comparison["phy_label"] = all_labels.index.map(_sorting_quality_series(sorting))
    comparison["agreement"] = comparison["prediction"] == comparison["phy_label"]
    return comparison


def compute_qm_labels(sorting_analyzer: object, qm_thresholds: dict) -> pd.DataFrame:
    metrics_df = sorting_analyzer.get_extension("quality_metrics").get_data()
    return sc.threshold_metrics_label_units(metrics_df, thresholds=qm_thresholds, column_name="qm_good")


def select_good_units(sorting: object, all_labels: pd.DataFrame, *, strategy: GoodUnitStrategy, prob_default: float = 0.65, prob_high: float = 0.8, qm_labels: pd.DataFrame | None = None) -> pd.Index:
    quality = sorting.get_property("quality")
    phy_good_ids = sorting.unit_ids[quality == "good"] if quality is not None else sorting.unit_ids[[]]
    if strategy == "phy":
        good_units = pd.Index(phy_good_ids)
    elif strategy == "sua":
        good_units = all_labels.index[all_labels["prediction"] == "sua"]
    elif strategy == "sua_relaxed_prob":
        good_units = all_labels.index[(all_labels["prediction"] == "sua") & (all_labels["probability"] > prob_default)]
    elif strategy == "sua_high_conf":
        good_units = all_labels.index[(all_labels["prediction"] == "sua") & (all_labels["probability"] > prob_high)]
    elif strategy == "hybrid_phy_sua":
        is_phy_good = _sorting_quality_series(sorting) == "good"
        good_units = all_labels.index[(all_labels["prediction"] == "sua") | is_phy_good.reindex(all_labels.index, fill_value=False)]
        good_units = good_units.unique()
    elif strategy == "qm_and_sua":
        if qm_labels is None:
            raise ValueError("qm_labels required for strategy 'qm_and_sua'")
        qm_good_ids = qm_labels.index[qm_labels["qm_good"] == "good"]
        good_units = all_labels.index[(all_labels["prediction"] == "sua") & all_labels.index.isin(qm_good_ids)]
    else:
        raise ValueError(f"Unknown GOOD_UNIT_STRATEGY: {strategy}")
    return good_units


def apply_auto_quality_property(sorting: object, all_labels: pd.DataFrame) -> None:
    sorting.set_property("auto_quality", [AUTO_QUALITY_LABEL_MAP.get(p, "unclassified") for p in all_labels.loc[sorting.get_unit_ids(), "prediction"]])


def curate_sorting(sorting: object, good_units: pd.Index) -> object:
    return sorting.remove_units(remove_unit_ids=[u for u in sorting.get_unit_ids() if u not in good_units])


def resolve_good_units(sorting: object, sorting_analyzer: object, all_labels: pd.DataFrame, curation: CurationConfig) -> pd.Index:
    qm_labels = None
    if curation.strategy == "qm_and_sua":
        qm_labels = compute_qm_labels(sorting_analyzer, curation.qm_thresholds)
    return select_good_units(sorting, all_labels, strategy=curation.strategy, prob_default=curation.prob_default, prob_high=curation.prob_high, qm_labels=qm_labels)

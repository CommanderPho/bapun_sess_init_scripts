from __future__ import annotations

import numpy as np
import pandas as pd

from spikeinterface_pipeline.config import QLabelConfig


def assign_q_labels(all_labels: pd.DataFrame, sorting_analyzer: object, good_units: pd.Index, q_config: QLabelConfig) -> pd.Series:
    quality_metrics = sorting_analyzer.get_extension("quality_metrics").get_data()
    template_metrics = sorting_analyzer.get_extension("template_metrics").get_data()
    metrics = quality_metrics.join(template_metrics, how="left", rsuffix="_template")
    metrics = metrics.reindex(all_labels.index)

    snr = _metric_column(metrics, ["snr"])
    isi_viol = _metric_column(metrics, ["isi_violations_ratio"])
    firing_rate = _metric_column(metrics, ["firing_rate"])
    peak_to_valley = _metric_column(metrics, ["peak_to_valley", "peak_to_trough_duration"])

    q = pd.Series("", index=all_labels.index, dtype=object)
    predictions = all_labels["prediction"].astype(str).str.lower()
    probabilities = all_labels.get("probability", pd.Series(np.nan, index=all_labels.index))
    is_good = all_labels.index.isin(good_units)

    q[predictions == "mua"] = "6"

    interneuron_mask = is_good & (firing_rate > q_config.interneuron_firing_rate_hz) & (peak_to_valley < q_config.interneuron_peak_to_valley_s)
    q[interneuron_mask] = "8"

    amazing_mask = is_good & ~interneuron_mask & (snr > q_config.amazing_snr) & (isi_viol < q_config.amazing_isi_violations_ratio) & (probabilities > q_config.amazing_probability)
    q[amazing_mask] = "1"

    sad_mask = is_good & ~interneuron_mask & ~amazing_mask & (probabilities <= q_config.sad_probability)
    q[sad_mask] = "3"

    default_good_mask = is_good & (q == "")
    q[default_good_mask] = "2"
    return q


def _metric_column(metrics: pd.DataFrame, candidate_names: list[str]) -> pd.Series:
    for name in candidate_names:
        if name in metrics.columns:
            return pd.to_numeric(metrics[name], errors="coerce")
    return pd.Series(np.nan, index=metrics.index)

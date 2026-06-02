from __future__ import annotations

import numpy as np


def patch_spikeinterface_metric_formatters() -> None:
    import spikeinterface.curation.model_based_curation as _mbc
    import spikeinterface.curation.train_manual_curation as _tmc

    def _format_metric_dataframe_pandas15(input_data):
        input_data = input_data.map(lambda x: np.nan if np.isinf(x) else x)
        return input_data.astype("float32")

    _tmc._format_metric_dataframe = _format_metric_dataframe_pandas15
    _mbc._format_metric_dataframe = _format_metric_dataframe_pandas15

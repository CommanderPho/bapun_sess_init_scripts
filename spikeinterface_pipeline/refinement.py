from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.mixture import GaussianMixture

from spikeinterface_pipeline.analyzer import phy_job_kwargs
from spikeinterface_pipeline.config import RefinementConfig


def mahalanobis_outlier_labels(features: np.ndarray, threshold_std: float = 14.0) -> np.ndarray:
    distances = _mahalanobis_dist_calc(features, features)
    labels = np.ones(features.shape[0], dtype=int)
    labels[distances > (threshold_std**2)] = 2
    return labels


def gaussian_mixture_labels(features: np.ndarray, n_components: int = 2) -> np.ndarray:
    return GaussianMixture(n_components=n_components, random_state=0).fit_predict(features)


def labels_to_split_indices(labels: np.ndarray, min_subcluster_spikes: int) -> list[np.ndarray]:
    split_indices = [np.flatnonzero(labels == label) for label in np.unique(labels)]
    split_indices = [indices for indices in split_indices if indices.size >= min_subcluster_spikes]
    if len(split_indices) < 2:
        return []
    used = np.concatenate(split_indices)
    if used.size != labels.size:
        missing = np.setdiff1d(np.arange(labels.size), used)
        if missing.size > 0:
            split_indices.append(missing)
    return split_indices


def refine_units_with_splits(sorting_analyzer: object, refinement: RefinementConfig, *, n_jobs: int = 8, cache_folder: Path | None = None, apply_splits: bool = True) -> tuple[object, list[dict[str, object]]]:
    sorting_analyzer = _ensure_principal_components(sorting_analyzer, n_components=refinement.pca_n_components, n_jobs=n_jobs)
    all_spike_pcs = _load_all_spike_pcs(sorting_analyzer, n_jobs=n_jobs, cache_folder=cache_folder)
    unit_spike_rows = _build_unit_spike_rows(sorting_analyzer.sorting)
    split_log: list[dict[str, object]] = []

    if refinement.apply_mahalanobis:
        md_splits = _build_mahalanobis_splits(sorting_analyzer, all_spike_pcs, unit_spike_rows, refinement, split_log)
        if apply_splits:
            sorting_analyzer = _apply_split_map(sorting_analyzer, md_splits, n_jobs=n_jobs)
        if apply_splits and len(md_splits) > 0:
            all_spike_pcs = _load_all_spike_pcs(sorting_analyzer, n_jobs=n_jobs, cache_folder=cache_folder, force_recompute=True)
            unit_spike_rows = _build_unit_spike_rows(sorting_analyzer.sorting)

    if refinement.apply_gmm:
        gmm_splits = _build_gmm_splits(sorting_analyzer, all_spike_pcs, unit_spike_rows, refinement, split_log)
        if apply_splits:
            sorting_analyzer = _apply_split_map(sorting_analyzer, gmm_splits, n_jobs=n_jobs)

    return sorting_analyzer, split_log


def _ensure_principal_components(sorting_analyzer: object, *, n_components: int, n_jobs: int) -> object:
    if sorting_analyzer.has_extension("principal_components"):
        return sorting_analyzer
    sorting_analyzer.compute("principal_components", n_components=n_components, mode="by_channel_global", whiten=True, **phy_job_kwargs(n_jobs=n_jobs))
    return sorting_analyzer


def _load_all_spike_pcs(sorting_analyzer: object, *, n_jobs: int, cache_folder: Path | None, force_recompute: bool = False) -> np.ndarray:
    pca_extension = sorting_analyzer.get_extension("principal_components")
    base_folder = cache_folder if cache_folder is not None else Path(sorting_analyzer.folder)
    base_folder.mkdir(parents=True, exist_ok=True)
    pca_path = base_folder / "all_pca_projections.npy"
    if force_recompute and pca_path.exists():
        pca_path.unlink()
    if not pca_path.exists():
        pca_extension.run_for_all_spikes(file_path=pca_path, **phy_job_kwargs(n_jobs=n_jobs))
    return np.load(pca_path, mmap_mode="r")


def _build_unit_spike_rows(sorting: object) -> dict[object, np.ndarray]:
    spike_vector = sorting.to_spike_vector()
    unit_spike_rows: dict[object, np.ndarray] = {}
    for unit_id in sorting.unit_ids:
        unit_index = sorting.id_to_index(unit_id)
        unit_spike_rows[unit_id] = np.flatnonzero(spike_vector["unit_index"] == unit_index)
    return unit_spike_rows


def _best_channel_indices(sorting_analyzer: object, unit_id: object) -> np.ndarray:
    templates = sorting_analyzer.get_extension("templates").get_data()
    if isinstance(templates, dict):
        if "average" in templates:
            templates = templates["average"]
        else:
            templates = next(iter(templates.values()))
    unit_index = sorting_analyzer.sorting.id_to_index(unit_id)
    unit_template = np.asarray(templates[unit_index])
    if unit_template.ndim < 2:
        return np.array([0], dtype=int)
    channel_amplitudes = np.ptp(unit_template, axis=0)
    channel_amplitudes = np.nan_to_num(channel_amplitudes, nan=0.0, posinf=0.0, neginf=0.0)
    sorted_channels = np.argsort(channel_amplitudes)[::-1]
    return sorted_channels[: min(2, sorted_channels.size)]


def _unit_feature_matrix(all_spike_pcs: np.ndarray, rows: np.ndarray, channel_indices: np.ndarray) -> np.ndarray:
    unit_pcs = np.asarray(all_spike_pcs[rows])
    if unit_pcs.ndim != 3:
        return np.empty((0, 0), dtype=float)
    channel_indices = channel_indices[channel_indices < unit_pcs.shape[2]]
    if channel_indices.size == 0:
        return np.empty((0, 0), dtype=float)
    unit_features = unit_pcs[:, :, channel_indices].reshape(unit_pcs.shape[0], -1)
    unit_features = np.nan_to_num(unit_features, nan=0.0, posinf=0.0, neginf=0.0)
    return unit_features


def _build_mahalanobis_splits(sorting_analyzer: object, all_spike_pcs: np.ndarray, unit_spike_rows: dict[object, np.ndarray], refinement: RefinementConfig, split_log: list[dict[str, object]]) -> dict[object, list[list[int]]]:
    split_map: dict[object, list[list[int]]] = {}
    for unit_id in sorting_analyzer.unit_ids:
        rows = unit_spike_rows[unit_id]
        if rows.size < refinement.min_spikes_for_split:
            continue
        features = _unit_feature_matrix(all_spike_pcs, rows, _best_channel_indices(sorting_analyzer, unit_id))
        if features.shape[0] < refinement.min_spikes_for_split or features.shape[0] < features.shape[1]:
            continue
        labels = mahalanobis_outlier_labels(features, threshold_std=refinement.mahalanobis_threshold_std)
        outlier_count = int(np.sum(labels == 2))
        if outlier_count < refinement.min_outlier_spikes:
            continue
        split_indices = labels_to_split_indices(labels, min_subcluster_spikes=refinement.min_subcluster_spikes)
        if len(split_indices) < 2:
            continue
        split_map[unit_id] = [indices.tolist() for indices in split_indices[: refinement.max_splits_per_unit + 1]]
        split_log.append({"stage": "mahalanobis", "unit_id": unit_id, "num_spikes": int(rows.size), "outlier_spikes": outlier_count, "n_groups": len(split_map[unit_id])})
    return split_map


def _build_gmm_splits(sorting_analyzer: object, all_spike_pcs: np.ndarray, unit_spike_rows: dict[object, np.ndarray], refinement: RefinementConfig, split_log: list[dict[str, object]]) -> dict[object, list[list[int]]]:
    split_map: dict[object, list[list[int]]] = {}
    for unit_id in sorting_analyzer.unit_ids:
        rows = unit_spike_rows[unit_id]
        if rows.size < refinement.min_spikes_for_split:
            continue
        features = _unit_feature_matrix(all_spike_pcs, rows, _best_channel_indices(sorting_analyzer, unit_id))
        if features.shape[0] < refinement.min_spikes_for_split or features.shape[0] < refinement.gmm_n_components:
            continue
        labels = gaussian_mixture_labels(features, n_components=refinement.gmm_n_components)
        split_indices = labels_to_split_indices(labels, min_subcluster_spikes=refinement.min_subcluster_spikes)
        if len(split_indices) < 2:
            continue
        split_map[unit_id] = [indices.tolist() for indices in split_indices[: refinement.max_splits_per_unit + 1]]
        split_log.append({"stage": "gmm", "unit_id": unit_id, "num_spikes": int(rows.size), "n_groups": len(split_map[unit_id])})
    return split_map


def _apply_split_map(sorting_analyzer: object, split_map: dict[object, list[list[int]]], *, n_jobs: int) -> object:
    if len(split_map) == 0:
        return sorting_analyzer
    return sorting_analyzer.split_units(split_units=split_map, format="memory", **phy_job_kwargs(n_jobs=n_jobs))


def _mahalanobis_dist_calc(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    rx = X.shape[0]
    ry = Y.shape[0]
    mean_x = np.mean(X, axis=0)
    mean_tiled = np.tile(mean_x, (ry, 1))
    centered = X - np.tile(mean_x, (rx, 1))
    _q, r = np.linalg.qr(centered)
    least_squares = np.linalg.lstsq(r.T, (Y - mean_tiled).T, rcond=None)[0]
    return np.transpose(np.sum(least_squares * least_squares, axis=0)).dot(rx - 1)

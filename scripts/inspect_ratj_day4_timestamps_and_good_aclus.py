"""Inspect RatJ Day4 timestamps.npy and extract good aclus from Klusta kwik curation.

Run from repo root:
    cd bapun_sess_init_scripts && uv run python scripts/inspect_ratj_day4_timestamps_and_good_aclus.py
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np

SESSION_DIR = Path("/home/halechr/FastData/Bapun/RatJ/Day4Openfield")
SESSION_STEM = "RatJ_Day4_2019-06-26_04-56-12"
KLUSTA_DAY4_DIR = Path("/home/halechr/cloud/turbo/Bapun/RatJ/Day4")
PHY_CLUSTER_GROUP = {0: "unsorted", 1: "noise", 2: "mua", 3: "good"}


@dataclass(frozen=True)
class TimestampsSummary:
    n_samples: int
    sample_rate_hz: int
    duration_sec: float
    first_frame: int
    last_frame: int
    is_contiguous_plus_one: bool


def load_timestamps_summary(session_dir: Path = SESSION_DIR, session_stem: str = SESSION_STEM) -> TimestampsSummary:
    basics = np.load(session_dir / f"{session_stem}_basics.npy", allow_pickle=True).item()
    timestamps = np.load(session_dir / f"{session_stem}_timestamps.npy", mmap_mode="r")
    sample_rate_hz = int(basics["sRate"])
    return TimestampsSummary(
        n_samples=int(timestamps.size),
        sample_rate_hz=sample_rate_hz,
        duration_sec=float(timestamps.size / sample_rate_hz),
        first_frame=int(timestamps[0]),
        last_frame=int(timestamps[-1]),
        is_contiguous_plus_one=bool(np.all(timestamps[1:6] - timestamps[:5] == 1)),
    )


def spike_sample_to_session_seconds(spike_sample_index: int, timestamps_summary: TimestampsSummary) -> float:
    """Map a kwik spike sample index to session time in seconds using timestamps.npy."""
    timestamps = np.load(SESSION_DIR / f"{SESSION_STEM}_timestamps.npy", mmap_mode="r")
    return float(timestamps[int(spike_sample_index)] / timestamps_summary.sample_rate_hz)


def _kwik_channel_group_key(kwik_file: h5py.File) -> str:
    channel_group_keys = sorted(kwik_file["channel_groups"].keys(), key=int)
    if len(channel_group_keys) != 1:
        raise ValueError(f"expected one channel group in {kwik_file.filename}, found {channel_group_keys}")
    return channel_group_keys[0]


def _clusters_main_group(kwik_file: h5py.File, channel_group_key: str) -> h5py.Group | None:
    clusters = kwik_file[f"channel_groups/{channel_group_key}"].get("clusters")
    if clusters is None:
        return None
    return clusters.get("main")


def load_good_aclus_from_kwik(kwik_path: Path, *, shank_id: int) -> list[tuple[int, int]]:
    good_aclus: list[tuple[int, int]] = []
    with h5py.File(kwik_path, "r") as kwik_file:
        channel_group_key = _kwik_channel_group_key(kwik_file)
        clusters_main = _clusters_main_group(kwik_file, channel_group_key)
        if clusters_main is None:
            return good_aclus
        for cluster_id_str in clusters_main.keys():
            cluster_group = int(clusters_main[cluster_id_str].attrs.get("cluster_group", -1))
            if cluster_group == 3:
                good_aclus.append((shank_id, int(cluster_id_str)))
    return sorted(good_aclus)


def load_all_good_aclus(klusta_day4_dir: Path = KLUSTA_DAY4_DIR) -> tuple[list[tuple[int, int]], dict[str, Counter | str]]:
    all_good_aclus: list[tuple[int, int]] = []
    group_counts_by_shank: dict[str, Counter | str] = {}
    for shank_dir in sorted(p for p in klusta_day4_dir.glob("Shank*") if p.is_dir()):
        kwik_paths = sorted(shank_dir.glob("*.kwik"))
        if not kwik_paths:
            group_counts_by_shank[shank_dir.name] = "missing kwik"
            continue
        shank_id = int(shank_dir.name.replace("Shank", ""))
        with h5py.File(kwik_paths[0], "r") as kwik_file:
            channel_group_key = _kwik_channel_group_key(kwik_file)
            clusters_main = _clusters_main_group(kwik_file, channel_group_key)
            if clusters_main is None:
                group_counts_by_shank[shank_dir.name] = "no clusters (detection/clustering incomplete)"
                continue
            group_counts_by_shank[shank_dir.name] = Counter(int(clusters_main[cid].attrs.get("cluster_group", -1)) for cid in clusters_main.keys())
        all_good_aclus.extend(load_good_aclus_from_kwik(kwik_paths[0], shank_id=shank_id))
    return all_good_aclus, group_counts_by_shank


def main() -> None:
    timestamps_summary = load_timestamps_summary()
    print("=== timestamps.npy ===")
    print(f"path: {SESSION_DIR / f'{SESSION_STEM}_timestamps.npy'}")
    print(f"n_samples: {timestamps_summary.n_samples:,}")
    print(f"sample_rate_hz: {timestamps_summary.sample_rate_hz}")
    print(f"duration_sec: {timestamps_summary.duration_sec:.2f}")
    print(f"first_frame: {timestamps_summary.first_frame}")
    print(f"last_frame: {timestamps_summary.last_frame}")
    print(f"contiguous +1 frames: {timestamps_summary.is_contiguous_plus_one}")
    print("\nThis file is the per-sample frame index stream for the .dat file.")
    print("It does not contain cluster IDs or curation labels, so good aclus cannot be read from it directly.")

    all_good_aclus, group_counts_by_shank = load_all_good_aclus()
    print("\n=== good aclus from Klusta kwik (cluster_group == 3) ===")
    for shank_name, counts in group_counts_by_shank.items():
        if isinstance(counts, str):
            print(f"{shank_name}: {counts}")
            continue
        readable_counts = {PHY_CLUSTER_GROUP.get(group_id, str(group_id)): count for group_id, count in counts.items()}
        print(f"{shank_name}: {readable_counts}")
    print(f"\nTotal good aclus (shank_id, local_cluster_id): {len(all_good_aclus)}")
    print(f"First 20: {all_good_aclus[:20]}")

    if all_good_aclus:
        example_shank, example_cluster = all_good_aclus[0]
        example_kwik = sorted((KLUSTA_DAY4_DIR / f"Shank{example_shank}").glob("*.kwik"))[0]
        with h5py.File(example_kwik, "r") as kwik_file:
            channel_group_key = _kwik_channel_group_key(kwik_file)
            spike_samples = kwik_file[f"channel_groups/{channel_group_key}/spikes/time_samples"]
            spike_clusters = kwik_file[f"channel_groups/{channel_group_key}/spikes/clusters/main"]
            example_spike_idx = int(np.where(spike_clusters[:] == example_cluster)[0][0])
            example_sample_index = int(spike_samples[example_spike_idx])
        example_time_sec = spike_sample_to_session_seconds(example_sample_index, timestamps_summary)
        print(f"\nExample: shank={example_shank} cluster={example_cluster} -> sample_index={example_sample_index} -> t={example_time_sec:.6f} sec")


if __name__ == "__main__":
    main()

from __future__ import annotations

import spikeinterface.extractors as se
import spikeinterface.full as si
from probeinterface.io import read_prb

from spikeinterface_pipeline.config import BapunSessionConfig
from spikeinterface_pipeline.paths import SessionPaths


def load_bapun_recording(config: BapunSessionConfig, paths: SessionPaths) -> tuple[object, object]:
    if not paths.concatenated_dat_file.exists():
        raise FileNotFoundError(f"concatenated_dat_file does not exist: {paths.concatenated_dat_file}")
    recording = se.read_binary(file_paths=paths.concatenated_dat_file.as_posix(), sampling_frequency=config.dat_file_sampling_rate, num_channels=config.n_channels, dtype="int16")
    recording.set_channel_gains(config.gain_to_uV)
    recording.set_channel_offsets(0)
    if not paths.prb_path.exists():
        raise FileNotFoundError(f"prb_path does not exist: {paths.prb_path}")
    probe = read_prb(paths.prb_path).probes[0]
    recording = recording.set_probe(probe, in_place=False)
    recording_filtered = si.bandpass_filter(recording)
    return recording, recording_filtered

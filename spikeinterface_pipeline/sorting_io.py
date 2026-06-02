from __future__ import annotations

import spikeinterface.extractors as se

from spikeinterface_pipeline.paths import SessionPaths


def load_phy_sorting(paths: SessionPaths) -> object:
    if not paths.phy_gui_dir.exists():
        raise FileNotFoundError(f"phy_gui_dir does not exist: {paths.phy_gui_dir}")
    return se.read_phy(paths.phy_gui_dir)


def load_spykingcircus_sorting(paths: SessionPaths) -> object:
    if not paths.spiking_circus_dir.exists():
        raise FileNotFoundError(f"spiking_circus_dir does not exist: {paths.spiking_circus_dir}")
    return se.read_spykingcircus(paths.spiking_circus_dir)

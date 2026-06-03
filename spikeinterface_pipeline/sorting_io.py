from __future__ import annotations

import spikeinterface.extractors as se
import spikeinterface.full as si

from spikeinterface_pipeline.paths import SessionPaths, SortingSessionPaths


def load_sorter_folder(paths: SortingSessionPaths) -> object:
    if not paths.sorter_output_folder.exists():
        raise FileNotFoundError(f"sorter_output_folder does not exist: {paths.sorter_output_folder}")
    return si.read_sorter_folder(paths.sorter_output_folder)


def load_phy_sorting(paths: SessionPaths) -> object:
    if not paths.phy_gui_dir.exists():
        raise FileNotFoundError(f"phy_gui_dir does not exist: {paths.phy_gui_dir}")
    return se.read_phy(paths.phy_gui_dir)


def load_spykingcircus_sorting(paths: SessionPaths) -> object:
    if not paths.spiking_circus_dir.exists():
        raise FileNotFoundError(f"spiking_circus_dir does not exist: {paths.spiking_circus_dir}")
    return se.read_spykingcircus(paths.spiking_circus_dir)

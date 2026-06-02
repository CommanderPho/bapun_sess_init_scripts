from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from neuropy.core.session.init_from_raw_data import find_first_file_rglob, windows_to_wsl_path_if_needed

from spikeinterface_pipeline.config import BapunSessionConfig


@dataclass
class SessionPaths:
    basedir: Path
    basename: str
    xml_path: Path
    concatenated_dat_file: Path
    prb_path: Path
    spiking_circus_dir: Path
    phy_gui_dir: Path
    phy_sorting_analyzer_folder: Path
    curation_review_path: Path


def resolve_session_paths(config: BapunSessionConfig) -> SessionPaths:
    basedir = windows_to_wsl_path_if_needed(config.basedir).resolve()
    basename = config.basename
    xml_path = find_first_file_rglob(basedir, "*.xml", recursive=False)
    concatenated_dat_file = windows_to_wsl_path_if_needed(basedir.joinpath("spyk-circ", f"{basename}.dat")).resolve()
    prb_path = windows_to_wsl_path_if_needed(basedir.joinpath("spyk-circ", f"{basename}.prb")).resolve()
    spiking_circus_dir = windows_to_wsl_path_if_needed(basedir.joinpath("spyk-circ", basename)).resolve()
    phy_gui_dir = windows_to_wsl_path_if_needed(basedir.joinpath("spyk-circ", basename, f"{basename}-merged.GUI")).resolve()
    phy_sorting_analyzer_folder = windows_to_wsl_path_if_needed(basedir.joinpath("spyk-circ", f"{basename}-phy-sorting_analyzer")).resolve()
    curation_review_path = basedir.joinpath("spyk-circ", f"{basename}-curation_review.csv")
    return SessionPaths(basedir=basedir, basename=basename, xml_path=xml_path, concatenated_dat_file=concatenated_dat_file, prb_path=prb_path, spiking_circus_dir=spiking_circus_dir, phy_gui_dir=phy_gui_dir, phy_sorting_analyzer_folder=phy_sorting_analyzer_folder, curation_review_path=curation_review_path)

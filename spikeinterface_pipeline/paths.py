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


@dataclass
class SortingSessionPaths:
    basedir: Path
    basename: str
    run_name: str
    xml_path: Path
    concatenated_dat_file: Path
    prb_path: Path
    sorter_output_folder: Path
    sorting_analyzer_folder: Path
    phy_raw_folder: Path
    phy_curated_folder: Path
    curation_review_path: Path
    good_units_path: Path


def resolve_sorting_paths(config: BapunSessionConfig, run_name: str) -> SortingSessionPaths:
    session_paths = resolve_session_paths(config)
    sorting_root = session_paths.basedir.joinpath("SORTING")
    sorter_output_folder = sorting_root.joinpath(run_name).resolve()
    sorting_analyzer_folder = sorting_root.joinpath(f"{run_name}_sorting_analyzer").resolve()
    phy_raw_folder = sorting_root.joinpath(f"{run_name}_phy").resolve()
    phy_curated_folder = sorting_root.joinpath(f"{run_name}_phy_curated").resolve()
    curation_review_path = sorting_root.joinpath(f"{run_name}_curation_review.csv").resolve()
    good_units_path = sorting_root.joinpath(f"{run_name}_good_units.tsv").resolve()
    return SortingSessionPaths(basedir=session_paths.basedir, basename=session_paths.basename, run_name=run_name, xml_path=session_paths.xml_path, concatenated_dat_file=session_paths.concatenated_dat_file, prb_path=session_paths.prb_path, sorter_output_folder=sorter_output_folder, sorting_analyzer_folder=sorting_analyzer_folder, phy_raw_folder=phy_raw_folder, phy_curated_folder=phy_curated_folder, curation_review_path=curation_review_path, good_units_path=good_units_path)

from __future__ import annotations

from pathlib import Path

from neuropy.core.session.init_from_raw_data import windows_to_wsl_path_if_needed
import spikeinterface.full as si
from spikeinterface.sorters import installed_sorters, run_sorter

from spikeinterface_pipeline.analyzer import phy_job_kwargs
from spikeinterface_pipeline.config import BapunSessionConfig, SortingConfig, SortingResult
from spikeinterface_pipeline.paths import resolve_session_paths
from spikeinterface_pipeline.recording import load_bapun_recording

PHY_EXPORT_EXTENSIONS = ["random_spikes", "waveforms", "templates"]


def resolve_sorting_output_folder(basedir: Path, basename: str, sorting_config: SortingConfig) -> Path:
    if sorting_config.output_folder is not None:
        return windows_to_wsl_path_if_needed(Path(sorting_config.output_folder)).resolve()
    sorting_root = windows_to_wsl_path_if_needed(basedir.joinpath("SORTING")).resolve()
    run_name = sorting_config.run_name if sorting_config.run_name else f"{sorting_config.sorter_name}_{basename}"
    return sorting_root.joinpath(run_name).resolve()


def resolve_phy_export_folder(basedir: Path, output_folder: Path, sorting_config: SortingConfig) -> Path:
    if sorting_config.phy_export_folder is not None:
        return windows_to_wsl_path_if_needed(Path(sorting_config.phy_export_folder)).resolve()
    sorting_root = windows_to_wsl_path_if_needed(basedir.joinpath("SORTING")).resolve()
    if sorting_config.run_name:
        return sorting_root.joinpath(f"{sorting_config.run_name}_phy").resolve()
    return output_folder.with_name(f"{output_folder.name}_phy").resolve()


def _build_phy_export_analyzer(sorting: object, recording_filtered: object, analyzer_folder: Path, n_jobs: int, analyzer_overwrite: str) -> object:
    if analyzer_overwrite == "always":
        sorting_analyzer = si.create_sorting_analyzer(sorting=sorting, recording=recording_filtered, format="binary_folder", folder=analyzer_folder.as_posix(), overwrite=True)
        sorting_analyzer.compute(PHY_EXPORT_EXTENSIONS, **phy_job_kwargs(n_jobs=n_jobs))
        return sorting_analyzer
    if analyzer_folder.exists():
        return si.load_sorting_analyzer(analyzer_folder)
    if analyzer_overwrite == "never":
        raise FileNotFoundError(f"SortingAnalyzer folder does not exist: {analyzer_folder}")
    sorting_analyzer = si.create_sorting_analyzer(sorting=sorting, recording=recording_filtered, format="binary_folder", folder=analyzer_folder.as_posix(), overwrite=True)
    sorting_analyzer.compute(PHY_EXPORT_EXTENSIONS, **phy_job_kwargs(n_jobs=n_jobs))
    return sorting_analyzer


def run_bapun_sorter(session: BapunSessionConfig, sorting_config: SortingConfig, *, dry_run: bool = False) -> SortingResult:
    available_sorters = installed_sorters()
    if sorting_config.sorter_name not in available_sorters:
        raise ValueError(f"Sorter '{sorting_config.sorter_name}' is not installed. Installed sorters: {available_sorters}. Run `uv run si-run-sorter list` to inspect availability.")
    paths = resolve_session_paths(session)
    recording, recording_filtered = load_bapun_recording(session, paths)
    recording_to_sort = recording_filtered if sorting_config.use_filtered_recording else recording
    output_folder = resolve_sorting_output_folder(paths.basedir, session.basename, sorting_config)
    output_folder.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        phy_export_folder = resolve_phy_export_folder(paths.basedir, output_folder, sorting_config) if sorting_config.export_phy else None
        analyzer_folder = output_folder.with_name(f"{output_folder.name}_sorting_analyzer") if sorting_config.export_phy else None
        return SortingResult(sorter_name=sorting_config.sorter_name, output_folder=output_folder, phy_export_folder=phy_export_folder, analyzer_folder=analyzer_folder, sorting=None)
    sorting = run_sorter(sorter_name=sorting_config.sorter_name, recording=recording_to_sort, folder=output_folder, remove_existing_folder=sorting_config.remove_existing_folder, delete_output_folder=sorting_config.delete_output_folder, verbose=sorting_config.verbose, docker_image=sorting_config.docker_image, singularity_image=sorting_config.singularity_image, delete_container_files=sorting_config.delete_container_files, **sorting_config.sorter_params)
    phy_export_folder = None
    analyzer_folder = None
    if sorting_config.export_phy:
        analyzer_folder = output_folder.with_name(f"{output_folder.name}_sorting_analyzer")
        phy_export_folder = resolve_phy_export_folder(paths.basedir, output_folder, sorting_config)
        sorting_analyzer = _build_phy_export_analyzer(sorting=sorting, recording_filtered=recording_filtered, analyzer_folder=analyzer_folder, n_jobs=sorting_config.n_jobs, analyzer_overwrite=sorting_config.analyzer_overwrite)
        sparsity = si.compute_sparsity(sorting_analyzer) if sorting_analyzer.get_num_channels() > 64 else None
        si.export_to_phy(sorting_analyzer=sorting_analyzer, output_folder=phy_export_folder, remove_if_exists=True, sparsity=sparsity, verbose=sorting_config.verbose, **phy_job_kwargs(n_jobs=sorting_config.n_jobs))
    return SortingResult(sorter_name=sorting_config.sorter_name, output_folder=output_folder, phy_export_folder=phy_export_folder, analyzer_folder=analyzer_folder, sorting=sorting)

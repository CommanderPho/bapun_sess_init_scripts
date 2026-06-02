from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

from spikeinterface.sorters import installed_sorters, sorter_dict

from spikeinterface_pipeline.config import BapunSessionConfig, SortingConfig
from spikeinterface_pipeline.sorting import run_bapun_sorter


def _parse_scalar(value: str) -> object:
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered == "none":
        return None
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def _parse_sorter_params(items: list[str], json_blob: str | None) -> dict[str, object]:
    params: dict[str, object] = {}
    if json_blob:
        decoded = json.loads(json_blob)
        if not isinstance(decoded, dict):
            raise ValueError("--sorter-params-json must decode to a JSON object")
        params.update(decoded)
    for item in items:
        if "=" not in item:
            raise ValueError(f"Invalid --sorter-param '{item}'. Expected KEY=VALUE.")
        key, raw_value = item.split("=", 1)
        params[key] = _parse_scalar(raw_value)
    return params


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run SpikeInterface sorters on Bapun sessions.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    list_parser = subparsers.add_parser("list", help="List installed sorters and versions.")
    list_parser.add_argument("--show-default-params", action="store_true", help="Print each installed sorter's default parameter dictionary")
    run_parser = subparsers.add_parser(
        "run",
        help="Run a sorter and optionally export to Phy.",
        epilog=(
            "Examples:\n"
            "  uv run si-run-sorter list\n"
            "  uv run si-run-sorter run --basedir /home/halechr/FastData/Bapun/RatS/Day1Openfield --basename RatS-Day1Openfield --sorter kilosort4 --run-name folder_kilosort4_v1\n"
            "  uv run si-run-sorter run --basedir /home/halechr/FastData/Bapun/RatS/Day1Openfield --basename RatS-Day1Openfield --sorter tridesclous2 --use-filtered --output-folder /home/halechr/FastData/Bapun/RatS/Day1Openfield/SORTING/folder_TDC2 --remove-existing-folder\n"
            "  uv run si-run-sorter run --basedir /home/halechr/FastData/Bapun/RatS/Day1Openfield --basename RatS-Day1Openfield --sorter kilosort4 --run-name folder_KS4 --export-phy --phy-export-folder /home/halechr/FastData/Bapun/RatS/Day1Openfield/SORTING/folder_KS4_phy"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    run_parser.add_argument("--basedir", type=Path, required=True, help="Session root directory (e.g. Day1Openfield)")
    run_parser.add_argument("--basename", type=str, required=True, help="Session basename (e.g. RatS-Day1Openfield)")
    run_parser.add_argument("--n-channels", type=int, default=195)
    run_parser.add_argument("--dat-sampling-rate", type=int, default=30000)
    run_parser.add_argument("--gain-to-uv", type=float, default=0.19499999284744263)
    run_parser.add_argument("--sorter", type=str, required=True, help="Sorter name (use `si-run-sorter list` to inspect installed sorters)")
    run_parser.add_argument("--output-folder", type=Path, default=None, help="Absolute output folder for sorter artifacts")
    run_parser.add_argument("--run-name", type=str, default=None, help="Folder name under {basedir}/SORTING when --output-folder is omitted")
    run_parser.add_argument("--use-filtered", action="store_true", help="Sort using bandpass-filtered recording instead of raw recording")
    run_parser.add_argument("--remove-existing-folder", action="store_true", help="Delete an existing sorter output folder before running")
    run_parser.add_argument("--delete-output-folder", action="store_true", help="Delete output folder after sorter finishes")
    run_parser.add_argument("--dry-run", action="store_true", help="Resolve paths and settings without running the sorter")
    run_parser.add_argument("--quiet", action="store_true", help="Reduce sorter verbosity")
    run_parser.add_argument("--export-phy", action="store_true", help="Build analyzer and export sorting to a Phy folder")
    run_parser.add_argument("--phy-export-folder", type=Path, default=None, help="Output folder for Phy export")
    run_parser.add_argument("--analyzer-overwrite", type=str, default="if_missing", choices=["if_missing", "always", "never"])
    run_parser.add_argument("--n-jobs", type=int, default=8)
    run_parser.add_argument("--docker-image", nargs="?", const=True, default=False, help="Run sorter in Docker; optional image name")
    run_parser.add_argument("--singularity-image", nargs="?", const=True, default=False, help="Run sorter in Singularity; optional image path/name")
    run_parser.add_argument("--keep-container-files", action="store_true", default=False, help="Keep temporary container files when using docker/singularity")
    run_parser.add_argument("--sorter-param", action="append", default=[], help="Sorter override as KEY=VALUE (can be repeated)")
    run_parser.add_argument("--sorter-params-json", type=str, default=None, help="JSON object of sorter overrides")
    return parser


def _run_list(show_default_params: bool) -> int:
    available = installed_sorters()
    if not available:
        print("No installed sorters detected.")
        return 0
    for sorter_name in available:
        sorter_version = sorter_dict[sorter_name].get_sorter_version()
        print(f"{sorter_name}: {sorter_version}")
        if show_default_params:
            print(f"default_params={sorter_dict[sorter_name].default_params()}")
    return 0


def _run_sort(args: argparse.Namespace) -> int:
    sorter_params = _parse_sorter_params(args.sorter_param, args.sorter_params_json)
    session = BapunSessionConfig(basedir=args.basedir, basename=args.basename, n_channels=args.n_channels, dat_file_sampling_rate=args.dat_sampling_rate, gain_to_uV=args.gain_to_uv)
    config = SortingConfig(sorter_name=args.sorter, output_folder=args.output_folder, run_name=args.run_name, use_filtered_recording=args.use_filtered, remove_existing_folder=args.remove_existing_folder, delete_output_folder=args.delete_output_folder, verbose=not args.quiet, export_phy=args.export_phy, phy_export_folder=args.phy_export_folder, analyzer_overwrite=args.analyzer_overwrite, n_jobs=args.n_jobs, sorter_params=sorter_params, docker_image=args.docker_image, singularity_image=args.singularity_image, delete_container_files=not args.keep_container_files)
    result = run_bapun_sorter(session, config, dry_run=args.dry_run)
    print(f"sorter={result.sorter_name}")
    print(f"output_folder={result.output_folder}")
    if args.dry_run:
        print("dry_run=True")
        print(f"use_filtered={args.use_filtered}")
    else:
        print(f"dry_run=False")
        if result.sorting is not None:
            print(f"num_units={result.sorting.get_num_units()}")
            print(f"num_segments={result.sorting.get_num_segments()}")
    if result.analyzer_folder is not None:
        print(f"analyzer_folder={result.analyzer_folder}")
    if result.phy_export_folder is not None:
        print(f"phy_export_folder={result.phy_export_folder}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "list":
        return _run_list(show_default_params=args.show_default_params)
    if args.command == "run":
        return _run_sort(args)
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

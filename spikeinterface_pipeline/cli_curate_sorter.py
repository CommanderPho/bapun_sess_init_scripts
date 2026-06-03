from __future__ import annotations

import argparse
from pathlib import Path

from spikeinterface_pipeline.config import BapunSessionConfig, QLabelConfig, RefinementConfig, SorterCurationConfig
from spikeinterface_pipeline.curate_sorter_pipeline import run_sorter_curation_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Post-sorter automated curation: merge, split, label, and export NeuroPy-ready Phy folder.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    run_parser = subparsers.add_parser("run", help="Run full curation pipeline on si-run-sorter output.")
    run_parser.add_argument("--basedir", type=Path, required=True, help="Session root directory (e.g. Day1Openfield)")
    run_parser.add_argument("--basename", type=str, required=True, help="Session basename (e.g. RatS-Day1Openfield)")
    run_parser.add_argument("--run-name", type=str, required=True, help="Sorter run folder name under SORTING (e.g. folder_KS4_v1)")
    run_parser.add_argument("--n-channels", type=int, default=195)
    run_parser.add_argument("--dat-sampling-rate", type=int, default=30000)
    run_parser.add_argument("--gain-to-uv", type=float, default=0.19499999284744263)
    run_parser.add_argument("--strategy", type=str, default="sua_relaxed_prob", choices=["phy", "sua", "sua_relaxed_prob", "sua_high_conf", "hybrid_phy_sua", "qm_and_sua"])
    run_parser.add_argument("--prob-default", type=float, default=0.65)
    run_parser.add_argument("--prob-high", type=float, default=0.8)
    run_parser.add_argument("--analyzer-overwrite", type=str, default="if_missing", choices=["if_missing", "always", "never"])
    run_parser.add_argument("--phy-export-overwrite", type=str, default="if_missing", choices=["if_missing", "always"], help="if_missing: skip export_to_phy when curated Phy folder already exists; always: rebuild Phy export")
    run_parser.add_argument("--n-jobs", type=int, default=8)
    run_parser.add_argument("--patch-pandas-compat", action="store_true", help="Apply pandas/SI metric formatter patch (Great Lakes)")
    run_parser.add_argument("--dry-run", action="store_true", help="Print resolved paths and pipeline plan without running")
    run_parser.add_argument("--skip-review-csv", action="store_true", help="Do not write curation review CSV")
    run_parser.add_argument("--overwrite-human-phy-labels", action="store_true", help="Overwrite existing human Phy group/q labels in curated folder")
    run_parser.add_argument("--skip-auto-merge", action="store_true", help="Skip auto_merge_units")
    run_parser.add_argument("--merge-preset", type=str, default="similarity_correlograms")
    run_parser.add_argument("--merge-recursive", action="store_true", help="Run auto_merge recursively")
    run_parser.add_argument("--skip-bombcell", action="store_true", help="Skip bombcell_label_units")
    run_parser.add_argument("--exclude-mua-from-phy", action="store_true", help="Do not export MUA units to Phy (only good)")
    run_parser.add_argument("--remove-duplicates", action="store_true", help="Apply remove_duplicated_spikes before analyzer")
    run_parser.add_argument("--remove-redundant", action="store_true", help="Apply remove_redundant_units on analyzer")
    run_parser.add_argument("--skip-mahalanobis", action="store_true", help="Skip Mahalanobis-based outlier split stage")
    run_parser.add_argument("--skip-gmm", action="store_true", help="Skip Gaussian mixture split stage")
    run_parser.add_argument("--mahalanobis-threshold", type=float, default=14.0)
    run_parser.add_argument("--gmm-components", type=int, default=2)
    run_parser.add_argument("--min-spikes-for-split", type=int, default=50)
    run_parser.add_argument("--min-outlier-spikes", type=int, default=10)
    run_parser.add_argument("--min-subcluster-spikes", type=int, default=10)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command != "run":
        return 1
    session = BapunSessionConfig(basedir=args.basedir, basename=args.basename, n_channels=args.n_channels, dat_file_sampling_rate=args.dat_sampling_rate, gain_to_uV=args.gain_to_uv)
    sorter_curation = SorterCurationConfig(run_name=args.run_name, strategy=args.strategy, prob_default=args.prob_default, prob_high=args.prob_high, analyzer_overwrite=args.analyzer_overwrite, n_jobs=args.n_jobs, export_review_csv=not args.skip_review_csv, preserve_human_phy_labels=not args.overwrite_human_phy_labels, apply_auto_merge=not args.skip_auto_merge, merge_preset=args.merge_preset, merge_recursive=args.merge_recursive, apply_bombcell=not args.skip_bombcell, include_mua_in_phy=not args.exclude_mua_from_phy, remove_duplicated_spikes=args.remove_duplicates, remove_redundant_units=args.remove_redundant, phy_export_overwrite=args.phy_export_overwrite)
    refinement = RefinementConfig(apply_mahalanobis=not args.skip_mahalanobis, apply_gmm=not args.skip_gmm, mahalanobis_threshold_std=args.mahalanobis_threshold, gmm_n_components=args.gmm_components, min_spikes_for_split=args.min_spikes_for_split, min_outlier_spikes=args.min_outlier_spikes, min_subcluster_spikes=args.min_subcluster_spikes)
    q_config = QLabelConfig()
    result = run_sorter_curation_pipeline(session, sorter_curation, refinement, q_config, patch_pandas_compat=args.patch_pandas_compat, dry_run=args.dry_run)
    if args.dry_run:
        return 0
    print(f"Strategy: {sorter_curation.strategy} -> {result.num_units_final} good units (of {result.num_units_initial} sorter units)")
    if hasattr(result.all_labels, "prediction"):
        print(f"Model predictions:\n{result.all_labels['prediction'].value_counts()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
from pathlib import Path

from spikeinterface_pipeline.config import BapunSessionConfig, CurationConfig
from spikeinterface_pipeline.pipeline import run_phy_curation_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run SpikeInterface UnitRefine curation on Bapun Phy-sorted data.")
    parser.add_argument("--basedir", type=Path, required=True, help="Session root directory (e.g. Day1Openfield)")
    parser.add_argument("--basename", type=str, required=True, help="Session basename (e.g. RatS-Day1Openfield)")
    parser.add_argument("--n-channels", type=int, default=195)
    parser.add_argument("--dat-sampling-rate", type=int, default=30000)
    parser.add_argument("--gain-to-uv", type=float, default=0.19499999284744263)
    parser.add_argument("--strategy", type=str, default="sua_relaxed_prob", choices=["phy", "sua", "sua_relaxed_prob", "sua_high_conf", "hybrid_phy_sua", "qm_and_sua"])
    parser.add_argument("--prob-default", type=float, default=0.65)
    parser.add_argument("--prob-high", type=float, default=0.8)
    parser.add_argument("--analyzer-overwrite", type=str, default="if_missing", choices=["if_missing", "always", "never"])
    parser.add_argument("--n-jobs", type=int, default=8)
    parser.add_argument("--patch-pandas-compat", action="store_true", help="Apply pandas/SI metric formatter patch (Great Lakes)")
    parser.add_argument("--skip-cluster-info", action="store_true", help="Do not write cluster_info.tsv")
    parser.add_argument("--allow-missing-cluster-info", action="store_true", help="Do not fail if cluster_info.tsv is missing")
    parser.add_argument("--skip-review-csv", action="store_true", help="Do not write curation review CSV")
    parser.add_argument("--overwrite-human-phy-labels", action="store_true", help="Allow algorithmic updates to overwrite existing human Phy group/q labels")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    session = BapunSessionConfig(basedir=args.basedir, basename=args.basename, n_channels=args.n_channels, dat_file_sampling_rate=args.dat_sampling_rate, gain_to_uV=args.gain_to_uv)
    curation = CurationConfig(strategy=args.strategy, prob_default=args.prob_default, prob_high=args.prob_high, analyzer_overwrite=args.analyzer_overwrite, n_jobs=args.n_jobs, write_cluster_info=not args.skip_cluster_info, require_cluster_info=not args.allow_missing_cluster_info, export_review_csv=not args.skip_review_csv, preserve_human_phy_labels=not args.overwrite_human_phy_labels)
    result = run_phy_curation_pipeline(session, curation, patch_pandas_compat=args.patch_pandas_compat)
    print(f"Strategy: {curation.strategy} -> {len(result.good_units)} good units (of {len(result.all_labels)} total)")
    print(f"Model predictions:\n{result.all_labels['prediction'].value_counts()}")
    if result.curation_review_path is not None:
        print(f"Review CSV: {result.curation_review_path}")
    if result.cluster_info_path is not None:
        print(f"Updated cluster_info.tsv: {result.cluster_info_path}")
    print(f"Good units: {list(result.good_units)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

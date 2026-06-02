from __future__ import annotations

import argparse
from pathlib import Path

from spikeinterface_pipeline.config import BapunSessionConfig, CurationConfig, QLabelConfig, RefinementConfig
from spikeinterface_pipeline.refine_pipeline import run_phy_refinement_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Phy-style SpikeInterface refinement (Mahalanobis + GMM + UnitRefine) on Bapun data.")
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
    parser.add_argument("--skip-review-csv", action="store_true", help="Do not write refinement review CSV")
    parser.add_argument("--skip-mahalanobis", action="store_true", help="Skip Mahalanobis-based outlier split stage")
    parser.add_argument("--skip-gmm", action="store_true", help="Skip Gaussian mixture split stage")
    parser.add_argument("--mahalanobis-threshold", type=float, default=14.0)
    parser.add_argument("--gmm-components", type=int, default=2)
    parser.add_argument("--min-spikes-for-split", type=int, default=50)
    parser.add_argument("--min-outlier-spikes", type=int, default=10)
    parser.add_argument("--min-subcluster-spikes", type=int, default=10)
    parser.add_argument("--dry-run", action="store_true", help="Run through labeling/review without applying cluster_info.tsv updates")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    session = BapunSessionConfig(basedir=args.basedir, basename=args.basename, n_channels=args.n_channels, dat_file_sampling_rate=args.dat_sampling_rate, gain_to_uV=args.gain_to_uv)
    curation = CurationConfig(strategy=args.strategy, prob_default=args.prob_default, prob_high=args.prob_high, analyzer_overwrite=args.analyzer_overwrite, n_jobs=args.n_jobs, write_cluster_info=not args.skip_cluster_info, require_cluster_info=not args.allow_missing_cluster_info, export_review_csv=not args.skip_review_csv)
    refinement = RefinementConfig(apply_mahalanobis=not args.skip_mahalanobis, apply_gmm=not args.skip_gmm, mahalanobis_threshold_std=args.mahalanobis_threshold, gmm_n_components=args.gmm_components, min_spikes_for_split=args.min_spikes_for_split, min_outlier_spikes=args.min_outlier_spikes, min_subcluster_spikes=args.min_subcluster_spikes)
    q_config = QLabelConfig()
    result = run_phy_refinement_pipeline(session, curation, refinement, q_config, patch_pandas_compat=args.patch_pandas_compat, dry_run=args.dry_run)
    print(f"Strategy: {curation.strategy} -> {len(result.good_units)} good units (of {len(result.all_labels)} total)")
    print(f"Model predictions:\n{result.all_labels['prediction'].value_counts()}")
    if result.curation_review_path is not None:
        print(f"Refinement review CSV: {result.curation_review_path}")
    if result.cluster_info_path is not None:
        print(f"Updated cluster_info.tsv: {result.cluster_info_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

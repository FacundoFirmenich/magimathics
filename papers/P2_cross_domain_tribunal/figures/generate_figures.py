#!/usr/bin/env python3
"""Generate P2 benchmark figures from frozen REAL-04 data."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]


def save(fig, stem: str) -> None:
    fig.tight_layout()
    fig.savefig(HERE / f"{stem}.svg")
    fig.savefig(HERE / f"{stem}.pdf")
    plt.close(fig)


def signature_sensitivity() -> None:
    src = ROOT / "research/umi-real04/data/METRICS_BY_SIGNATURE.csv"
    df = pd.read_csv(src)
    x = np.arange(len(df))
    width = 0.24
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width, df["precision"], width, label="Precision")
    ax.bar(x, df["specificity"], width, label="Specificity")
    ax.bar(x + width, df["false_discovery_rate"], width, label="False discovery rate")
    ax.set_xticks(x, [p.title() for p in df["profile"]])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Metric")
    ax.set_title("Semantic-signature strength controls tribunal selectivity")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "P2_FIG4A_SIGNATURE_SENSITIVITY")


def missing_evidence() -> None:
    src = ROOT / "research/umi-real04/data/MISSING_EVIDENCE_ROBUSTNESS.csv"
    df = pd.read_csv(src)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(df["missing_count"], df["coverage"], marker="o", label="Coverage")
    ax.plot(df["missing_count"], df["accuracy_on_adjudicated"], marker="o", label="Accuracy among adjudicated")
    ax.plot(df["missing_count"], df["false_positive_rate_on_adjudicated"], marker="o", label="False-positive rate")
    ax.set_xticks(df["missing_count"])
    ax.set_ylim(-0.02, 1.05)
    ax.set_xlabel("Tribunal dimensions withheld")
    ax.set_ylabel("Metric")
    ax.set_title("Conservative abstention under missing evidence")
    ax.legend(frameon=False)
    ax.grid(alpha=0.25)
    save(fig, "P2_FIG4B_MISSING_EVIDENCE")


if __name__ == "__main__":
    signature_sensitivity()
    missing_evidence()
    print("PASS_P2_FIGURE_GENERATION")

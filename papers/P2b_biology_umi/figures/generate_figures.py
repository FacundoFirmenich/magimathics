#!/usr/bin/env python3
"""Generate current P2b figures from frozen REAL-01 and REAL-02 data."""
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


def repressilator_interventions() -> None:
    src = ROOT / "research/umi-real01/data/intervention_results.csv"
    df = pd.read_csv(src)
    labels = {
        "baseline_closed_repression_cycle": "Baseline",
        "ablate_PZ_to_X": "Ablate cI→LacI",
        "ablate_PX_to_Y": "Ablate LacI→TetR",
        "ablate_PY_to_Z": "Ablate TetR→cI",
        "rewire_PX_to_Y_as_PZ_to_Y": "Source rewire",
        "flip_PX_to_Y_to_activation": "Sign flip",
        "one_node_self_repression": "1-node",
        "two_node_mutual_repression": "2-node",
    }
    df = df[df["run"].isin(labels)].copy()
    df["label"] = df["run"].map(labels)
    df["plot_value"] = df["relative_amplitude"].clip(lower=1e-18)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.bar(np.arange(len(df)), df["plot_value"])
    ax.set_yscale("log")
    ax.set_xticks(np.arange(len(df)), df["label"], rotation=35, ha="right")
    ax.set_ylabel("Relative amplitude (baseline = 1)")
    ax.set_title("Repressilator signature collapses under critical interventions")
    ax.grid(axis="y", alpha=0.25)
    save(fig, "P2B_FIG2A_REPRESSILATOR_INTERVENTIONS")


def repressilator_phase() -> None:
    src = ROOT / "research/umi-real01/data/substitution_and_phase.csv"
    df = pd.read_csv(src)
    df = df[df["record_type"] == "phase"].copy()
    names = {
        "PZ_cI_to_PY_TetR": "cI→TetR",
        "PY_TetR_to_PX_LacI": "TetR→LacI",
        "PX_LacI_to_next_PZ_cI": "LacI→cI",
    }
    df["label"] = df["key"].map(names)
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.bar(df["label"], df["value_2"])
    ax.axhline(1 / 3, linestyle="--", linewidth=1, label="1/3 period")
    ax.set_ylim(0.3328, 0.3338)
    ax.set_ylabel("Mean phase lag / period")
    ax.set_title("Cyclic phase order is distributed in near-equal thirds")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "P2B_FIG2B_REPRESSILATOR_PHASE")


def rpa_minimality() -> None:
    src = ROOT / "research/umi-real02/data/minimality_audit.csv"
    df = pd.read_csv(src)
    df["plot_value"] = df["adaptation_ratio"].clip(lower=1e-16)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(np.arange(len(df)), df["plot_value"])
    ax.set_yscale("log")
    ax.set_xticks(np.arange(len(df)), df["carrier"], rotation=30, ha="right")
    ax.set_ylabel("Terminal error / peak deviation")
    ax.set_title("Only the full sensor–integrator–actuator carrier achieves RPA")
    ax.axhline(1e-3, linestyle="--", linewidth=1, label="Frozen pass threshold")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "P2B_FIG3_RPA_MINIMALITY")


if __name__ == "__main__":
    repressilator_interventions()
    repressilator_phase()
    rpa_minimality()
    print("PASS_P2B_FIGURE_GENERATION")

#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np


def magnetic_fitness(spec: dict) -> dict:
    k = spec.get("coverage_factor")
    limit = spec.get("maximum_expanded_uncertainty_mT")
    components = spec.get("components_standard_uncertainty_mT", {})
    if k is None or limit is None or not components or any(v is None for v in components.values()):
        return {
            "status": "ABSTAIN_NUMERIC_MAGNETIC_FITNESS_INPUT_INCOMPLETE",
            "pass": False,
            "combined_standard_uncertainty_mT": None,
            "expanded_uncertainty_mT": None,
        }
    vals = np.asarray([float(v) for v in components.values()], dtype=float)
    if np.any(vals < 0) or float(k) <= 0 or float(limit) <= 0:
        raise ValueError("invalid magnetic fitness input")
    uc = float(np.sqrt(np.sum(vals * vals)))
    U = float(k) * uc
    return {
        "status": "PASS_MAGNETIC_FITNESS" if U <= float(limit) else "FAIL_MAGNETIC_FITNESS",
        "pass": bool(U <= float(limit)),
        "combined_standard_uncertainty_mT": uc,
        "coverage_factor": float(k),
        "expanded_uncertainty_mT": U,
        "maximum_expanded_uncertainty_mT": float(limit),
        "components": {str(k): float(v) for k, v in components.items()},
    }


def q_value(V: float, Vs: float, Vc: float) -> float:
    D = float(Vc) - float(Vs)
    if D <= 0:
        raise ValueError("Vc must exceed Vs")
    return (float(Vc) - float(V)) / D


def q_jacobian(V: float, Vs: float, Vc: float) -> np.ndarray:
    D = float(Vc) - float(Vs)
    if D <= 0:
        raise ValueError("Vc must exceed Vs")
    Q = q_value(V, Vs, Vc)
    return np.asarray([-1.0 / D, Q / D, (1.0 - Q) / D], dtype=float)


def propagate_q_uncertainty(V: float, Vs: float, Vc: float, covariance) -> dict:
    S = np.asarray(covariance, dtype=float)
    if S.shape != (3, 3):
        raise ValueError("Q covariance must be 3x3 for (V,Vs,Vc)")
    S = (S + S.T) / 2
    vals = np.linalg.eigvalsh(S)
    if vals[0] < -1e-12:
        raise ValueError("covariance not PSD")
    J = q_jacobian(V, Vs, Vc)
    var = float(J @ S @ J)
    if var < -1e-12:
        raise ValueError("negative propagated variance")
    return {
        "Q": float(q_value(V, Vs, Vc)),
        "jacobian_V_Vs_Vc": J.tolist(),
        "standard_uncertainty_Q": float(math.sqrt(max(var, 0.0))),
    }


def bethe_q(Qplus: float, Qminus: float, z: float) -> float:
    Qp = float(Qplus)
    Qm = float(Qminus)
    zz = float(z)
    if not (0 <= Qp < 1 and Qp <= Qm <= 1 and zz > 1):
        raise ValueError("invalid Bethe inversion input")
    alpha = (Qm - Qp) / (1 - Qp)
    y = (1 - alpha) ** (1 / zz)
    den = 1 - (1 - Qp) * y ** (zz - 1)
    if abs(den) < 1e-15:
        raise ValueError("singular Bethe inversion")
    q = (1 - y) / den
    return float(q)


def bethe_q_jacobian(Qplus: float, Qminus: float, z: float) -> np.ndarray:
    x = np.asarray([Qplus, Qminus, z], dtype=float)
    base = bethe_q(*x)
    out = np.zeros(3)
    for j in range(3):
        h = 1e-6 * (1 + abs(x[j]))
        xp = x.copy()
        xm = x.copy()
        xp[j] += h
        xm[j] -= h
        # Use one-sided differences at domain boundaries.
        try:
            fp = bethe_q(*xp)
            fm = bethe_q(*xm)
            out[j] = (fp - fm) / (2 * h)
        except ValueError:
            xp = x.copy()
            xp[j] += h
            fp = bethe_q(*xp)
            out[j] = (fp - base) / h
    return out


def propagate_bethe_q_uncertainty(Qplus: float, Qminus: float, z: float, covariance) -> dict:
    S = np.asarray(covariance, dtype=float)
    if S.shape != (3, 3):
        raise ValueError("Bethe covariance must be 3x3 for (Qplus,Qminus,z)")
    S = (S + S.T) / 2
    vals = np.linalg.eigvalsh(S)
    if vals[0] < -1e-12:
        raise ValueError("covariance not PSD")
    J = bethe_q_jacobian(Qplus, Qminus, z)
    var = float(J @ S @ J)
    return {
        "q": bethe_q(Qplus, Qminus, z),
        "jacobian_Qplus_Qminus_z": J.tolist(),
        "standard_uncertainty_q": float(math.sqrt(max(var, 0.0))),
    }


def compile_fitness(doc: dict) -> dict:
    mag = magnetic_fitness(doc.get("magnetic", {}))
    ads = doc.get("adsorption", {})
    limits_ready = (
        ads.get("maximum_standard_uncertainty_Q") is not None
        and ads.get("maximum_standard_uncertainty_q") is not None
    )
    all_ready = mag["status"] not in {"ABSTAIN_NUMERIC_MAGNETIC_FITNESS_INPUT_INCOMPLETE"} and limits_ready
    return {
        "profile": "hgmf-hg39-fitness-output/1.0",
        "magnetic": mag,
        "adsorption_limits_ready": bool(limits_ready),
        "status": "PASS_FITNESS_INPUT_COMPILED" if all_ready else "ABSTAIN_NUMERIC_FITNESS_INPUT_INCOMPLETE",
        "arming_eligible": bool(all_ready and mag["pass"]),
        "note": "Compilation is a software result. Arming also requires real receipts and future-only checks.",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    doc = json.loads(args.input.read_text(encoding="utf-8"))
    result = compile_fitness(doc)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

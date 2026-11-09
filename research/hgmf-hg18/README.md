# HGMF‑HG18 — Context-Area Form, Dimensional Transgression and Cross-Carrier Holonomy

**Verdict:** `PASS_CONTEXT_AREA_FORM_CONDITIONAL / PASS_DIMENSIONLESS_CURVATURE_DENSITY / PASS_CROSS_CARRIER_QGT_TRANSPORT_CONDITIONAL / FAIL_DIMENSIONAL_TRANSGRESSION / FAIL_STANDARD_HOLONOMY_EXCLUSION`.

## Core result

For a regular oriented two-parameter family of pure states, the quantum geometric tensor defines

\[
dA_Q=\sqrt{\det g}\,d\lambda^1\wedge d\lambda^2,
\qquad
\chi_Q=\frac{\mathcal F_{12}}{2\sqrt{\det g}},
\qquad |\chi_Q|\le1.
\]

This is a canonical area of state distinguishability and a coordinate/gauge-invariant dimensionless curvature density. It is not a dimensionful physical area or scale.

## Exact witnesses

For the Bloch sphere:

\[
g_{\theta\theta}=1/4,
\quad g_{\phi\phi}=\sin^2\theta/4,
\quad \mathcal F_{\theta\phi}=\sin\theta/2,
\]

so

\[
\chi_Q=1,
\quad \mathrm{Vol}_Q=\pi,
\quad C_1=1.
\]

A constant isometric qutrit embedding preserves the QGT exactly. A parameter-dependent hidden ancilla preserves the qubit's coarse outcomes but changes

\[
\chi_Q:1\mapsto1/\sqrt5,
\qquad
\mathrm{Vol}_Q:\pi\mapsto\pi\sqrt5.
\]

Thus coarse UMI equivalence is insufficient for geometric transport; a QGT-isometric transport is required.

## Scale no-go

Coordinate rescaling changes curvature components and metric-area density by reciprocal Jacobian factors while preserving \(\chi_Q\), holonomy and Chern number. A dimensionful curvature density requires an independently derived physical area form, calibration and coupling. The same phase `0.37` assigned to context areas `0.25` and `100` gives densities differing by a factor `400`.

## Mixed-state boundary

Monotonicity does not select a unique mixed-state metric; the Petz family remains. Bures/SLD is distinguished but not uniquely derived by the current HGMF axioms.

## Standard-QM boundary

Berry curvature, quantum metric, Chern numbers, quantum-volume inequalities and their direct measurement belong to standard quantum mechanics. HG18 derives no nonzero HGMF correction and no energy, time or length scale.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `CONTEXT AREA + DIMENSIONLESS CURVATURE PASS CONDITIONAL; SCALE + STANDARD EXCLUSION FAIL/HOLD`.

## Next gate

`HGMF‑HG19 — Operational Context Metric, Action Cost and Dimensional Coupling`.

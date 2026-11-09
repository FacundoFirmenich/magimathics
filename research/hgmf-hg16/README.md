# HGMF‑HG16 — Base de correcciones protogeométricas y espectroscopia multigap

**Fecha:** 9 November 2026  
**Verdict:** `PASS_MINIMAL_CORRECTION_BASIS / PASS_STANDARD-QM ABSORPTION NO-GO / FAIL_PHYSICAL_HGMF CORRECTION / FAIL_SCALE IDENTIFICATION`.

## Core result

A reduced anomaly is not a proto-geometric signature. Every CPTP channel has a standard unitary dilation, and every causal finite-time process tensor has a standard unitary-circuit realization. HGMF attribution must therefore be formulated on a quotient of observations by a frozen standard nuisance class.

For an equispaced `d`-level system, the complex equal-gap residual dimension is

\[
\binom d2-(d-1)=\binom{d-1}{2}.
\]

A qutrit is the first system capable of falsifying scalar-time smearing. In the exact four-level witnesses:

- scalar-time defect: `0`;
- general standard dephasing defect: `0.09933824336616051`, with CP defect `0`;
- non-CP witness defect: `0.46130177212481277`.

Thus falsifying scalar time does not falsify standard quantum mechanics.

## Attribution basis

\[
\mathbf J=(J_{gap},J_{CP},J_{QRF},J_{order},J_{std},J_{scale},J_{carrier}).
\]

A candidate requires simultaneously:

- outside scalar-time and the frozen nuisance class;
- inside a physically consistent process class;
- QRF covariance after transporting states and interventions;
- a common dimensionful scaling law;
- cross-carrier transport;
- held-out prediction.

## Exact diagnostics

- consistent QRF channel-cycle defect: `1.4848073818342024e-15`;
- inconsistent relative-cycle defect: `0.4488307605303952`;
- standard unitary-environment order witness: trace distance `0.03362182206058064`.

Order dependence, memory and non-Markovianity are therefore non-specific.

## Scale no-go

The current axioms do not select a unique correction functional or a dimensionful coupling. Multiple even analytic functions vanish in the same standard limit. No `E_HG`, `tau_HG`, `ell_HG` or `lambda_HG` has been derived.

```text
CORRECTION DIAGNOSTIC BASIS = PASS
NONZERO PHYSICAL HGMF TERM = FAIL_NOT_DERIVED
DIMENSIONFUL SCALE = FAIL_NOT_DERIVED
DISTINGUISHABILITY FROM STANDARD QM = FAIL
```

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `CORRECTION BASIS + ATTRIBUTION CONTRACT PASS; PHYSICAL CORRECTION AND SCALE FAIL/HOLD`.

## Next gate

`HGMF‑HG17 — Cross-Context Cocycle Curvature and Scale Selection`.

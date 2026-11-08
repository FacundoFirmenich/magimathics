# HGMF‑UMI‑21 — Carrier‑Native Semantic Measure and Scale‑Range Extension

**Date:** 8 November 2026  
**Verdict:** `PASS_NATIVE_MULTISCALE_ONLY / FAIL_SURROGATE_TRIBUNAL / FAIL_TRANSPORT_INVARIANCE`

## Portfolio

- **Paper A:** remains `EXPERIMENT_READY` under UMI‑17.
- **Paper B:** retains the formal UMI core; this corpus provides carrier-native multiscale organization but not an empirical scale-rich multifractal UMI.
- **Paper C:** receives no empirical bridge or support for HGMF/geometric constants.

## Native witness measure

- `H`: within-layer/within-branch response variation.
- `D`: opposite-history or opposite-branch separation at matched control.
- `V`: change from the previous historical layer at matched control.
- `J=(HDV)^(1/3)`: joint coactivation.
- `T=H+D+V`: total semantic mass.

No model-comparison residual defines the measure.

## Scale tribunal

Six native covers were retained: `2, 4, 8, 16, 32, 64` boxes, with positive moments `q = 0.5, 1, 2, 3, 4`.

- total multiscale persistence: `13/13` records;
- full surrogate passes for `T`: `0/13`;
- full surrogate passes for `J`: `0/13`.

Therefore:

```text
PASS_NATIVE_MULTISCALE
FAIL_EMPIRICAL_SCALE-RICH_MULTIFRACTALITY
```

## Cross-carrier transport

Exact permutation tests on generalized-dimension vectors:

| Axis | Exact p | Verdict |
|---|---:|---|
| H | 0.012587 | FAIL_DIFFERENCE_DETECTED |
| D | 0.001399 | FAIL_DIFFERENCE_DETECTED |
| V | 0.450350 | HOLD_NO_EQUIVALENCE_MARGIN |
| J | 0.075524 | HOLD_NO_EQUIVALENCE_MARGIN |
| T | 0.106294 | HOLD_NO_EQUIVALENCE_MARGIN |

Because the complete signature includes all axes:

```text
FAIL_TRANSPORT_INVARIANCE
```

## Triaxial coupling

H/D/V dependence is detected in `13/13` records, but coupling magnitude is carrier-specific:

- magnetic mean total correlation: `0.931728`;
- adsorption mean: `0.476660`;
- exact transport p-value: `1/715`.

```text
PASS_NATIVE_TRIAXIAL_COUPLING
FAIL_COUPLING_TRANSPORT
```

## Scientific closure

The negative result of UMI‑20 survives after replacing model-residual witnesses with carrier-native measures. Both carriers possess multiscale organization and genuine triaxial interrelation, but blocks/regimes reproduce the apparent spectral curvature and the complete spectrum does not transport.

## Next gate

`HGMF‑UMI‑22 — Native Intervention Hierarchies and Independent Scale Extension`.

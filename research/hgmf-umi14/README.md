# HGMF‑UMI‑14 — External Replication and Horizon‑Local Calibration

**Verdict:** `PASS_EXTERNAL_REPLICATION / PASS_HIDDEN_STATE_REQUIREMENT / FAIL_CONTROL-ONLY SCALE / FAIL_EXTERNAL HORIZON CALIBRATION`

## Core results

- Eight public training-effect HDF5 assets and four original wPF controls were materialized and decoded.
- Declared acquisition metadata match across the twelve magnetic histories.
- At matched programmed field amplitudes, response span differs by up to ~1200×; therefore field amplitude, temperature and declared settings are not a sufficient scale state.
- At the same ~200 mT amplitude, span differs by <1% while the HEB proxy differs by ~46.945 mT; amplitude and asymmetry require a vector state.
- The chronological training-effect sequence has a monotone field/span relation, but field amplitude and acquisition order are confounded.
- Frozen UMI‑13 forecasting was tested on external NIST runs 1, 2, 3, 4, 6 and 7: 65/72 horizon tasks and 15/18 complete-suffix tasks reached 90% coverage.
- The single externally triggered compressed set preserved coverage but did not reduce complete-suffix width and remained wider than the full run span.
- Horizon-local calibration improved coverage in 0/72 tasks, worsened 2 and left 70 unchanged.

## Semantic conclusion

The invariant that survives is the history-bearing semantic core, not a universal operator, universal scale, field-only regime or universal interval width.

## Next gate

`HGMF‑UMI‑15 — Orthogonal History‑State Constitutive Law`: crossed field/training protocols, vector response state, causal reset probes and external sharpness.

## Audit

Binary materialization and analysis were executed on the isolated draft PR #11. This branch is not intended for merge; it preserves the reproducibility contract and source receipts.

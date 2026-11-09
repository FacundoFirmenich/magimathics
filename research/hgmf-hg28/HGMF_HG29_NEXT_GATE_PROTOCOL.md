# HGMF‑HG29 — Confirmatory loss functions, nuisance closure and third-carrier escalation

## Objective

Freeze the quantitative predictive-loss and nuisance-exclusion rules needed to move from replicated causal interaction to a nonstandard cross-carrier response, and determine the evidence required beyond two carriers.

## Gate A — held-out loss

Choose one proper predictive loss for modal amplitudes and one geometry-aware loss for nodes/signs before data.

## Gate B — kernel margin

Define a simultaneous held-out margin against all frozen alternative kernels, with explicit handling of nested/intersection boundaries.

## Gate C — nuisance closure

Specify which standard models must be rejected, approximated or dominated:
- drift;
- hidden state;
- control geometry;
- process tensor;
- alternative spectral kernels;
- carrier-map misspecification.

## Gate D — transcarrier loss

Define no-refit transfer loss and calibration of carrier-specific measurement units.

## Gate E — third carrier

Derive when a third non-isomorphic carrier is required for escalation beyond HGMF_COMPATIBLE_PHYSICAL_CANDIDATE.

## Gate F — external prediction

Freeze at least one quantitative prediction not used to choose potentials, kernel, gamma or carrier map.

## Gate G — authorized outcomes

- PASS_CONFIRMATORY_LOSS_CONTRACT
- PASS_NUISANCE_CLOSURE_CONTRACT
- PASS_THIRD_CARRIER_ESCALATION_RULE
- FAIL_KERNEL_MARGIN_IDENTIFIABILITY
- FAIL_STANDARD_RESPONSE_EXCLUSION
- HOLD_PHYSICAL_PROTOGEOMETRY

# HGMF‑HG24 — Contrato de co-localización causal–geométrica

A claim `COLOCATED_TRIAXIAL_INTERACTION` requires all of the following, frozen before holdout:

1. a do-interventional interaction contrast independent of the geometric source;
2. a nondegenerate normalized source `s_D`;
3. a frozen response kernel;
4. one training-only amplitude calibration;
5. held-out agreement of signs and extrema;
6. held-out nodal distance below the preregistered tolerance;
7. held-out relative residual below the preregistered tolerance;
8. order-sensitive contrasts reported separately;
9. transport to a second carrier without refitting the kernel;
10. failure of the frozen standard-response nuisance class.

Authorized outputs:

```text
GEOMETRIC_TRANSVERSALITY_ONLY
CAUSAL_INTERACTION_ONLY
COLOCATED_TRIAXIAL_INTERACTION
NEITHER
ORDER_DEPENDENT_INTERACTION
ABSTAIN_CAUSAL_IDENTIFICATION
ABSTAIN_CARRIER_TRANSFER
```

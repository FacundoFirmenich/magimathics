# HGMF‑HG28 — Diseño de orden causal, gatekeeping multicomponente y decisión confirmatoria

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** CAUSAL ORDER / DIRECTIONAL REPLICABILITY / MULTIPLICITY / CONFIRMATORY CLAIMS

## Veredicto

~~~text
PASS_SPARSE_ORDER_SUBDESIGN
PASS_ORDER_EFFECT_IDENTIFIABILITY_CONDITIONAL
PASS_DIRECTIONAL_2OF2_REPLICABILITY
PASS_14-CLAIM_HOLM_GATEKEEPING
PASS_ANTIAGGREGATIVE_COMPONENTWISE_CONFIRMATION
PASS_TRANSCARRIER_REPLICATION_RULE
PASS_CONFIRMATORY_CLAIM_LATTICE

FAIL_ORDER_EFFECT_FROM_BASE_GRID_ALONE
FAIL_UNADJUSTED_COMPONENT_SELECTION
FAIL_META-ANALYTIC_SUBSTITUTION_FOR_REPLICATION
FAIL_PHYSICAL_PROTOGEOMETRY_CLAIM_FROM_TWO_CARRIERS

ABSTAIN_NUMERIC_ORDER_POWER
ABSTAIN_EMPIRICAL_CONFIRMATION
HOLD_PHYSICAL_PROTOGEOMETRY
~~~

## Core results

1. The base \(3\times8\times3\) grids identify symmetric factorial interaction but not intervention order.
2. A sparse outcome-blind order module selects both lateral edges and three history bands: early \(1\to2\), middle \(4\to5\), late \(7\to8\).
3. This gives \(6\) order contexts per wave and carrier. Two reversed paths per context give:
\[
6\times3\times2=36
\]
sequence blocks per carrier, \(72\) across two carriers.
4. For component \(j\) and causal type \(t\in\{sym,ord\}\):
\[
p^+_{tj}=\max(p^+_{M,tj},p^+_{A,tj}),\qquad
p^-_{tj}=\max(p^-_{M,tj},p^-_{A,tj}),
\]
\[
p^{rep}_{tj}=\min\{1,2\min(p^+_{tj},p^-_{tj})\}.
\]
5. The \(14\) replicated causal p-values are tested together by Holm at familywise \(\alpha=0.05\).
6. No scalar average over \((A,B,C,K,E,Q,Z)\) is used for confirmation.
7. Modal, nodal, kernel and nuisance gates are nested validation requirements: they may narrow a causal claim but cannot manufacture one.
8. The strongest claim authorized by two carriers is CANDIDATE_NONSTANDARD_CROSS_CARRIER_RESPONSE, not physical protogeometry.

## Structural budget

- base dual-carrier grid: 144 acquisition units;
- sparse order module: 72 ordered sequence blocks;
- combined structural programme: 216 units/blocks;
- order-module training: 48;
- order-module holdout: 24.

## Next gate

HGMF‑HG29 — Confirmatory loss functions, nuisance closure and third-carrier escalation.

# HGMF‑HG07 — Event Geometry, Coarse‑Graining and Chance Semantics

**Verdict:** `PASS_BORN_WEIGHT_FORM_CONDITIONAL / FAIL_CHANCE_SEMANTICS / HOLD_FULL_BORN_DERIVATION`.

## Core result

Conditional on HG05–HG06 — quadratic Hilbert geometry, a complex amplitude module and sharp self-adjoint filters — the event weight

\[
q_\psi(P)=\frac{\|P\psi\|^2}{\|\psi\|^2}
=\operatorname{Tr}(\rho_\psi P)
\]

is normalized, representation-noncontextual for the same physical event and additive over mutually orthogonal coarse-grainings.

The additivity is not introduced as a probability axiom. It follows from Pythagoras:

\[
\left\|\sum_iP_i\psi\right\|^2=\sum_i\|P_i\psi\|^2,
\qquad P_iP_j=0.
\]

Coherent amplitude addition remains nonadditive because of the interference cross term.

## Exact boundaries

\[
q_\psi(P)=1\iff P\psi=\psi,
\qquad
q_\psi(P)=0\iff P\psi=0.
\]

For repeated product preparations, the quadratic weight of exactly `k` occurrences is binomial and concentrates exponentially near `q`. This is a theorem of weight-typicality, not a derivation of single-case objective chance.

The same mathematical weight is compatible with chance, branch typicality, decision weight and propensity. Event geometry does not select among those semantics.

```text
PASS_EVENT_GEOMETRY
PASS_ORTHOGONAL_WEIGHT_ADDITIVITY
PASS_NONCONTEXTUAL_TRACE_WEIGHT_CONDITIONAL
PASS_BORN_FUNCTIONAL_FORM_CONDITIONAL
PASS_FREQUENCY_WEIGHT_CONCENTRATION

FAIL_SINGLE_CASE_CHANCE_SEMANTICS
HOLD_FULL_BORN_DERIVATION
```

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `BORN_WEIGHT_FORM_CONDITIONAL_PASS / CHANCE_SEMANTICS_HOLD`.

## Next gate

`HGMF‑HG08 — Quadratic Weight, Frequency Typicality and Single‑Case Chance`.

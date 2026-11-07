# HGMF‑UMI‑15 — Orthogonal History‑State Constitutive Law

**Verdict:** `PASS_PARTIAL_VECTOR_HISTORY_LAW / HOLD_FULL_CONSTITUTIVE_LAW`

## Result

The operational magnetic history-state cannot be represented by one scalar. The audited state is

\[
\mathbf s_t=(A_t,B_t,C_t,K_t,E_t,Q_t,Z_t),
\]

with response span, signed HEB, coercive width, switching-completeness gate, normalized loop area, empirical q95 noise, and a fresh/trained/incomplete flag.

Four matched empirical contrast directions — completed-loop history, preset sign, field-plus-history, and sample/context — are linearly independent in the declared observable map (`rank = 4`). This is an observable-rank result, not an ontological state-dimension claim.

## Fixed-control training

Five consecutive loops at `|H|max = 200.064398 mT` show a discrete fresh→trained transition. The first loop lies outside the trained cycle-2–5 envelope in span, HEB, coercive width and loop area. HEB, coercivity and area undergo a fast first-cycle reset; span retains a slower or unresolved evolution.

## Reset-sign contrast

At identical field amplitude, PF+ and PF− differ in span by only `0.308%`, while HEB is nearly antisymmetric: the signed residual is `0.863128 mT` (`2.796%` relative). Five of five valid labelled first-loop histories preserve the opposite-sign preset/HEB relation. Magnitude does not transfer sharply.

## Future-only test

Cycles 2–4 define the trained-state set before observing cycle 5. HEB, coercive width and q95 noise are covered; span and loop area are not.

- `PASS_FAST_COMPONENT_SET_FORECAST`
- `FAIL_FULL_VECTOR_FORECAST`

## Scientific boundary

The gate supports a piecewise causal law with a discrete fresh→trained state transition. It does not identify a universal continuous constitutive map because field and history remain incompletely orthogonalized and independent factorial replications are absent.

No novelty is claimed for exchange-bias training, Paccard relaxation or Binek's recurrence. Their independent reconstruction remains part of the internally closed programme and is reused in the UMI vector-state architecture.

## Next gate

`HGMF‑UMI‑16 — Counterbalanced Reset × Field × Cycle`: same device, preset signs `+/-/0`, three field amplitudes, five cycles, randomized field order, explicit resets, and at least three independent replications per cell.

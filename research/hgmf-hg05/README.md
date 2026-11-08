# HGMF‑HG05 — Amplitude Geometry and Quadratic Weight Tribunal

**Verdict:** `PASS_P_NORM_FAMILY / PASS_QUADRATIC_WEIGHT_SELECTION_CONDITIONAL / FAIL_AMPLITUDE_DERIVATION / FAIL_NONCIRCULAR_BORN_SELECTION`.

## Core result

A continuous, phase-invariant, nontrivial scalar weight that is multiplicative under composition has the form

\[
w(z)=|z|^p,\qquad p>0.
\]

Composition alone leaves `p` free.

For the balanced linear mixer

\[
B=a\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\]

reversibility `B^2 = I` up to global phase fixes `|a|=1/sqrt(2)`. Preserving the separable `p`-weight of a basis state then gives

\[
2|a|^p=2^{1-p/2}=1,
\]

hence

\[
\boxed{p=2}.
\]

The coefficient `1/sqrt(2)` follows from involution, not from assuming the 2-norm. The existence of a linear balanced reversible mixer is an additional physical axiom.

## Hilbert geometry

The selected norm satisfies the parallelogram law, and Jordan–von Neumann recovers an inner product. This selects Hilbert geometry conditionally, but does not select the scalar field `R`, `C` or `H`.

## Born boundary

HG05 derives a quadratic conserved amplitude weight, not a probability law. Outcome geometry, orthogonal additivity, normalization as chance, noncontextuality and empirical probability semantics remain un-derived. The 2026 analysis by Zhang confirms that additivity is indispensable in the main Born-rule derivation families.

```text
QUADRATIC AMPLITUDE GEOMETRY = PASS CONDITIONAL
COMPLEX FIELD = HOLD
BORN PROBABILITY = HOLD
```

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `QUADRATIC_AMPLITUDE_GEOMETRY_CONDITIONAL_PASS / BORN_HOLD`.

## Next gate

`HGMF‑HG06 — Operational Superposition and Scalar‑Field Selection`.

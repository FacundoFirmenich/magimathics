# HGMF‑UMI‑18 — Representation-Independent UMI Characterization

**Verdict:** `PASS_UMI_CHARACTERIZATION_THEOREM / PASS_GRADED_APPROXIMATION / FAIL_MINIMALITY_UNIQUENESS`

## Canonical result

A UMI is not a privileged carrier. Relative to a declared jurisdiction \(\mathcal J\), it is the semantic equivalence class

\[
\operatorname{UMI}_{\mathcal J}(\sigma)=\{S:\Sigma_{\mathcal J}(S)=\sigma\}.
\]

The complete signature contains enabled and forbidden realizations, intervention/history response and closure status, after quotienting only by admissible representation transports.

Exact identity

\[
S\equiv_{\mathcal J}T \iff \Sigma_{\mathcal J}(S)=\Sigma_{\mathcal J}(T)
\]

is reflexive, symmetric and transitive. Directed exact refinement is a preorder; mutual refinement is an equivalence. Fixed-\(\varepsilon\) similarity is not transitive in general, so approximate transport must be represented by a grainwise vector pseudometric or an accumulated loss budget.

## Minimality

Minimality belongs to realizations, not to UMI identity. Four distinct notions are frozen:

1. inclusion minimality;
2. causal minimality;
3. representational minimality;
4. scale-relative atomicity.

The minimal core is generally an antichain of non-isomorphic carriers, not a unique carrier. The exact counterexample contains minimal realizations \(\{a\}\) and \(\{b,c\}\) of the same signature.

## Composition

UMI equivalence is a congruence only when the semantic map is compositional and later contexts respect the declared interface. A context that exposes a hidden channel can distinguish systems that were equivalent in the original jurisdiction.

## Antiaggregation theorem

A summary \(A\) is semantically sufficient exactly when

\[
\ker A\subseteq\equiv_{\mathcal J}.
\]

It is canonical exactly when

\[
\ker A=\equiv_{\mathcal J}.
\]

The mean and pooled global average fail in general: equal means can hide different support, tails, forbidden outcomes and grain structure.

## Separating counterexamples

The exact checker verifies:

- same carrier, different UMI;
- different carriers, same UMI;
- same operator, different semantics;
- same semantics, different operators;
- non-transitive fixed-tolerance similarity;
- non-unique minimal realizations;
- mean collision;
- composition failure through an undeclared hidden channel.

## Status of the dual acronym

- `Unidad Mínima Invariante`: formally characterized.
- `Unidad Multifractal de Interrelación`: pending a scale-indexed semantic measure and a transport-stable multifractal spectrum.

## Next gate

`HGMF‑UMI‑19 — Scale-Indexed Semantic Measure and Multifractal Interrelation`.

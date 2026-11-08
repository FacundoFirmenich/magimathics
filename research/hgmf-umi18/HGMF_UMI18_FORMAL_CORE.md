# HGMF‑UMI‑18 — Formal Core

## Jurisdiction

\[
\mathcal J=(\mathcal E,\mathcal G,\mathcal Y,\mathfrak T,\mathfrak C,\mathbf d,\boldsymbol\varepsilon,\mathfrak R).
\]

It declares experiments and histories, grains, observation spaces, admissible representation transports, composition contexts, grainwise distances, loss budgets and allowed reductions.

## Semantic behavior object

For a system \(S\) and experiment \(e\):

\[
b_S(e)=(A_S(e),F_S(e),R_S(e),\kappa_S(e)),
\]

with enabled realizations, forbidden realizations, intervention/history response and closure/completeness.

## Transported signature

\[
\Sigma_{\mathcal J}(S)=\left([b_S(e)]_{\mathfrak T_e}\right)_{e\in\mathcal E}.
\]

## Exact UMI identity

\[
S\equiv_{\mathcal J}T\iff\Sigma_{\mathcal J}(S)=\Sigma_{\mathcal J}(T).
\]

This is an equivalence relation.

## UMI class and minimal core

\[
\operatorname{UMI}_{\mathcal J}(\sigma)=\Sigma_{\mathcal J}^{-1}(\{\sigma\}),
\]

\[
\operatorname{Core}_{\mathcal J}(\sigma)=\operatorname{Min}_{\trianglelefteq_{\mathcal J}}\operatorname{UMI}_{\mathcal J}(\sigma).
\]

The class is the unit; systems realize it. The core is generally a non-unique antichain.

## Exact theorems

1. **Finite existence:** every nonempty finite realization fiber has at least one minimal realization.
2. **Uniqueness:** a unique minimum exists iff the fiber contains a least element under the declared reduction, modulo carrier isomorphism.
3. **Approximation:** a grainwise pseudometric vector has exact UMI identity as its zero fiber. Fixed positive tolerance is not transitive in general.
4. **Composition:** if \(\Sigma(S\circ T)=\Sigma(S)\star\Sigma(T)\), exact UMI identity is a congruence.
5. **Antiaggregation:** a summary \(A\) avoids false semantic mergers iff \(\ker A\subseteq\equiv_{\mathcal J}\); it is canonical iff equality holds.

## Minimality taxonomy

- inclusion;
- causal;
- representational;
- scale-relative atomicity.

These are not generally equivalent.

## Exact negative results

- fixed-\(\varepsilon\) approximate identity is not transitive;
- minimal realization is not unique in general;
- composition fails if later contexts expose undeclared hidden channels;
- means and pooled global averages are not sufficient invariants in general.

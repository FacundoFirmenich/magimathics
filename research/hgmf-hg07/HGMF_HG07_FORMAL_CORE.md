# HGMF‑HG07 — Formal Core

## Sharp events

Let `H` be the conditional complex Hilbert amplitude space from HG05–HG06. A sharp event is an orthogonal projector

\[
P=P^2=P^\dagger.
\]

Mutually exclusive events satisfy `P_i P_j = 0`; their coarse-graining is `sum_i P_i`.

## Quadratic event weight

\[
q_\psi(P)=\frac{\|P\psi\|^2}{\|\psi\|^2}.
\]

For pairwise orthogonal projectors,

\[
q_\psi\!\left(\sum_iP_i\right)=\sum_iq_\psi(P_i).
\]

This is Pythagorean additivity, not a probabilistic postulate.

## Coherent alternatives

\[
\|u+v\|^2=\|u\|^2+\|v\|^2+2\operatorname{Re}\langle u,v\rangle.
\]

Amplitude addition and event union are distinct operations. Additivity applies only after exclusivity/orthogonality has been established.

## Trace form and certainty

For

\[
\rho_\psi=|\psi\rangle\langle\psi|/\langle\psi|\psi\rangle,
\]

\[
q_\psi(P)=\operatorname{Tr}(\rho_\psi P).
\]

Moreover,

\[
q_\psi(P)=1\iff P\psi=\psi,
\qquad
q_\psi(P)=0\iff P\psi=0.
\]

## Repeated products

For a binary event of weight `q`, the `N`-copy sector with `k` occurrences has weight

\[
W_N(k)=\binom Nk q^k(1-q)^{N-k}.
\]

Its mass outside a frequency window obeys a Hoeffding-type exponential bound.

## Boundary

The construction yields a normalized additive mathematical event measure and the conditional Born functional form. It does not determine whether the weight is objective chance, branch typicality, decision weight or propensity.

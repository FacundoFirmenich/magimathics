# HGMF‑HG01 — Formal Core

## 1. Founding order

\[
\mathsf{PreGeom}\succ_{fund}\mathsf{ProtoGeom}\succ_{fund}\mathsf{Geom}.
\]

\(\succ_{fund}\) is strict explanatory dependence. No temporal symbol appears in the theory, so no chronological inequality follows.

## 2. Proto-code

An observer-side proto-code is

\[
P=(\mathcal R,\operatorname{cl}_P,\mathcal N_P,\mu_P,\Theta_P),
\]

with graded relational alphabet, closure operator, nested patches, optional semantic measure and realizability profile.

The closure satisfies extensivity, monotonicity and idempotence. Its fixed points form a complete lattice.

## 3. Projection and stabilization

\[
\Pi_\lambda:\mathcal P\rightharpoonup\mathcal Y_\lambda,
\qquad
S_\lambda:\mathcal Y_\lambda\to\mathcal G_\lambda,
\qquad
S_\lambda^2=S_\lambda,
\]

\[
\Phi_\lambda=S_\lambda\circ\Pi_\lambda.
\]

## 4. Fibre quotient theorem

\[
P\sim_\lambda P'\iff\Phi_\lambda(P)=\Phi_\lambda(P').
\]

Then the induced map

\[
\overline\Phi_\lambda:\mathcal P/\!\sim_\lambda\to\operatorname{im}\Phi_\lambda
\]

is bijective.

## 5. Invariant factorization theorem

A function \(I:\mathcal P\to X\) is geometrically recoverable exactly when it is constant on fibres of \(\Phi_\lambda\). Equivalently, there is a unique \(\overline I\) such that

\[
I=\overline I\circ\Phi_\lambda.
\]

## 6. Contextual realization

\[
\mathscr R(P)=\{(\lambda,\Phi_\lambda(P)):\lambda\in\Lambda\}.
\]

Different realizations under different contexts are compatible with one proto-code provided each lies in its admissible realization profile \(\Theta(P)\).

## 7. Hypergeometric grammar

\[
\mathfrak H=(\succ_{fund},\operatorname{cl},\Theta,\Lambda,\{\Phi_\lambda\},\{\sim_\lambda\},\operatorname{Inv}).
\]

This is a theory signature, not an ontological containing space.

## 8. Boundaries

- positive internal pregeometry: `HOLD`;
- physical projection dynamics: `HOLD`;
- special constants: excluded;
- multifractal proto-code: conditional subclass, not yet physically instantiated.

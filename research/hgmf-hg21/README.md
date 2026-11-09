# HGMF‑HG21 — Zero‑Flux Residual Fields, Hodge Modes and Nonlocal Coupling

**Verdict:** `PASS_ZERO_FLUX_RESIDUAL_BASIS / PASS_HODGE_RECONSTRUCTION / PASS_NONLOCAL_COUPLING_CLASS / PASS_HODGE_TRANSPORT_CONDITIONAL / FAIL_MODE_UNIQUENESS / FAIL_STANDARD_GEOMETRY_EXCLUSION`.

## Core theorem

On a closed connected oriented context surface,

\[
\delta\mathcal F=f\,dA_Q,\qquad \int_M f\,dA_Q=0
\]

is exact. With the positive Laplace–Beltrami operator \(\mathcal L=-\operatorname{div}\nabla\), there is a unique mean-zero potential

\[
\mathcal Lu=f,
\]

and a canonical coexact reconstruction

\[
\alpha_f=-*du,\qquad d\alpha_f=\delta\mathcal F.
\]

The full connection difference remains

\[
\alpha=d\chi-*du+h,
\]

where \(h\) is harmonic. Curvature does not identify flat harmonic holonomies.

## Modal basis

\[
f=\sum_{n\ge1}a_n\phi_n,\qquad
u=\sum_{n\ge1}\frac{a_n}{\lambda_n}\phi_n.
\]

The constant mode is excluded. The basis is complete, but the coefficients are not physically selected.

A fully isometry-invariant scalar residual on a homogeneous carrier is constant; zero mean then forces it to vanish. Any nonzero residual requires a source, axis, history, interaction or other symmetry-breaking datum.

## Composition

The additive object is the residual two-form:

\[
\delta\mathcal F_{AB}=\delta\mathcal F_A+\delta\mathcal F_B.
\]

Densities and modal coefficients do not add universally because the composite metric and Laplacian change. The exact torus witness has area densities `2,2,5` and creates a new spectral degeneracy.

## Nonlocal class

Every zero-mode-free spectral multiplier

\[
\mathcal K=\sum_{\lambda>0}\kappa(\lambda)\Pi_\lambda
\]

preserves zero flux. Green, screened, fractional and heat kernels produce different nodal structures. Hodge theory does not select \(\kappa\).

History kernels

\[
a_n(t)=\int_0^tk_n(t-s)b_n(s)ds
\]

can be realized by hidden Markovian states for exponential kernels, so memory/nonlocality is not HGMF-specific.

## Cross-carrier transport

An oriented QGT isometry transports \(dA\), Hodge star, Laplacian eigenspaces and the residual exactly. Inside degenerate eigenspaces only block projectors and block power are canonical. Spectrum equality without isometry is insufficient.

## Exact formal holdout

On the QGT sphere,

\[
f_*(x)=2P_1(x)+4P_2(x)+3P_3(x)
=\frac{(5x+4)(3x^2-1)}2.
\]

Three training points recover the coefficients exactly and predict the held-out nodes

\[
x=-4/5,\qquad x=\pm1/\sqrt3.
\]

This is an analytic future-only witness, not empirical evidence.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`; spectral-transport boundary added.
- Paper C: `ZERO-FLUX HODGE BASIS + NONLOCAL CLASS PASS; PHYSICAL MODE/KERNEL SELECTION FAIL/HOLD`.

## Next gate

`HGMF‑HG22 — Relational Source, Modal Selection and Cross‑Carrier Nodal Falsifiers`.

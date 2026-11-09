# HGMF‑HG21 — Formal Core

## Exact zero-flux theorem

Let \(M\) be a closed connected oriented Riemannian surface. For \(\omega=f\,dA\):

\[
\omega\text{ exact}\iff\int_M\omega=0.
\]

With \(\mathcal L=-\operatorname{div}\nabla\ge0\), every zero-mean \(f\) has a unique mean-zero solution \(u\) of

\[
\mathcal Lu=f.
\]

Then

\[
\alpha_f=-*du,\qquad d\alpha_f=f\,dA.
\]

Every connection difference with this curvature is

\[
\alpha=d\chi-*du+h,
\]

with \(h\) harmonic.

## Spectral representation

For

\[
\mathcal L\phi_n=\lambda_n\phi_n,
\qquad 0=\lambda_0<\lambda_1\le\cdots,
\]

zero flux removes the constant mode:

\[
f=\sum_{n\ge1}a_n\phi_n.
\]

The reconstruction is

\[
u=\sum_{n\ge1}\frac{a_n}{\lambda_n}\phi_n,
\qquad
\alpha_f=-\sum_{n\ge1}\frac{a_n}{\lambda_n}*d\phi_n.
\]

Norm identities:

\[
\|f\|_2^2=\sum_{n\ge1}|a_n|^2,
\qquad
\|\alpha_f\|_2^2=\sum_{n\ge1}\frac{|a_n|^2}{\lambda_n}.
\]

## Harmonic sector

For genus \(g\):

\[
\dim\mathcal H^1(M)=2g.
\]

This flat sector changes noncontractible-cycle holonomies without changing curvature.

## Boundary exception

If \(\partial M\neq\varnothing\):

\[
\int_Md\alpha=\oint_{\partial M}\alpha.
\]

Zero total flux is not required without a boundary-circulation condition.

## Symmetry no-go

A scalar invariant under a transitive isometry group is constant. Combined with zero mean, this forces the residual to vanish. Nonzero fields require symmetry-breaking data.

## Composition

The natural additive object is

\[
\delta\mathcal F_{AB}=\delta\mathcal F_A+\delta\mathcal F_B.
\]

Relative to the composite area:

\[
f_{AB}=
\frac{f_A\sqrt{\det g_A}+f_B\sqrt{\det g_B}}
{\sqrt{\det(g_A+g_B)}}.
\]

Mode coefficients must be recomputed with the composite Laplacian.

## Nonlocal response

A Laplace-equivariant zero-mode-free response has the form

\[
\mathcal K=\sum_{\lambda>0}\kappa(\lambda)\Pi_\lambda.
\]

Its bilocal kernel is

\[
K(x,y)=\sum_{n\ge1}\kappa(\lambda_n)\phi_n(x)\phi_n(y).
\]

History dependence is

\[
a_n(t)=\int_0^tk_n(t-s)b_n(s)ds.
\]

Neither \(\kappa\) nor \(k_n\) is selected by the current axioms.

## Cross-carrier theorem

An orientation-preserving isometry \(\varphi:M_1\to M_2\) intertwines \(d\), Hodge star and Laplace–Beltrami operators. It transports the Hodge reconstruction exactly. In degenerate eigenspaces, block power

\[
P_\lambda(f)=\|\Pi_\lambda f\|_2^2
\]

is canonical, while individual basis coefficients are not.

## Claim boundary

Hodge theory supplies a complete admissible basis and a canonical reconstruction, not a physical source, a unique mode, a unique nonlocal kernel or a proto-geometric correction.

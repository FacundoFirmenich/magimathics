# HGMF‑UMI‑19 — Formal Core

## Semantic witness space

\[
\Omega_{\mathcal J}=\Omega_V\sqcup\Omega_H\sqcup\Omega_D\sqcup\Omega_J.
\]

A nonnegative witness valuation depends only on the UMI‑18 semantic signature:

\[
c_S(\omega)=v_\omega(\Sigma_{\mathcal J}(S))\ge0.
\]

The semantic measure is

\[
\mu_S(A)=\int_A c_S(\omega)d\nu(\omega).
\]

## Scale-indexed covers

For nested, predeclared covers \(\mathcal G_n\) with \(\ell_n\to0\):

\[
Z(q,n)=\sum_{B\in\mathcal G_n}p_B(n)^q,
\]

\[
\tau(q)=\lim_{n\to\infty}\frac{\log Z(q,n)}{\log\ell_n},
\qquad
D_q=\frac{\tau(q)}{q-1}.
\]

## Scale-rich multifractal UMI

A UMI class is scale-rich multifractal only if:

1. measure and covers are fixed ex ante;
2. \(\tau(q)\) exists on a nondegenerate interval;
3. \(\tau(q)\) is non-affine;
4. the spectrum survives compatible transports;
5. width does not collapse under finite-size scaling;
6. finite mixtures, broad marginals, heteroscedasticity and regime changes are rejected as sole explanations.

## Spectral transport theorem

If \(\phi_*\mu_S=\mu_T\), \(\phi(\mathcal G_n^S)=\mathcal G_n^T\), and triaxial typing is preserved, then

\[
Z_S=Z_T,\quad \tau_S=\tau_T,\quad D_q^S=D_q^T,\quad f_S=f_T.
\]

Preserving only total mass, a terminal mass multiset or a global mean is insufficient.

## Triaxial coupling

Marginal measures \(\mu_V,\mu_H,\mu_D\) are compared with the joint measure through

\[
\Xi(q)=\tau_{\otimes}(q)-\tau_{\rm joint}(q).
\]

This is an operational coupling spectrum, not a claim of unique PID decomposition.

## Dual-acronym theorem

Let \(\mathfrak U_{MI}\) be minimal invariant UMI classes and \(\mathfrak U_{MF}\) be transport-stable scale-rich multifractal classes. Then

\[
\mathfrak U_{dual}=\mathfrak U_{MI}\cap\mathfrak U_{MF}.
\]

Neither class contains the other in general.

## Exact no-go results

- uniform minimal carrier: minimal invariant but monofractal;
- redundant binomial cascade: multifractal but non-minimal;
- finite mixture: finite spectrum and piecewise-affine asymptotic \(\tau\);
- same finest-scale masses, different hierarchy: different intermediate-scale spectra;
- uniform V/H/D marginals, multifractal joint distribution.

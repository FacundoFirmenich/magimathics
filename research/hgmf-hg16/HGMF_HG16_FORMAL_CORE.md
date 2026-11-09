# HGMF‑HG16 — Formal Core

## Nuisance quotient

Let `O` be the space of observable multi-gap, multi-clock and multi-context processes, and `N_std` the preregistered class of standard nuisances. The attributable object is

\[
[\mathcal D]\in\mathfrak O/\mathfrak N_{std}.
\]

## Standard-absorption theorem

A CPTP correction admits a Stinespring dilation. A causal finite-time process tensor admits a pure-state/isometric/unitary-circuit realization. Therefore a reduced anomaly, dephasing pattern, memory kernel or order effect is not uniquely proto-geometric.

## Multi-gap dimension theorem

For `d` equispaced levels, the number of complex coherences is `d(d-1)/2`; scalar-time smearing has only `d-1` distinct positive-gap values. Hence

\[
N_{res}=\binom{d-1}{2}.
\]

A qutrit is minimal.

## Diagnostics

\[
J_{gap}^2=\frac1{\binom d2}\sum_{k=1}^{d-1}\sum_{m=0}^{d-k-1}|C_{m,m+k}-\bar C_k|^2.
\]

For a Schur dephasing channel:

\[
J_{CP}=\sum_{\lambda_i(C)<0}|\lambda_i(C)|.
\]

For a QRF cycle:

\[
\Omega_{abc}=T_{a\leftarrow c}T_{c\leftarrow b}T_{b\leftarrow a},
\qquad
J_{QRF}=D_{gen}(\Omega_{abc},id).
\]

For matched-endpoint order protocols:

\[
J_{order}=D_{gen}(\mathcal T[AB],\mathcal T[BA]).
\]

## Attribution condition

A candidate requires

\[
J_{std}>0,\quad J_{CP}=0,\quad J_{QRF}\le\epsilon_{QRF},\quad J_{scale}\le\epsilon_{scale},
\]

plus cross-carrier transport and future-only validation.

## Scale no-go

The current programme contains no derived dimensionful `E_HG`, `tau_HG`, `ell_HG` or coupling. Symmetry and the standard limit allow infinitely many correction functions. The diagnostic basis is closed; the physical correction is not.

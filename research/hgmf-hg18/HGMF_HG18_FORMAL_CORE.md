# HGMF‑HG18 — Formal Core

## Pure-state context geometry

For an oriented regular map

\[
\lambda\mapsto[\psi(\lambda)]\in\mathbb P(\mathcal H),
\]

define

\[
Q_{ij}=\langle\partial_i\psi|(I-|\psi\rangle\langle\psi|)|\partial_j\psi\rangle,
\quad
g_{ij}=\operatorname{Re}Q_{ij},
\quad
\mathcal F_{ij}=2\operatorname{Im}Q_{ij}.
\]

If `rank g=2`, the quantum distinguishability area is

\[
dA_Q=\sqrt{\det g}\,d\lambda^1\wedge d\lambda^2.
\]

The normalized curvature density

\[
\chi_Q=\frac{\mathcal F_{12}}{2\sqrt{\det g}}
\]

obeys `|chi_Q|<=1` because the QGT is positive semidefinite.

## Small-loop theorem

On an Abelian patch:

\[
\operatorname{Hol}(\partial\Sigma)=\exp\left(i\int_\Sigma\mathcal F\right),
\]

and locally

\[
\arg\operatorname{Hol}=2\chi_Q A_Q+o(A_Q).
\]

## Global quantization

\[
C_1=\frac{1}{2\pi}\int\mathcal F\in\mathbb Z.
\]

Chern quantization fixes dimensionless total flux, not a dimensionful scale.

## Strong cross-carrier transport

If

\[
|\psi_2(\varphi(\lambda))\rangle=e^{i\alpha(\lambda)}V|\psi_1(\lambda)\rangle
\]

with `varphi` an oriented diffeomorphism and `V` a constant isometry, then

\[
\varphi^*Q_2=Q_1.
\]

QGT, area, normalized density, holonomy and Chern number are transported exactly.

Coarse semantic/UMI equivalence does not imply this. A parameter-dependent hidden ancilla preserves system-level outcomes while changing the total QGT.

## Dimensional no-go

Under `x=a λ1`, `y=b λ2`:

\[
\mathcal F_{xy}=\mathcal F_{12}/(ab),
\qquad
\sqrt{\det g_{xy}}=\sqrt{\det g}/|ab|,
\]

so `chi_Q` is invariant. QGT area is dimensionless. A dimensionful curvature density requires an independently calibrated physical area form and coupling.

## Mixed-state boundary

Monotonicity under channels permits a Petz family of mixed-state metrics. Bures/SLD is distinguished but not uniquely selected by the present HGMF axioms.

## Standard-QM boundary

QGT, Berry curvature, Chern number, quantum volume and their direct experimental measurement are standard quantum geometry. None alone distinguishes physical protogeometry.

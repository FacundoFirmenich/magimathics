# HGMF‑HG41 — Formal core

## 1. Labelled affine quotient chart

Let y=(y1,...,ym) be labelled observations and choose distinct anchors r,s. On the nondegenerate stratum ys != yr, define

rho_i = (y_i-y_r)/(y_s-y_r),  i not in {r,s}.

Set u=y_r and v=y_s-y_r. The inverse chart is

y_r=u,  y_s=u+v,  y_i=u+v rho_i.

The absolute Jacobian is

|det d y / d(u,v,rho)| = |v|^(m-2).

The anchor-degenerate stratum v=0 must be represented separately or rejected fail-closed.

## 2. Quotient pushforward density

If f(y) is a proper density on the labelled observation space, the quotient density in chart (r,s) is

q_rs(rho) = integral integral f(T_rs(u,v,rho)) |v|^(m-2) dv du,

with v integrated over the physical orientation domain. Normalization follows by change of variables.

## 3. Chart covariance

Changing anchors produces a fractional affine coordinate transformation. A density must transform with the chart-transition Jacobian. Therefore a naive Gaussian directly assigned to rho is not anchor-neutral. Anchors and orientation must be frozen before outcomes, or transition Jacobians must be included.

## 4. Quotient universal e-value theorem

Let T be a measurable quotient map and Q_P=P o T^{-1} the induced law under each original-space null P. Suppose every Q_P has density q_P with respect to one quotient measure mu_Q. Let g_T be a proper training-only quotient density and

U_0(z) >= sup_{P in H0} q_P(z).

Then

E_Q(z)=g_T(z)/U_0(z)

on U_0>0, and zero otherwise, satisfies

E_P[E_Q(T(Y))] <= 1

for every P in H0.

## 5. Support-only pointwise ceiling theorem

Let F be the quotient observations compatible with a null under the available bounded-error authority. If the null contains every point mass delta_z for z in F, every valid e-variable obeys

E(z) <= 1 for every z in F.

Proof: validity under delta_z gives E_delta_z[E]=E(z)<=1.

Thus a feasible historical observation cannot reach the carrier threshold 140 under support-only authority.

## 6. Magnetic consequence

The one-shot trained-state null is feasible iff the intervals [h_i-Delta_i,h_i+Delta_i], i=2,...,5, have nonempty intersection.

For the historical FGT/CrSBr summaries, the common interval is

[-0.9549680763, 0.2177953130] mT.

Hence the equal-trained-state source null is exactly support-compatible, and its quotient point (1,1,1) lies in the feasible set. Without a stochastic law for residual field discretization, every valid quotient e-value at the historical observation is bounded by one.

## 7. Adsorption consequence

HG40 evaluated 713 pairwise no-passing comparisons. Fifty-one raw point differences were negative, but zero exceeded the conservative last-digit-plus-rounding envelope. Each local comparison therefore intersects the no-passing order cone.

The artifact does not define a joint stochastic law for correlated interpolation nodes. Treating the 713 nodes as independent Bernoulli or Gaussian observations would manufacture authority absent from the source.

## 8. Claim boundary

HG41 establishes the quotient measure, its Jacobian, the finite-sample quotient e-value theorem and the support-only no-go. It does not establish model-specific quotient densities, a historical confirmatory e-value, exclusion of carrier-standard physics or physical protogeometry.

# HGMF‑HG30 — Núcleo formal

## 1. Covariance receipt

Para estimates \(y\in\mathbb R^n\), la incertidumbre es una entidad versionada:

\[
R_\Sigma=(\ell,u,\Sigma,r,\tau,\mathcal A,\mathcal P).
\]

Admisibilidad:

\[
\Sigma=\Sigma^\top,
\qquad
\lambda_{\min}(\Sigma)\ge-\tau.
\]

Si la covariance es singular, sólo se permiten contrasts en su support.

## 2. Transformación

Para transformación lineal congelada \(A\):

\[
y'=Ay,
\qquad
\Sigma'=A\Sigma A^\top.
\]

Todo rectangle/modal transform genera un derivation receipt y conserva ancestry.

## 3. Predictive receipt

Un nuisance adapter produce una entidad que fija family id, training fit, complexity cap, holdout scope, predictive object, discrepancy y calibration authority.

## 4. Calibration authority

HG30 distingue:

- EXACT_FINITE_SAMPLE;
- EXACT_CONDITIONAL_RANDOMIZATION;
- ASYMPTOTIC_THEOREM;
- EMPIRICAL_CALIBRATION_ONLY;
- UNPROVEN.

Una implementación no adquiere autoridad confirmatoria por existir.

## 5. Monte Carlo resolution

Para

\[
p_{MC}=\frac{1+\#\{T_b\ge T_{obs}\}}{B+1},
\]

el menor valor es \(1/(B+1)\). Para cruzar \(\alpha_j=1/140\), es necesario:

\[
\boxed{B\ge139.}
\]

Esto es resolución discreta, no prueba de family-level calibration.

## 6. Drift/control

En Gaussian linear prediction:

\[
y_T=X_T\beta+\varepsilon_T,
\qquad
y_H=X_H\beta+\varepsilon_H.
\]

Con OLS training:

\[
e_H=y_H-X_H\hat\beta,
\]

\[
V_H=I+X_H(X_T^\top X_T)^{-1}X_H^\top.
\]

Si \(m=|H|\) y \(\nu=n_T-p\):

\[
\boxed{
F=
\frac{e_H^\top V_H^{-1}e_H}{m\,s_T^2}
\sim F_{m,\nu}
}
\]

exactamente bajo los supuestos Gaussianos homoscedásticos.

## 7. Complejidad

Toda nuisance compleja debe declarar límites antes de holdout:

- hidden-state: number of states and emission family;
- process tensor: memory length, local dimension, bond/compression cap and tomography algorithm;
- kernel: candidate family and parameter range;
- ancilla/control geometry: latent dimension/rank and map family.

Una clase sin cap queda ABSTAIN_UNBOUNDED_NUISANCE_MODEL.

## 8. Frontera

HG30 implementa interfaces y algunos engines. No concede calibración family-level a HMM, PT-MPO o ancilla sólo porque generen predictive distributions.

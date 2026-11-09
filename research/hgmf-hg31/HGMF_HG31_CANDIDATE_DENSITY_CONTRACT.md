# HGMF‑HG31 — Contrato de densidad candidata

El numerator universal \(g_T(H)\) debe ser una densidad propia, normalizada y congelada con training.

Puede ser:

- Gaussian predictive density sobre components;
- discrete predictive mass sobre raw outcomes;
- mixture de densities training-frozen;
- otra density normalizada con observation measure explícita.

No puede ser:

- un score no normalizado;
- RMSE convertido a likelihood sin modelo;
- likelihood ajustada con wave 3;
- best-of-many candidate seleccionado con holdout.

## Gaussian candidate

Para mean \(\mu_T\) y covariance predictiva positiva definida \(\Sigma_T\):

\[
g_T(y)
=
\mathcal N(y;\mu_T,\Sigma_T).
\]

La covariance puede incluir measurement uncertainty y parameter uncertainty siempre que quede congelada antes del holdout.

## Potencia

Una candidate density pobre no invalida el e-value; simplemente reduce \(E_X\). Esto separa validez de potencia.

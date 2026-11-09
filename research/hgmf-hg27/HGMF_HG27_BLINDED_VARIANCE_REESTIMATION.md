# HGMF‑HG27 — Reestimación ciega de varianza

HG27 autoriza un único look de precisión después de que ambos carriers completen wave 1.

Puede usar:

- standard errors de extracción;
- residual noise del raw trace;
- calibration drift;
- pooled nuisance variance;
- missingness y quarantine rates.

No puede usar signos de rectángulos, contrastes de celda, nodos, kernel comparisons, transfer scores ni wave 3.

Para half-width objetivo:

\[
W_{req,j}=\left\lceil(2z_{1-\alpha_j/2}\widehat\sigma_j/h_j)^2\right\rceil.
\]

Para potencia sobre \(\Delta_j^\star\):

\[
W_{req,j}=\left\lceil[2(z_{1-\alpha_j/2}+z_{1-\beta_j})\widehat\sigma_j/\Delta_j^\star]^2\right\rceil.
\]

La expansión sólo puede aumentar training y está limitada por \(W_{max}\). Wave 3 permanece intacta.

No existe expansión numérica autorizada mientras no se preregistren \(h_j\), \(\Delta_j^\star\), multiplicity rule y \(W_{max}\).

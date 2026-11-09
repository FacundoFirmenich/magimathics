# HGMF‑HG20 — Selección del acoplamiento adimensional y tribunal residual transcarrier

## Objetivo

Determinar si el coeficiente residual

\[
c_{\rm HG}
=\hbar^2
\frac{\delta\mathcal F}{dA_{\rm act}}
\]

puede quedar seleccionado sin ajuste retrospectivo.

## Gate A — residual estándar

Definir

\[
\delta\mathcal F
=\mathcal F_{\rm obs}-\mathcal F_{\rm std}
\]

tras congelar QGT, Bures, clocks, ancillas, controles y process tensors estándar.

## Gate B — composición

Auditar cómo \(c_{\rm HG}\) transforma bajo productos, coarse-graining y sistemas compuestos.

## Gate C — orientación y cuantización

Determinar si orientación, Chern classes, winding o cociclos seleccionan un valor discreto o sólo restricciones globales.

## Gate D — cross-carrier

La misma constante debe predecir al menos dos carriers no isomorfos bajo un transporte UMI y métrico preregistrado.

## Gate E — mixed-state robustness

La estimación no puede depender de elegir retrospectivamente una métrica dentro de la familia de Petz.

## Gate F — future-only

Calibrar \(c_{\rm HG}\) en patches y carriers de entrenamiento; predecir loops, áreas y gaps retenidos.

## Gate G — frontera de constantes

No introducir \(\pi/6\), \(\pi/18\), \(4\pi/9\) o RMNC salvo selección única frente a alternativas.

## Resultados autorizados

- `PASS_DIMENSIONLESS_COUPLING_SELECTION`
- `PASS_CROSS_CARRIER_RESIDUAL`
- `PASS_TOPOLOGICAL_NORMALIZATION`
- `FAIL_COUPLING_UNIQUENESS`
- `FAIL_STANDARD_GEOMETRY_EXCLUSION`
- `HOLD_PHYSICAL_PROTOGEOMETRY`

# HGMF‑HG21 — Campos residuales de flujo cero, modos de Hodge y acoplamiento no local

## Objetivo

Clasificar la clase mínima de correcciones no nulas que sobrevive HG20.

## Gate A — flujo cero

Sobre un bundle topológicamente preservado:

\[
\delta\mathcal F=f\,dA_Q,
\qquad
\int_M f\,dA_Q=0.
\]

## Gate B — base modal

Expandir \(f\) en eigenmodos de Laplace–Beltrami excluyendo el modo constante.

## Gate C — gauge y topología

Separar formas exactas, componentes armónicas, bordes y cambios topológicos.

## Gate D — composición

Derivar una ley de composición para los modos residuales; no admitir un término de interacción libre sin predicciones.

## Gate E — no localidad

Auditar kernels bilocales o dependientes de historia que no reduzcan a \(c\,dA\).

## Gate F — cross-carrier

Transportar espectros y signos mediante un mapa UMI+QGT preregistrado.

## Gate G — future-only

Calibrar modos en patches de entrenamiento y predecir nodos, cambios de signo, loops y carriers retenidos.

## Resultados autorizados

- `PASS_ZERO_FLUX_RESIDUAL_BASIS`
- `PASS_HODGE_MODE_TRANSPORT`
- `PASS_NONLOCAL_COUPLING_FUNCTIONAL`
- `FAIL_MODE_UNIQUENESS`
- `FAIL_STANDARD_GEOMETRY_EXCLUSION`
- `HOLD_PHYSICAL_PROTOGEOMETRY`

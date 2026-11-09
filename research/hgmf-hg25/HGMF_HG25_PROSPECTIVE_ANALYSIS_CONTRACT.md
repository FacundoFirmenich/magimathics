# HGMF‑HG25 — Contrato prospectivo de análisis

## Unidad primaria

La unidad es el bloque experimental completo, no un punto individual del trace.

## Outputs

Conservar por separado:

\[
(A,B,C,K,E,Q,Z).
\]

No se autoriza una media escalar del vector.

## Rectángulos

- calcular sólo con cuatro esquinas observadas;
- reportar por wave y componente;
- separar \(I_{\rm sym}\) e \(I_{\rm ord}\) cuando exista orden de intervención;
- `ABSTAIN` para componentes no identificables.

## Modalidad

- exigir fuente con soporte no nulo;
- congelar eigenblocks;
- 3 bloques de training y 2 de holdout recomendados;
- evaluar candidate families con la misma nuisance y el mismo split;
- no seleccionar kernel por train fit.

## Nodos

- tolerancia preregistrada;
- signs y extrema además de nodes;
- reportar grains;
- prohibido mover el umbral después del holdout.

## Carrier transfer

- map UMI+QGT estimado sólo en training;
- no refit de kernel;
- gamma sólo transferible con calibración común de units;
- usar modal ratios y alignment como outputs dimensionless;
- reportar orientation reversal explícitamente.

## Nuisance

Comparar, como mínimo, contra:

- drift;
- hidden state;
- process tensor;
- control geometry;
- alternative kernels;
- outcome rescaling.

## Authorized adjudications

```text
PASS_CAUSAL_MODAL_SPECTROSCOPY
PASS_KERNEL_PHYSICAL_SELECTION
PASS_DUAL_CARRIER_NODAL_EXECUTION
FAIL_CAUSAL_COLOCALIZATION
FAIL_CROSS_CARRIER_TRANSFER
FAIL_STANDARD_RESPONSE_EXCLUSION
ABSTAIN_INSUFFICIENT_EXECUTION
ABSTAIN_UNCALIBRATED_HOLDOUT
HOLD_PHYSICAL_PROTOGEOMETRY
```

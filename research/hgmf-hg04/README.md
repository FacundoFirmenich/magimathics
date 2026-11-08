# HGMF‑HG04 — Selección no circular de medida en fibras residuales

**Veredicto:** `PASS_UNIFORM_SYMMETRIC_MEASURE_ONLY / PASS_MEASURE_FAMILY / FAIL_GENERAL_NONCIRCULAR_SELECTION / HOLD_BORN_DERIVATION`

## Resultado central

Para una fibra finita `X` y un grupo físico de automorfismos `G`, las medidas invariantes forman un simplex cuyas coordenadas son los pesos de las órbitas. La medida es única si y sólo si la acción es transitiva; en ese caso es uniforme.

La simetría debe preservar preparación, dinámica, posibilidad, outcomes y composición. Una permutación de etiquetas no justifica equiprobabilidad.

## Refinamiento y composición

- El conteo de microestados selecciona pesos sólo si el refinamiento es físicamente canónico y se asume aditividad.
- Refinamientos distintos del mismo espacio coarse producen asignaciones incompatibles.
- Marginales uniformes no fijan la medida conjunta; la independencia o una simetría de producto transitiva son supuestos adicionales.
- En espacios compactos homogéneos, Haar selecciona la medida invariante normalizada, pero no una regla Born de outcomes condicionados.

## Frontera Born

Gleason y Busch caracterizan medidas normalizadas, aditivas y no contextuales dentro de una geometría cuántica ya dada. HG04 no contiene amplitudes, Hilbert, ortogonalidad ni ley cuadrática. Un análisis de 2026 muestra además que la aditividad es indispensable en las principales familias de derivación de Born.

```text
PASS_UNIFORM_SYMMETRIC_MEASURE_ONLY
PASS_ORBIT_WEIGHT_SIMPLEX
PASS_CANONICAL_REFINEMENT_COUNTING_CONDITIONAL
PASS_PRODUCT_MEASURE_CONDITIONAL

FAIL_GENERAL_UNIQUE_FIBRE_MEASURE
FAIL_REFINEMENT_INDEPENDENCE
FAIL_COMPOSITION_WITHOUT_INDEPENDENCE
FAIL_BORN_FROM_FIBRE_SYMMETRY

HOLD_BORN_DERIVATION
```

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `MEASURE_SELECTION_BOUNDARY PASS / AMPLITUDE GEOMETRY PENDING`.

## Next gate

`HGMF‑HG05 — Geometría de amplitudes y tribunal de peso cuadrático`.

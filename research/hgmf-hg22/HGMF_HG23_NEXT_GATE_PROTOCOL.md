# HGMF‑HG23 — Potenciales relacionales triaxiales, normalización de fuente y protocolo nodal empírico

## Objetivo

Derivar o refutar los potenciales físicos que alimentan la fuente canónica de HG22.

## Gate A — potenciales operacionales

Definir \(a_V\) y \(b_H\) desde intervenciones, historia y respuesta observables, con unidades, gauge y resolución preregistrados.

## Gate B — eje diagonal

Auditar si

\[
s_D=*(da_V\wedge db_H)
\]

representa una interrelación diagonal transportable o sólo un Jacobiano descriptivo.

## Gate C — normalización

Derivar la amplitud \(\gamma\), su signo y su escala; no ajustarla retrospectivamente por carrier.

## Gate D — acción

Decidir si la mínima acción Dirichlet queda físicamente seleccionada o si otro kernel es necesario.

## Gate E — experimento nodal

Congelar training patches y predecir nodos, signos y flujos parciales en regiones retenidas.

## Gate F — carrier swap

Transportar potenciales, orientación, QGT y nodos a un segundo carrier no isomorfo.

## Gate G — nuisance

Excluir Poisson/Green estándar, control geometry, hidden ancillas, process tensors y drift instrumental.

## Resultados autorizados

- `PASS_TRIAXIAL_POTENTIAL_DERIVATION`
- `PASS_SOURCE_NORMALIZATION`
- `PASS_EMPIRICAL_NODAL_FALSIFIER`
- `FAIL_POTENTIAL_UNIQUENESS`
- `FAIL_KERNEL_PHYSICAL_SELECTION`
- `FAIL_STANDARD_RESPONSE_EXCLUSION`
- `HOLD_PHYSICAL_PROTOGEOMETRY`

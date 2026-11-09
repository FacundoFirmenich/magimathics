# HGMF‑HG28 — Diseño de orden causal, gatekeeping multicomponente y decisión confirmatoria

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** CONFIRMATORY DESIGN / STRONG FWER / STRICT REPLICATION / ORDER SUBDESIGN / NO EARLY EFFICACY

## Veredicto

PASS_STRICT_TWO_CARRIER_REPLICATION_RULE  
PASS_SEVEN_CHAIN_STRONG_FWER_GATEKEEPING  
PASS_FIXED_FINAL_CONFIRMATORY_MODE  
PASS_SPARSE_ORDER_SUBDESIGN  
PASS_MINIMUM_HOLDOUT_ORDER_PAIRS_THEOREM  
PASS_CONFIRMATORY_CLAIM_LATTICE  

FAIL_BASE_GRID_ORDER_IDENTIFICATION  
FAIL_META_ANALYTIC_SUBSTITUTION_FOR_REPLICATION  
FAIL_EARLY_EFFICACY_MODE  
FAIL_PHYSICAL_PROTOGEOMETRY_CLAIM  

ABSTAIN_EMPIRICAL_CONFIRMATION  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

Los siete componentes (A,B,C,K,E,Q,Z) se conservan como siete cadenas confirmatorias separadas. Con

\[
\alpha=0.05,
\qquad
\alpha_j=\alpha/7=1/140,
\]

cada componente sigue una secuencia fija:

\[
C_j\to M_j\to N_j\to X_j\to O_j,
\]

donde C = interacción causal replicada; M = transferencia modal/kernel; N = transferencia nodal/signo; X = exclusión de la nuisance estándar congelada; O = efecto de orden confirmatorio opcional.

Una cadena sólo avanza si el nodo anterior rechaza a nivel \(\alpha_j\). No existe reciclado entre componentes. Esto controla FWER fuerte por debajo de 0.05 bajo dependencia arbitraria.

La replicación estricta usa

\[
p_{rep}=\max(p_{mag},p_{ads}),
\]

con dirección congelada en training y concordancia de signo después del mapa de orientación. Un carrier significativo no puede rescatar al otro.

## Módulo de orden

El base grid no identifica el conmutador. HG28 selecciona un módulo sparse:

- 3 pares ordenados de training por carrier;
- 8 pares ordenados de holdout por carrier;
- 2 secuencias por par: \(V\to H\) y \(H\to V\).

Total:

\[
(3+8)\times2\times2=44
\]

adquisiciones adicionales máximas.

Como \(\alpha_j=1/140\), un sign-flip exacto one-sided necesita al menos

\[
2^{-n}\le1/140
\Rightarrow n\ge8.
\]

Con 7 pares, el menor p-value posible es \(1/128>1/140\); con 8 es \(1/256<1/140\). Ocho pares holdout son, por tanto, el mínimo discreto.

## Presupuesto

\[
144\text{ base}+44\text{ order}=188
\]

unidades máximas del diseño sparse, frente a 288 de una duplicación completa del orden.

## Estado

No existen receipts experimentales admitidos.

CONFIRMATORY DESIGN = PASS  
EMPIRICAL CONFIRMATION = ABSTAIN  
PHYSICAL PROTOGEOMETRY = HOLD

## Próxima frontera

HGMF‑HG29 — Umbrales confirmatorios, nuisance-exclusion test y preregistro ejecutable de claims.

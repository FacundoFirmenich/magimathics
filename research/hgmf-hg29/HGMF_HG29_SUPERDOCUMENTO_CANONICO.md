# HGMF‑HG29 — Tests confirmatorios ejecutables y exclusión de nuisance congelada

## Veredicto

PASS_EXECUTABLE_CAUSAL_TEST  
PASS_EXECUTABLE_MODAL_ALIGNMENT_TEST  
PASS_EXECUTABLE_NODAL_BRACKET_IUT  
PASS_FROZEN_NUISANCE_ENVELOPE_IUT  
PASS_EXECUTABLE_ORDER_SIGN_TEST  
PASS_MACHINE_ADJUDICATOR_CORE  
PASS_STRICT_REPLICATION_INTEGRATION  

FAIL_UNRESTRICTED_STANDARD_PHYSICS_EXCLUSION  
FAIL_NUISANCE_EXCLUSION_BY_BEST_FIT_ONLY  

ABSTAIN_NUISANCE_FAMILY_ADAPTERS_UNTIL_IMPLEMENTED  
ABSTAIN_EMPIRICAL_ADJUDICATION  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. Corrección del nodo X

HG28 usó provisionalmente la etiqueta StandardNuisanceExclusion. HG29 la restringe a:

\[
\boxed{\text{FROZEN STANDARD NUISANCE ENVELOPE EXCLUSION}}
\]

y la claim a:

CANDIDATE_OUTSIDE_FROZEN_STANDARD_NUISANCE_ENVELOPE.

La restricción es necesaria: un null estándar irrestricto con representaciones suficientemente saturadas no es falsable por un dataset finito.

## 2. Nodo C

El vector de 14 rectángulos holdout se construye linealmente desde las 24 celdas de wave 3:

\[
I=Dy.
\]

La covariance se propaga:

\[
\Sigma_I=D\Sigma_yD^\top.
\]

Un template training-frozen produce un único statistic directional. Esto evita seleccionar después qué rectángulos “funcionaron”.

## 3. Nodo M

El modal statistic es un matched filter contra la predicción frozen. La claim es modal alignment. No se confunde un buen alignment con unicidad ontológica del kernel.

## 4. Nodo N

Los nodos se convierten en brackets de signo. Cada flank posee un test one-sided y la conjunción usa el máximo p-value. La distancia geométrica al zero crossing se reporta, pero no determina retrospectivamente el pass/fail.

## 5. Nodo X

Cada familia nuisance debe emitir un p-value holdout calibrado. Se admite, por ejemplo, un split predictive check donde el modelo se ajusta sólo en training y se critica en holdout.

\[
p_X=\max_kp_k.
\]

Si falta una familia required, X abstiene.

## 6. Nodo O

El sign test sustituye al sign-flip de magnitud como default confirmatorio, reduciendo el supuesto de simetría de magnitudes. Con ocho pares, sólo una concordancia 8/8 alcanza el umbral local \(1/140\).

## 7. Machine adjudicator

El adjudicator no ajusta modelos ni repara datos. Sólo:

- verifica holdout;
- replica 2/2;
- aplica X como IUT;
- ejecuta la secuencia fija;
- emite la claim máxima;
- mantiene siempre physical_protogeometry_confirmed=false.

## 8. Estado

No hay datos admitidos y los cinco adapters físicos de nuisance todavía no están implementados. Por tanto el pipeline estadístico central está especificado, pero el primer end-to-end real no puede ejecutarse.

## 9. Próxima frontera

HGMF‑HG30 — Adaptadores nuisance físicos, covariance receipts y dry-run end-to-end sin datos empíricos.

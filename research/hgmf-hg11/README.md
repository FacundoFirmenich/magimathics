# HGMF‑HG11 — Singlete transicional y frontera de peso uno

**Fecha:** 9 de noviembre de 2026  
**Veredicto:** `PASS_WEIGHT_ONE_IDENTITY / PASS_TRANSITIONAL_SINGLET_CONDITIONAL / PASS_SEMANTIC_BOUNDARY / FAIL_ACTUALITY_FROM_PROBABILITY_ONE`.

## Resultado central

Para un proyector ortogonal `P` y un estado no nulo `psi`:

\[
1-q_\psi(P)=\frac{\|(I-P)\psi\|^2}{\|\psi\|^2},
\]

por tanto

\[
q_\psi(P)=1\iff P\psi=\psi.
\]

`q -> 1` expresa aproximación métrica al subespacio; `q = 1` expresa pertenencia algebraica exacta. Un singlete estricto requiere además que el evento sea atómico/minimal. Un proyector coarse de rango mayor que uno puede tener peso uno y conservar múltiples micro-outcomes.

## Probabilidad y pseudoforma sin probabilística

Una medida delta sigue siendo una probabilidad en el sentido matemático estándar. Lo que desaparece es la ramificación no degenerada:

\[
\operatorname{supp}\delta_{y_*}=\{y_*\},\qquad H=0,\qquad \operatorname{Var}=0.
\]

La intuición histórica se formaliza como degeneración del carrier probabilístico hacia una identidad de soporte único, no como prohibición del valor matemático uno.

## Identidad tipada PRV–PSP

La protoforma real-virtual y la pseudoforma no son objetos del mismo tipo. La igualdad rigurosa es

\[
\boxed{\Delta(\Pi_\lambda(\mathsf P_{RV}^{*}))=\mathsf p_{sp}^{*}=\delta_{y_*}}.
\]

La comparación se realiza después del transporte al espacio común de medidas sobre outcomes. La igualdad literal no tipada `PRV = PSP` queda rechazada.

## Probability-one boundary

- medida uno no equivale necesariamente a evento seguro en espacios infinitos;
- peso uno no implica necesidad lógica;
- peso uno no implica que un token outcome ya haya ocurrido;
- peso uno sobre un evento coarse no identifica un micro-outcome;
- el endpoint no determina la regla de pesos en el interior y no deriva retrospectivamente Born.

## Microsingularidad

La función `q` puede llegar continuamente a uno, pero la estrata del simplex cambia en el endpoint: el soporte pasa de múltiples outcomes a un vértice delta. Se autoriza el término `microsingularidad` sólo como singularidad semántico-estratificada, no como singularidad física demostrada.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `TRANSITIONAL_SINGLET_FORMAL_PASS / ACTUALITY_AND_PROTOFORM_PHYSICS_HOLD`.

## Next gate

`HGMF‑HG12 — Dinámica de identidad transicional y lift helicoidal`.

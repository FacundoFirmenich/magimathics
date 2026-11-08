# HGMF‑HG09 — Núcleo formal

## Definición — Perfil funcional de chance

Una asignación q ocupa el rol operacional de chance si satisface:

1. calibración;
2. optimalidad bajo una clase separante de scores estrictamente propios;
3. estabilidad bajo preparaciones operacionalmente equivalentes;
4. sensibilidad correcta bajo intervenciones;
5. screening-off de la historia dada la preparación operacional completa.

## Teorema 1 — Unicidad predictiva

Para un kernel Bernoulli K_q, q es el único reporte óptimo bajo Brier y log score.

## Teorema 2 — Dilatación determinista

Para todo kernel de Markov K de un espacio medible a un espacio estándar de Borel, existe f(x,u) medible con u uniforme en [0,1] tal que:

\[
f(x,U)\sim K(x,\cdot).
\]

Por tanto, el kernel observado no identifica estocasticidad primitiva.

## Teorema 3 — Screening-off dual

Existe una dinámica determinista en un espacio ampliado y una medida inicial para la cual el proceso observado es IID y satisface screening-off operacional, mientras el futuro completo es función del hidden seed.

## Teorema 4 — Insuficiencia ontológica del rol

Ningún conjunto de propiedades que dependa exclusivamente del kernel observado, sus intervenciones y su calibración puede distinguir dos realizaciones que comparten ese kernel.

## Corolario

El rol operacional puede caracterizar chance funcional, pero no chance modal irreducible.

## Frontera

Para identificar chance modal se necesita una noción independiente de estado físico completo y un criterio que excluya toda dilatación determinista físicamente admisible.

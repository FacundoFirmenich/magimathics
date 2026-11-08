# HGMF‑HG12 — Dinámica de identidad transicional y lift helicoidal

**Fecha:** 9 de noviembre de 2026  
**Veredicto:** `PASS_TRANSITIONAL_PATH_FORMALISM / PASS_HELICAL_LIFT_CONDITIONAL / PASS_MONODROMY_INVARIANT / FAIL_HELICAL_UNIQUENESS / HOLD_PHYSICAL_SPIN_IDENTIFICATION`

## Resultado rector

HG11 fijó el endpoint atómico. HG12 demuestra que

\[
q(t)=\langle\psi_t|P_*|\psi_t\rangle
\]

sólo fija la distancia radial al singlete. No fija azimut, winding, longitud Fubini–Study ni fase global.

El testigo qubit construye windings `0,1,3,10` con el mismo `q(t)` y longitudes entre `0.785398` y `20.034843`.

## Lift helicoidal

Dado un bundle `U(1)`, conexión `A` y métrico base:

\[
\nu_A=\dot\chi+A(\dot\gamma).
\]

Un pitch constante satisface

\[
\nu_A=\kappa\|\dot\gamma\|.
\]

La condición es gauge-invariante para conexión fijada, pero no independiente de la conexión ni de la dinámica.

## No unicidad

El mismo loop ecuatorial admite pitches `+1,0,-1,+2`. El lift horizontal de pitch cero tiene holonomía `-1`. Por tanto, holonomía y cierre de base no seleccionan una hélice única.

## Antiagregación

Windings `+1` y `-1` promedian una curva que atraviesa el origen y pierde winding. La media de holonomías abandona `U(1)` en general, y la media de estados puros puede destruir pureza y fase.

## Spin boundary

Geometric phase and a `-1` holonomy do not prove physical spin. Spin requires a representation of spatial rotations, generators, Casimir and dynamics.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `TRANSITIONAL PATH / HOLONOMY PASS; HELICAL UNIQUENESS FAIL; SPIN HOLD`.

## Next gate

`HGMF‑HG13 — Selección de conexión, generador físico y dinámica helicoidal`.

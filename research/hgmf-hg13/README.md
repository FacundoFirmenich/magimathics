# HGMF‑HG13 — Selección de conexión, generador físico y dinámica helicoidal

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / HILBERT BUNDLE / INVERSE DYNAMICS / ENERGY-GAUGE AUDIT`

## Veredicto

```text
PASS_CONNECTION_SELECTION_CONDITIONAL
PASS_MINIMAL_GENERATOR_THEOREM
PASS_CONSTANT_PITCH_FROM_AUTONOMOUS_H_CONDITIONAL
PASS_PROJECTIVE_NONCIRCULAR_INVARIANT
PASS_CURVATURE_HOLONOMY_BOUNDARY

FAIL_INTRINSIC_HELICAL_PITCH
FAIL_UNIQUE_HAMILTONIAN_FROM_RAY_PATH
FAIL_TOPOLOGICAL_MONODROMY_FROM_HOLONOMY
FAIL_GEOMETRIC_PHASE_AS_SPIN

HOLD_ACTION_SELECTED_HELICAL_DYNAMICS
HOLD_PHYSICAL_SPIN_IDENTIFICATION
```

## Resultado central

La conexión canónica de Pancharatnam–Berry queda seleccionada unívocamente por el producto interno de Hilbert, la invariancia unitaria completa y la normalización vertical. Sin embargo, una trayectoria proyectiva no determina un Hamiltoniano único ni un pitch helicoidal no nulo.

Para la familia general que realiza el mismo rayo:

\[
H=H_{\min}+hP+K,
\qquad K\psi=0,
\]

la trayectoria fija \(\Delta H\), pero deja libre \(\langle H\rangle=h\). Respecto de la conexión canónica:

\[
\kappa=-\frac{\langle H\rangle}{\Delta H}.
\]

Un Hamiltoniano autónomo produce pitch constante, pero \(H+cI\) preserva toda la trayectoria de rayos y cambia \(\kappa\). El pitch no es un invariante proyectivo intrínseco sin una referencia externa de fase o de cero de energía.

## Invariante no circular

\[
\mathcal E_{\rm proj}=L_{\rm FS}-d_{\rm FS}
\]

es invariante de gauge, trivialización y reparametrización. Detecta no geodesicidad y distingue las trayectorias con igual \(q(t)\) de HG12, pero no caracteriza de forma única una hélice.

## Frontera de holonomía

Puede existir holonomía de Berry no trivial en loops contractibles porque la conexión canónica posee curvatura. La monodromía topológica requiere defectos, degeneraciones removidas o topología adicional del espacio de parámetros.

## Frontera de spin

Un qubit, una holonomía \(-1\) o una fase geométrica no establecen spin físico. Se requieren representación de rotaciones espaciales, generadores, Casimir, acoplamiento y contraste experimental.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `CANONICAL CONNECTION + MINIMAL GENERATOR PASS; INTRINSIC HELICAL DYNAMICS FAIL; SPIN HOLD`.

## Next gate

`HGMF‑HG14 — Canonical Dynamics, Contact Flow and Helical Falsifiers`.

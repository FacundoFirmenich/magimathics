# HGMF‑HG27 — No-go de identificación del orden desde el grid base

El grid de 72 celdas por carrier soporta rectángulos factoriales, pero no contiene ambas composiciones ordenadas.

En un contexto \(x\):

\[
y_0=m(x),\quad y_V=m(\Phi_Vx),\quad y_H=m(\Phi_Hx),
\]

\[
y_{HV}=m(\Phi_H\Phi_Vx),\quad y_{VH}=m(\Phi_V\Phi_Hx).
\]

\[
I_{ord}=\tfrac12(y_{HV}-y_{VH}).
\]

Sin ambos joint outcomes, \(I_{ord}\) no está identificado.

Si baseline y singles ya están observados, cada contexto seleccionado necesita dos adquisiciones ordered-joint adicionales. Duplicar ambos grids bajo secuencia reversa requeriría hasta 144 unidades extra.

```text
BASE GRID => SYMMETRIC FACTORIAL INTERACTION
BASE GRID != ORDER/COMMUTATOR EFFECT
```

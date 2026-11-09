# HGMF‑HG36 — Teorema de no-identificación de la referencia Vycor

Cimino et al. escriben el observable como

[
V(p)=V_s(p)Q(p)+(1-Q(p))V_c(p),
]

de donde

[
Q(p)=rac{V_c(p)-V(p)}{V_c(p)-V_s(p)}.
]

El método requiere:

- (V_s): film reference isotherm sobre una superficie no porosa del mismo origen;
- (V_c): reference de condensed fluid, extrapolada desde la meseta reversible superior.

Brown proporciona (V(p)) boundary/scanning en Vycor, pero no una isoterma no-porosa Xe/silica que point-identifique (V_s).

## Teorema

Fijados (V(p)) y (V_c(p)>V(p)), para cualquier (Q(p)in(0,1]) que produzca una referencia físicamente admisible,

[
V_s(p)=rac{V(p)-(1-Q(p))V_c(p)}{Q(p)}
]

genera exactamente el mismo observable (V(p)).

Por tanto, sin una restricción externa suficiente sobre (V_s),

[
V(p),V_c(p)
otRightarrow Q(p)
]

de forma única.

Como el Bethe inverse map utiliza (Q_+) y (Q_-),

[
Q	ext{ no identificado}Rightarrow q(p)	ext{ no identificado}.
]

## Consecuencia

Los datos Brown pueden acotar (V_s,Q,q) mediante monotonicidad, closure points y el boundary loop, pero no convertirlos en point estimates con autoridad confirmatoria.

Un likelihood completo requiere una de:

1. film reference Xe/silica externa;
2. surface area + FHH parameters calibrados independientemente;
3. una prior/constraint física con cobertura explícita incorporada al null.

No se permite elegir (V_s) para mejorar el ajuste de los scanning runs.

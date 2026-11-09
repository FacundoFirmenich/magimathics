# HGMF‑HG36 — Teorema de no-potencia del summary HEB con resolución de campo acotada

Sea, para cada loop entrenado,

[
h_n^{obs}=mu_n+delta_n+arepsilon_n,
]

donde:

- (mu_n) es el exchange bias físico;
- (delta_nin[-Delta_n,Delta_n]) representa la incertidumbre/discretización del eje de campo;
- (arepsilon_n) es el ruido de voltaje propagado al estimator HEB.

El source-specific trained null fija:

[
mu_n=0,qquad n=2,dots,5.
]

## Teorema

Si

[
|h_n^{obs}|leDelta_n
]

para todo loop entrenado, entonces el profile null puede elegir

[
delta_n=h_n^{obs}.
]

Por tanto el residual estocástico puede ser cero:

[
h_n^{obs}-mu_n-delta_n=0.
]

Para cualquier observation density centrada y maximizada en residual cero, el profile likelihood del null alcanza el peak observacional de cada summary.

Si además (mu_1) es libre bajo el estado metastable del primer loop, todo el vector summary (h_{1:5}) puede ser interpolado por el null.

Consecuencia:

[
oxed{	ext{HEB-SUMMARY UNIVERSAL E-VALUE}le 1}
]

contra esta clase de nuisance.

## Interpretación

El bootstrap de raw voltage puede demostrar que (arepsilon_n) es pequeño. Eso no elimina (delta_n).

Para obtener potencia hace falta al menos una de estas rutas:

1. calibración del eje de campo con incertidumbre mucho menor que el step;
2. observation likelihood sobre la curva completa (V_{xy}(H)), no sólo sus dos cruces;
3. un constraint físico compartido que acople (delta_n) entre loops y no permita ajustarlos independientemente.

Este resultado no confirma el source mechanism; demuestra que HEB solo, con la resolución actual, no puede falsarlo.

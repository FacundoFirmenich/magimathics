# HGMF‑HG28 — Teorema de gatekeeping confirmatorio

Sean siete familias disjuntas, una por componente, con presupuesto local \(\alpha_j=\alpha/7\). En cada familia se aplica un fixed-sequence test

\[
H_{C,j}\to H_{M,j}\to H_{N,j}\to H_{X,j}\to H_{O,j}.
\]

Cada hipótesis sólo se prueba si todas sus predecesoras fueron rechazadas, y cada test usa nivel \(\alpha_j\).

Entonces, para cualquier configuración de nulls y cualquier dependencia entre estadísticas,

\[
\boxed{\mathrm{FWER}\le\alpha.}
\]

En una cadena fija, si existe al menos un null verdadero, el primer null verdadero sólo puede rechazarse mediante un test de nivel \(\alpha_j\). Rechazar cualquier null verdadero en la cadena implica rechazar ese primer null verdadero, por lo que

\[
\Pr(V_j\ge1)\le\alpha_j.
\]

Por unión:

\[
\Pr\left(\bigcup_j\{V_j\ge1\}\right)
\le\sum_j\alpha_j
=\alpha.
\]

Consecuencias:

- no se necesita independencia;
- no se necesita una media multicomponente;
- no se recicla alpha entre componentes;
- una cadena fuerte no financia otra cadena débil;
- los componentes siguen auditables por separado.

El diseño es deliberadamente más conservador que un graphical recycling completo. La pérdida de potencia compra una frontera de claims especialmente limpia.

# HGMF‑HG28 — Teorema de replicabilidad direccional y gatekeeping

## Teorema 1 — Conjunción 2/2

Sea \(p_M^+\) un p-value válido para \(H_{0,M}^+:\theta_M\le0\), y \(p_A^+\) análogo. Para la hipótesis nula:
\[
H_{0,+}^{rep}=H_{0,M}^+\cup H_{0,A}^+,
\]
el estadístico
\[
p_+^{rep}=\max(p_M^+,p_A^+)
\]
es un p-value válido sin requerir independencia.

Bajo la unión nula, al menos uno de los dos nulls es verdadero; entonces
\[
\Pr(\max(p_M^+,p_A^+)\le u)
\le
\Pr(p_{true}\le u)
\le u.
\]

El mismo resultado vale para la dirección negativa.

## Teorema 2 — Dirección desconocida

Si la dirección no se preregistra:
\[
p^{rep}
=
\min\{1,2\min(p_+^{rep},p_-^{rep})\}
\]
es válido por Bonferroni sobre las dos direcciones.

HG28 no utiliza excepciones que permitan omitir el factor dos.

## Teorema 3 — Familia de 14 claims

Aplicar Holm a los 14 p-values:
\[
7\text{ componentes}\times2\text{ estimandos causales}
\]
controla:
\[
FWER\le0.05
\]
bajo dependencia arbitraria.

## No sustitución por meta-análisis

Un meta-análisis puede ser significativo si un carrier es fuerte y el otro casi nulo. Eso no satisface una claim 2/2.

\[
\boxed{\text{META-ANALYTIC SIGNAL}\neq\text{REPLICATED SIGNAL}.}
\]

## Missing carrier/order module

Si un claim no posee ambos carriers o el order module no fue ejecutado, el algoritmo confirmatorio lo trata como no rechazable y la clasificación sustantiva es ABSTAIN_NOT_TESTABLE.

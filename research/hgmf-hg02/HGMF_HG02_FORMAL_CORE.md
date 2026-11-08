# HGMF‑HG02 — Núcleo formal

## Definición 1 — Mapa conjunto

\[
\Phi_A:\mathcal P\to\prod_{\lambda\in A}\mathcal G_\lambda,
\qquad
\Phi_A(P)=(\Phi_\lambda(P))_{\lambda\in A}.
\]

## Teorema 1 — Identificabilidad conjunta

\[
\ker\Phi_A
=
\bigcap_{\lambda\in A}\ker\Phi_\lambda.
\]

Por tanto:

\[
\Phi_A\text{ es inyectiva}
\iff
\bigcap_{\lambda\in A}\sim_\lambda
=
\Delta_{\mathcal P}.
\]

## Definición 2 — Saturación observacional

\[
\sim_{\rm sat}
=
\bigcap_{\lambda\in\Lambda_{\rm adm}}\sim_\lambda,
\]

\[
[P]_{\rm sat}
=
\{P':P'\sim_{\rm sat}P\}.
\]

## Teorema 2 — Límite de saturación

Ninguna familia de contextos contenida en \(\Lambda_{\rm adm}\) puede separar dos estados de la misma clase saturada.

## Definición 3 — Pares separables

\[
U_{\rm sep}
=
\{\{P,P'\}:\exists\lambda\in\Lambda_{\rm adm},\ \Phi_\lambda(P)\ne\Phi_\lambda(P')\}.
\]

Una familia alcanza saturación si cubre todos los pares de \(U_{\rm sep}\). Encontrar una familia mínima es un problema de set cover.

## Definición 4 — Hiperacceso

\[
F(A)
=
\left|
\bigcup_{\lambda\in A}S_\lambda
\right|,
\]

con \(S_\lambda\) el conjunto de pares separados por \(\lambda\).

## Teorema 3 — Submodularidad

Para \(A\subseteq B\) y \(\lambda\notin B\):

\[
F(A\cup\{\lambda\})-F(A)
\ge
F(B\cup\{\lambda\})-F(B).
\]

## Definición 5 — Certidumbre relativa a propiedad

Una propiedad \(Q\) es cierta bajo \(A\) en \(P\) si

\[
Q(P')=Q(P)
\qquad
\forall P'\in[P]_A.
\]

La certidumbre de \(Q\) no implica que \([P]_A\) sea singleton.

## Corolario — Proto-certidumbre

Una identidad transicional puede quedar determinada exactamente por un contexto aunque el código protogeométrico permanezca no identificado.

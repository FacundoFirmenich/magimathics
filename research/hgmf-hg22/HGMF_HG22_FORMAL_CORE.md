# HGMF‑HG22 — Núcleo formal

## 1. Fuente relacional

Sea \((M,g,dA)\) una superficie orientada y sean \(a,b\in C^\infty(M)\) dos potenciales relacionales preregistrados. Defina

\[
\Sigma[a,b]=da\wedge db,
\qquad
s[a,b]=*\Sigma[a,b],
\qquad
\Sigma=s\,dA.
\]

En una superficie cerrada:

\[
\int_Ms\,dA=\int_Mda\wedge db=\int_Md(a\,db)=0.
\]

La fuente es bilineal, antisimétrica, orientation-sensitive y nula cuando \(da\wedge db=0\).

## 2. Unicidad dentro de la clase declarada

Todo operador escalar universal, de primer orden, bilineal y alternante que dependa sólo de \(da,db\), del métrico y de la orientación, sin campos geométricos adicionales ni escala nueva, es proporcional a

\[
*(da\wedge db).
\]

La razón puntual es que el espacio de formas bilineales alternantes invariantes de \(SO(2)\) es unidimensional. La normalización fija el factor.

La conclusión no selecciona los campos \(a,b\). Tampoco excluye multiplicadores dependientes de curvatura si se amplía la clase de operadores.

## 3. Respuesta de mínima acción

En el subespacio de funciones de media cero, considere

\[
\mathcal A[f;s]
=\frac12\int_M|\nabla f|^2dA
-\gamma\int_Mfs\,dA.
\]

El minimizador único satisface

\[
\mathcal Lf=\gamma s,
\qquad
f=\gamma\mathcal L^{-1}s.
\]

Si

\[
s=\sum_{n\ge1}a_n\phi_n,
\]

entonces

\[
f=\gamma\sum_{n\ge1}\frac{a_n}{\lambda_n}\phi_n.
\]

La respuesta Green queda seleccionada sólo dentro de la clase local, cuadrática, isotrópica, second-order, shift-invariant y sin escala adicional. Mass terms, higher derivatives y kernels no locales reabren la no unicidad.

## 4. Composición

Para \(a=a_A+a_B\), \(b=b_A+b_B\):

\[
s_{AB}=s_A+s_B+s_{\rm int},
\]

\[
s_{\rm int}=\{a_A,b_B\}+\{a_B,b_A\}.
\]

En un producto realmente independiente con estructura de Poisson block-diagonal y campos soportados en factores distintos, los términos cruzados se anulan.

## 5. Transporte

Si \(\varphi:M_1\to M_2\) es una isometría orientada y

\[
a_1=\varphi^*a_2,
\qquad
b_1=\varphi^*b_2,
\]

entonces

\[
s_1=\varphi^*s_2,
\qquad
f_1=\varphi^*f_2,
\]

para la respuesta Green. Así

\[
Z(f_1)=\varphi^{-1}(Z(f_2)).
\]

Una inversión de orientación cambia el signo de \(s\) y \(f\), pero conserva el nodal set.

## 6. Frontera

HG22 selecciona un operador fuente y un contrato nodal condicional. No selecciona los potenciales físicos, el acoplamiento, el kernel general ni un origen protogeométrico distinto de respuestas estándar.

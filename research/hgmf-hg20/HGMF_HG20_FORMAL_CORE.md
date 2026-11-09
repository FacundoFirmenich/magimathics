# HGMF‑HG20 — Núcleo formal

## 1. Ansätz auditado

\[
\delta\mathcal F
=
\frac{c_{\rm HG}}{\hbar^2}dA_{\rm act}
=
c_{\rm HG}dA_Q.
\]

El gate no supone que éste sea el único ansatz posible. Audita si un coeficiente constante, local y universal puede sobrevivir composición, topología y transporte transcarrier.

## 2. Teorema de mismo bundle

Sean \(\nabla_{\rm obs}\) y \(\nabla_{\rm std}\) dos conexiones sobre el mismo line bundle \(L\to M\). Entonces

\[
\delta\mathcal F
=
\mathcal F_{\rm obs}-\mathcal F_{\rm std}
=
d\alpha
\]

para alguna 1-forma global \(\alpha\). Si \(M\) es cerrada:

\[
\int_M\delta\mathcal F=0.
\]

Si, además,

\[
\delta\mathcal F=c_{\rm HG}dA_Q
\]

con \(dA_Q\) positiva y \(c_{\rm HG}\) constante, entonces

\[
c_{\rm HG}\operatorname{Vol}_Q(M)=0,
\]

por lo que

\[
\boxed{c_{\rm HG}=0.}
\]

## 3. Teorema de composición

Para estados producto sobre el mismo manifold contextual:

\[
Q_{AB}=Q_A+Q_B,
\qquad
\mathcal F_{AB}=\mathcal F_A+\mathcal F_B.
\]

Si el residual de sistemas independientes debe ser aditivo:

\[
\delta\mathcal F_{AB}
=
\delta\mathcal F_A+\delta\mathcal F_B,
\]

el ansatz exige

\[
c\,dA(g_A+g_B)
=
c[dA(g_A)+dA(g_B)].
\]

Esto falla genéricamente porque

\[
\sqrt{\det(g_A+g_B)}
\neq
\sqrt{\det g_A}+\sqrt{\det g_B}.
\]

El testigo

\[
g_A=\operatorname{diag}(1,4),
\qquad
g_B=\operatorname{diag}(4,1)
\]

produce

\[
dA_A=2,\quad dA_B=2,\quad dA_{AB}=5.
\]

La aditividad fuerza \(5c=4c\), luego \(c=0\).

## 4. Topología

Si se permite cambiar el line bundle:

\[
\Delta C_1
=
\frac{1}{2\pi}\int_M\delta\mathcal F
=
\frac{c_{\rm HG}}{2\pi}\operatorname{Vol}_Q(M)
\in\mathbb Z.
\]

En la esfera de Bloch:

\[
\operatorname{Vol}_Q=\pi
\quad\Rightarrow\quad
c_{\rm HG}/2\in\mathbb Z.
\]

En el carrier exacto con ancilla oculta de HG18:

\[
\operatorname{Vol}_Q=\pi\sqrt5
\quad\Rightarrow\quad
c_{\rm HG}\sqrt5/2\in\mathbb Z.
\]

No existe solución común no nula. Si \(c=2m\), la segunda condición exige \(m\sqrt5\in\mathbb Z\), imposible para \(m\neq0\).

## 5. Mixed-state boundary

Para un residual fijo y una métrica isotrópica \(g_f=m_fI\):

\[
c_f\propto\frac{1}{m_f}.
\]

La familia Petz de HG19 produce distintos valores. Sin un principio previo que seleccione Bures/SLD, el coeficiente no es metric-independent.

## 6. Clase residual sobreviviente

En una superficie cerrada y sobre el mismo bundle, escriba

\[
\delta\mathcal F=f\,dA_Q.
\]

La condición necesaria es

\[
\boxed{\int_M f\,dA_Q=0.}
\]

El modo constante queda excluido. Sobreviven perfiles sign-changing, exactos, no locales o interaction-dependent. Ésa es la frontera HG21.

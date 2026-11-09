# HGMF‑HG23 — Núcleo formal

## 1. Formas de respuesta intervenida

Para cada contexto \(\lambda\in M\), las intervenciones preregistradas producen 1-formas de respuesta \(\omega_V\) y \(\omega_H\). La atribución causal pertenece al diseño experimental que define dichas formas, no a la descomposición geométrica posterior.

## 2. Proyección Hodge

En una superficie cerrada:

\[
\omega=da+\delta\beta+h.
\]

Con gauge \(\int_Ma\,dA=0\):

\[
\mathcal La=d^\dagger\omega.
\]

Equivalentemente:

\[
a=\arg\min_{\int a=0}\|\omega-da\|_2^2.
\]

El potencial es único una vez fijados métrico, orientación, boundary conditions y gauge.

## 3. Fuente diagonal

\[
s_D=*(da_V\wedge db_H).
\]

En una superficie cerrada:

\[
\int_Ms_DdA=\int_Mda_V\wedge db_H=0.
\]

Es el Jacobiano orientado del mapa \((a_V,b_H)\).

## 4. No-go causal

La no nulidad de \(s_D\) sólo implica independencia lineal de \(da_V\) y \(db_H\). No implica que un outcome posea interacción causal entre las intervenciones vertical y horizontal. Un contraste do-interventional o una mixed response derivative debe auditarse separadamente.

## 5. Normalización de Dirichlet

\[
E_V=\|da_V\|_2^2,
\qquad E_H=\|db_H\|_2^2.
\]

Para \(E_VE_H>0\):

\[
\widehat s_D=\frac{s_D}{\sqrt{E_VE_H}}.
\]

Preserva exactitud y flujo cero, y elimina shifts y escalas afines positivas.

## 6. Índice de orientación

En el conjunto regular:

\[
\chi_D=\frac{*(da_V\wedge db_H)}{|da_V||db_H|}.
\]

Bajo \(a\mapsto F(a)\), \(b\mapsto G(b)\) con \(F'G'>0\), \(\chi_D\) es invariante. Si uno de los gradientes se anula:

```text
ABSTAIN_LOCAL_ORIENTATION_UNDEFINED
```

## 7. Potenciales vectoriales y whitening

Para \(\mathbf a\in\mathbb R^p\), \(\mathbf b\in\mathbb R^q\):

\[
G_V=\int d\mathbf a\,d\mathbf a^\top dA,
\qquad
G_H=\int d\mathbf b\,d\mathbf b^\top dA.
\]

Si ambos son invertibles, se blanquean los potenciales y se define

\[
\mathbf S_D=*(d\widehat{\mathbf a}\wedge d\widehat{\mathbf b}^{\top}).
\]

Bajo \(\mathbf a' = A\mathbf a\), \(\mathbf b'=B\mathbf b\), las fuentes blanqueadas se relacionan por

\[
\mathbf S_D'=O_V\mathbf S_DO_H^\top
\]

con matrices ortogonales \(O_V,O_H\). Por tanto, singular values, rango y norma Frobenius son invariantes.

## 8. Respuesta

Green queda seleccionada sólo dentro de la clase de acciones locales, cuadráticas, isotrópicas, shift-invariant y sin escala nueva:

\[
\mathcal Lf=\gamma\widehat s_D.
\]

La geometría no determina \(\gamma\). Otros kernels cambian los nodos.

## 9. Transporte

Una isometría QGT orientada que transporta las formas de respuesta transporta sus proyecciones Hodge, la fuente normalizada y los nodos. Una inversión de orientación cambia el signo y preserva el conjunto nodal.

## 10. Frontera

El gate selecciona una arquitectura operacional y una normalización geométrica. No deriva la elección física de canales, el acoplamiento de respuesta, el kernel real ni un origen protogeométrico.

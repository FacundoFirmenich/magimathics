# HGMF‑HG40 — Núcleo formal de identificabilidad por cociente afín

## 1. Teorema del cociente afín etiquetado

Sean \(m\ge3\) observaciones etiquetadas:

\[
y_i=a+b x_i,
\qquad b\ne0.
\]

Fijados dos anchors no degenerados \(r,s\), defina:

\[
\rho_i
=
\frac{y_i-y_r}{y_s-y_r}.
\]

Entonces:

\[
\rho_i
=
\frac{x_i-x_r}{x_s-x_r}.
\]

Por tanto, ​\(\rho_i\) es invariante bajo la nuisance afín ​\((a,b)\).

### Completitud

Si dos configuraciones etiquetadas no degeneradas poseen las mismas coordenadas ​\(\rho_i\), existe una única transformación afín que lleva una configuración a la otra y mapea ambos anchors.

Luego el cociente de ​\(m\) observaciones por el grupo afín unidimensional posee:

\[
\boxed{m-2}
\]

grados identificables.

Esto no recupera la escala absoluta; recupera toda la geometría relativa que la nuisance afín no puede alterar.

---

## 2. Corolario magnético

Suponga una calibración compartida entre loops:

\[
H'=\alpha H+\beta,
\qquad \alpha>0.
\]

Para coercivos ​\(C_{n,-},C_{n,+}\):

\[
H_{EB,n}
=
\frac{C_{n,-}+C_{n,+}}2,
\qquad
W_n
=
\frac{C_{n,+}-C_{n,-}}2.
\]

Entonces:

\[
H'_{EB,n}=\alpha H_{EB,n}+\beta,
\qquad
W'_n=\alpha W_n.
\]

Son invariantes:

\[
\frac{H_{EB,i}-H_{EB,j}}{W_k},
\qquad
\frac{W_i}{W_j},
\qquad
\frac{H_{EB,i}-H_{EB,r}}
     {H_{EB,s}-H_{EB,r}}.
\]

### Corrección a HG36

El no‑go de HG36 continúa siendo correcto para offsets libres e independientes por loop.

Pero una calibración común afín posee sólo dos grados de nuisance. Para cinco loops quedan:

\[
5-2=3
\]

grados relativos identificables.

Por tanto:

```text
INDEPENDENT LOOP OFFSETS  -> summary saturation
COMMON AFFINE CALIBRATION -> relative training geometry survives
```

La recuperación es parcial: no identifica campo absoluto ni sustituye un likelihood completo de ​\(V_{xy}(H)\).

---

## 3. Corolario de adsorción

A presión y temperatura fijas:

\[
V_h
=
V_s Q_h+(1-Q_h)V_c
=
V_c-DQ_h,
\qquad
D=V_c-V_s>0.
\]

Para tres o más historias medidas al mismo ​\((p,T)\):

\[
\frac{V_h-V_r}{V_s^{\star}-V_r}
=
\frac{Q_h-Q_r}{Q_s-Q_r},
\]

donde ​\(V_s^{\star}\) denota aquí el observable de la historia anchor ​\(s\), no la film reference.

Así, las coordenadas relativas entre historias eliminan exactamente:

\[
V_s(p,T),\qquad V_c(p,T).
\]

### Alcance

El cociente es pointwise en ​\((p,T)\). Como ​\(V_s,V_c\) varían con presión y temperatura, no autoriza:

- comparar escalas absolutas entre presiones;
- reconstruir ​\(Q(p)\) o ​\(q(p)\) absolutos;
- fabricar un likelihood de masa adsorbida sin modelo adicional.

Sí autoriza testar restricciones cross‑history que vivan enteramente en el cociente.

---

## 4. Teorema de no‑passing Bethe

Para scanning desorption:

\[
y
=
(1-q)+q(1-Q_+)y^{z-1},
\]

\[
Q_-
=
1-(1-Q_+)y^z.
\]

Sea:

\[
S
=
1-q(1-Q_+)(z-1)y^{z-2}>0
\]

la condición de rama estable.

Por diferenciación implícita:

\[
\frac{dy}{dQ_+}
=
-\frac{q y^{z-1}}{S}
\le0.
\]

Por tanto:

\[
\frac{dQ_-}{dQ_+}
=
y^z
-(1-Q_+)zy^{z-1}\frac{dy}{dQ_+}
\ge0,
\]

con desigualdad estricta en el interior no degenerado.

Luego el Bethe scan preserva el orden de estados iniciales.

Para scans simples que parten de la primary adsorption branch:

- mayor presión de reversión ​\(\Rightarrow\) estado más lleno;
- a presión común durante desorción ​\(\Rightarrow\) adsorción no menor.

Esta predicción es reference‑free y puede evaluarse directamente en ​\(V\), porque el mapa ​\(Q\mapsto V\) es afín y monótono.

---

## 5. Frontera de claim

HG40 puede producir:

- identificabilidad relativa;
- invariantes de training;
- no‑passing y orden cross‑history;
- tests de nulls estándar en el cociente.

No puede producir por sí solo:

- identificabilidad absoluta;
- el denominador físico completo de HG31;
- exclusión integral de network/percolation;
- evidencia de protogeometría física.

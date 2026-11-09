# HGMF‑HG23 — No-go: transversalidad no es interacción causal

Sea \(M\) un espacio de contextos con coordenadas \((v,h)\). Tome

\[
a_V=v,\qquad b_H=h.
\]

Entonces

\[
*(da_V\wedge db_H)=1.
\]

Considere un outcome aditivo:

\[
m(v,h)=m_V(v)+m_H(h).
\]

Para cualesquiera niveles \(v_0,v_1,h_0,h_1\):

\[
I_{VH}
=m(v_1,h_1)-m(v_1,h_0)-m(v_0,h_1)+m(v_0,h_0)=0.
\]

Por tanto, una fuente diagonal no nula puede coexistir con ausencia exacta de interacción causal.

## Clasificación autorizada

- `GEOMETRIC_TRANSVERSALITY_ONLY`: \(s_D\neq0\), contraste causal nulo.
- `CAUSAL_INTERACTION_ONLY`: contraste causal no nulo, fuente geométrica degenerada o no definida.
- `COLOCATED_TRIAXIAL_INTERACTION`: ambos pasan future-only y co-localizan.
- `ABSTAIN_CAUSAL_IDENTIFICATION`: intervenciones/confounding insuficientes.

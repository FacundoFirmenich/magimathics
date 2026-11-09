# HGMF‑HG24 — Teorema de independencia causal–geométrica

La fuente geométrica

\[
s_D=*(da_V\wedge db_H)
\]

y la interacción causal aditiva

\[
I_{VH}=m_{11}-m_{10}-m_{01}+m_{00}
\]

son lógicamente independientes.

## Testigos exactos

- Geometría sin causalidad:
  \(a_V=v\), \(b_H=h\), \(m(v,h)=v^2+\sin h\); entonces \(s_D=1\), \(I_{VH}=0\).
- Causalidad sin geometría:
  \(a_V=v\), \(b_H=v\), \(m(v,h)=vh\); entonces \(s_D=0\), \(I_{VH}=1\).
- Ambos:
  \(a_V=v\), \(b_H=h\), \(m(v,h)=vh\); entonces \(s_D=1\), \(I_{VH}=1\).
- Ninguno:
  \(a_V=v\), \(b_H=v\), \(m(v,h)=v^2+h^2\); entonces \(s_D=0\), \(I_{VH}=0\).

## Corolario

Ningún threshold sobre \(s_D\) identifica interacción causal sin un estimando de intervención independiente.

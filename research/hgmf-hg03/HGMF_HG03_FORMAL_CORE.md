# HGMF‑HG03 — Núcleo formal

## Posibilidad inducida por proyección

\[
\Gamma_{C,O}(c)=\{O(Fp):C(p)=c\}.
\]

## Identidad transicional

\[
|\Gamma_{C,O}(c)|=1\quad\forall c
\iff
\exists\bar F:\ O\circ F=\bar F\circ C.
\]

## Kernel con medida declarada

\[
K_{\rho}(c,o)
=
\rho(O(FP)=o\mid C(P)=c).
\]

## Teorema de independencia de medida

Si se permiten todas las distribuciones condicionales sobre cada fibra, \(K_\rho\) es independiente de \(\rho\) si y sólo si \(\Gamma_{C,O}(c)\) es singleton para toda fibra.

## Filtro de fibra

\[
\pi_t(p)=\Pr(P_t=p\mid G_{0:t}).
\]

\[
\Pr(G_{t+1}=h\mid G_{0:t})
=
\sum_{p\in\Phi^{-1}(G_t)}
\pi_t(p)\mathbf1_{\{\Phi(Fp)=h\}}.
\]

La memoria observada reside en la evolución del posterior sobre la fibra residual.

## Lumpability determinista

Para la matriz \(M_{p,q}=\mathbf1_{q=F(p)}\), la condición fuerte de lumpability es equivalente a

\[
\Phi(p)=\Phi(p')
\Rightarrow
\Phi(Fp)=\Phi(Fp').
\]

## Decodependencia

\[
\mathcal D_\rho(C;O)=H_\rho(O(FP)\mid C(P)).
\]

Si \(C'\) refina \(C\):

\[
\mathcal D_\rho(C';O)\le\mathcal D_\rho(C;O).
\]

Si \(O'\) refina \(O\):

\[
\mathcal D_\rho(C;O')\ge\mathcal D_\rho(C;O).
\]

## Markovidad relativa

El proceso observado es Markov de primer orden bajo una ley inicial concreta si todos los historiales alcanzables con el mismo estado observado inducen la misma distribución pushforward del posterior de fibra. Strong lumpability exige la propiedad para toda ley inicial.

# HGMF‑HG03 — Fibras residuales, decodependencia y probabilidad inducida por el observador

**Fecha:** 8 de noviembre de 2026  
**Autoridad:** `FORMAL / FINITE WITNESS / MEASURE-EXPLICIT`  
**Veredicto:** `PASS_OBSERVER-INDUCED POSSIBILITY / PASS PROBABILITY WITH DECLARED MEASURE / FAIL MEASURE INDEPENDENCE`

## Resultado rector

Para una dinámica oculta determinista

\[
F:\mathcal P\to\mathcal P
\]

y una observación

\[
\Phi:\mathcal P\to\mathcal G,
\]

el objeto primario libre de medida es

\[
\Gamma_\Phi(g)=\{\Phi(F(p)):\Phi(p)=g\}.
\]

Si cada \(\Gamma_\Phi(g)\) es singleton, existe una transición exacta

\[
\Phi\circ F=\bar F\circ\Phi.
\]

Si no es singleton, la proyección sólo determina posibilidades. Una probabilidad exige una medida condicional \(\mu_g\) sobre la fibra:

\[
K_\mu(g,h)=\mu_g\{p:\Phi(F(p))=h\}.
\]

## Teorema de identidad transicional

En dinámica determinista finita son equivalentes:

1. \(\Phi\circ F\) es constante en cada fibra;
2. existe \(\bar F\) con \(\Phi F=\bar F\Phi\);
3. el kernel inducido es independiente de toda medida condicional de fibra;
4. el proceso observado es determinista de primer orden para toda distribución inicial;
5. la matriz determinista oculta es fuertemente lumpable respecto de \(\Phi\).

## Testigo exacto

El modelo usa 16 estados \((g,o,n,z)\in\{0,1\}^4\). La observación saturada \(S=(g,o,n)\) deja fibras residuales de tamaño dos.

Una dinámica independiente de \(z\) conserva fibras ocultas y, aun así, induce una transición exacta: la ignorancia del hidden state no implica probabilidad.

En la dinámica ramificada

\[
g_{t+1}=g_t\oplus z,\quad o_{t+1}=o_t,\quad n_{t+1}=n_t,\quad z_{t+1}=z_t,
\]

cada macroestado tiene dos sucesores posibles. Bajo medida uniforme, ambos reciben probabilidad \(1/2\). Bajo \(\Pr(z=0\mid S)=\alpha\), las probabilidades son \(\alpha\) y \(1-\alpha\). Incluso la invariancia dinámica deja una familia convexa de medidas invariantes.

## Memoria proyectada

\[
H(S_{t+1}\mid S_t)=1\text{ bit},
\qquad
H(S_{t+1}\mid S_{t-1},S_t)=0.
\]

Por tanto:

\[
I(S_{t+1};S_{t-1}\mid S_t)=1\text{ bit}.
\]

El proceso observado es determinista de orden dos. La historia reconstruye el bit latente.

## Decodependencia bivariante

Para contexto actual \(C\) y resolución futura \(O\):

\[
\mathcal R(C,O)=\{(p,p'):C(p)=C(p'),\ O(Fp)\ne O(Fp')\}.
\]

- refinar \(C\), con \(O\) fijo, reduce la ambigüedad;
- refinar \(O\), con \(C\) fijo, puede revelar divergencias nuevas.

La decodependencia tiene dos ejes con monotonicidades opuestas.

## Perfil de hiperacceso

| Contexto | Entropía oculta | Entropía sucesora | Pares discordantes |
|---|---:|---:|---:|
| ninguno | 4 | 3 | 112 |
| G | 3 | 3 | 56 |
| GO | 2 | 2 | 24 |
| GON | 1 | 1 | 8 |
| GONP | 1 | 1 | 8 |
| GONPZ | 0 | 0 | 0 |

El contexto redundante P no reduce el residuo. El metacontexto Z convierte el kernel probabilístico en identidad transicional.

## Claim boundary

HG03 demuestra posibilidad multivaluada, probabilidad dependiente de medida, memoria inducida, no-Markovidad y desaparición de incertidumbre por hiperacceso.

No demuestra Born, una medida única, estructura de Hilbert, spin, colapso físico ni una microdinámica pregeométrica real.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `OBSERVER_INDUCED_PROBABILITY_FORMAL_PASS / MEASURE_SELECTION_PENDING`.

## Next gate

`HGMF‑HG04 — Selección no circular de medida en fibras residuales`.

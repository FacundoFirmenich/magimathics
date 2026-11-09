# HGMF‑HG19 — Métrica operacional de contexto, coste de acción y acoplamiento dimensional

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / EXACT WITNESS / OPERATIONAL ACTION / MIXED-STATE PURIFICATION`

## Veredicto vinculante

```text
PASS_OPERATIONAL_CONTEXT_METRIC_CONDITIONAL
PASS_PURE_STATE_ACTION_METRIC_THEOREM
PASS_STANDARD_ACTION_TRANSGRESSION
PASS_BURES_ACTION_METRIC_CONDITIONAL
PASS_ACCESSIBLE_CROSS_CARRIER_TRANSPORT
PASS_HIDDEN_ANCILLA_BOUNDARY
PASS_FORMAL_FUTURE_ONLY_HOLDOUT

FAIL_UNCONDITIONAL_CONTROL_COST_UNIQUENESS
FAIL_UNCONDITIONAL_MIXED_STATE_METRIC_UNIQUENESS
FAIL_NONZERO_HGMF_COUPLING_SELECTION
FAIL_STANDARD_GEOMETRY_EXCLUSION

HOLD_PHYSICAL_PROTOGEOMETRY
```

La conclusión principal es doble:

\[
\boxed{h^{\rm act}_{ij}=\hbar^2 g^{Q}_{ij}}
\]

selecciona una métrica operacional con unidades de acción al cuadrado, pero

\[
\boxed{\lambda_{\rm HG}=c_{\rm HG}/\hbar^2}
\]

continúa conteniendo un coeficiente adimensional no determinado. HG19 cierra las unidades; no cierra una nueva constante física.

## 1. Métrica de acción pura

Sea una familia normalizada de estados puros y sea \(G_i\) un generador hermitiano local:

\[
\partial_i|\psi\rangle=-\frac{i}{\hbar}G_i|\psi\rangle.
\]

El tensor geométrico cuántico se escribe como covarianza no simetrizada:

\[
Q_{ij}=\frac{1}{\hbar^2}\langle\Delta G_i\Delta G_j\rangle.
\]

Por tanto:

\[
g^Q_{ij}=\frac{1}{2\hbar^2}\langle\{\Delta G_i,\Delta G_j\}\rangle,
\qquad
\mathcal F_{ij}=\frac{1}{i\hbar^2}\langle[G_i,G_j]\rangle.
\]

Para el generador horizontal mínimo

\[
G_i^{\min}=i\hbar\left(|\eta_i\rangle\langle\psi|-|\psi\rangle\langle\eta_i|\right),
\qquad
|\eta_i\rangle=(I-P)|\partial_i\psi\rangle,
\]

se define

\[
\boxed{
h^{\rm act}_{ij}=\frac14\operatorname{Tr}\{G_i^{\min},G_j^{\min}\}=\hbar^2g^Q_{ij}.
}
\]

La misma cantidad se obtiene como covarianza del generador sobre el estado:

\[
h^{\rm act}_{ij}=\frac12\langle\{\Delta G_i,\Delta G_j\}\rangle.
\]

Así:

\[
ds_{\rm act}^2=h^{\rm act}_{ij}d\lambda^id\lambda^j,
\qquad
\boxed{ds_{\rm act}=\hbar ds_Q}.
\]

A lo largo de una trayectoria temporal:

\[
ds_{\rm act}=\Delta H\,dt.
\]

En 99 puntos de la esfera de Bloch, con \(\hbar=2.3\) como unidad de auditoría, los errores máximos fueron \(1.11\times10^{-15}\) para el generador mínimo, \(1.33\times10^{-15}\) para la covarianza y \(2.50\times10^{-16}\) para la invariancia gauge del QGT.

## 2. Coste intrínseco frente a coste instrumental

Todo generador que realiza el mismo tangent proyectivo puede escribirse como

\[
G_i=G_i^{\min}+c_iI+K_i,
\qquad K_i|\psi\rangle=0.
\]

Los términos adicionales no cambian la covarianza sobre el estado, pero sí cambian la norma Hilbert–Schmidt total, \(\langle G_i^2\rangle\) y el coste del actuador.

\[
\boxed{\text{coste de cambio de estado}\neq\text{coste total del actuador}.}
\]

## 3. Área de acción y transgresión estándar

En dos dimensiones:

\[
\boxed{dA_{\rm act}=\hbar^2dA_Q.}
\]

Como

\[
\mathcal F=2\chi_QdA_Q,
\]

se obtiene

\[
\boxed{\mathcal F=\frac{2\chi_Q}{\hbar^2}dA_{\rm act}.}
\]

Para una superficie pura saturada:

\[
\chi_Q=\pm1,
\qquad
\lambda_{\rm std}=\pm2/\hbar^2.
\]

Una corrección HGMF residual tendría la forma

\[
\delta\mathcal F=\frac{c_{\rm HG}}{\hbar^2}dA_{\rm act},
\]

pero HG19 no selecciona \(c_{\rm HG}\neq0\), su signo, su dependencia contextual ni una ley de escala.

## 4. Mixed states

La monotonicidad frente a canales no selecciona una métrica única. En el testigo \(\rho=\operatorname{diag}(0.8,0.2)\), las métricas Petz normalizadas producen:

| Métrica | Valor | Razón frente a SLD |
|---|---:|---:|
| SLD | 0.360000 | 1.000000 |
| Wigner–Yanase | 0.400000 | 1.111111 |
| BKM | 0.415888 | 1.155245 |

Si se añade el principio de mínima acción coherente entre purificaciones, Uhlmann selecciona condicionalmente:

\[
\boxed{h_B=\hbar^2g_B=\inf_{\Psi\mapsto\rho}\hbar^2g_{FS}.}
\]

## 5. Contracción y accesibilidad

Para una familia equatorial depolarizada:

\[
g_B^{\phi\phi}=r^2/4.
\]

La auditoría obtiene error máximo \(1.39\times10^{-16}\).

Un embedding constante qubit→qutrit preserva exactamente QGT y métrica de acción. En cambio, una ancilla oculta dependiente de \(\theta\) cambia el área pura total por un factor \(\sqrt5\) y lleva \(\chi:1\mapsto1/\sqrt5\), mientras el estado reducido accesible y su métrica Bures permanecen iguales.

Por tanto, el transporte transcarrier debe fijar el álgebra accesible, no una purificación arbitraria.

## 6. Holdout formal

El factor \(h=\alpha g\) se congeló con 40 puntos analíticos:

\[
\widehat\alpha=5.29=\hbar^2.
\]

En los puntos retenidos, el error relativo máximo fue \(1.13\times10^{-14}\). Es una validación formal, no empírica.

## 7. Frontera científica

QGT como covarianza de generadores, Fubini–Study, Berry curvature, Bures, la familia Petz, speed limits y purificación mínima pertenecen a la ciencia establecida. HG19 integra esos elementos con la arquitectura UMI/HGMF, cierra la unidad de acción y localiza la deuda restante en un coeficiente adimensional transcarrier.

## 8. Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `OPERATIONAL ACTION METRIC + STANDARD DIMENSIONAL TRANSGRESSION PASS; HGMF COUPLING + STANDARD EXCLUSION FAIL/HOLD`.

## 9. Próxima frontera

`HGMF‑HG20 — Selección del acoplamiento adimensional y tribunal residual transcarrier`.

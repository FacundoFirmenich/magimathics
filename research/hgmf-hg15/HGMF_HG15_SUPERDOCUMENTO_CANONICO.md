# HGMF‑HG15 — Dinámica relacional de reloj y falsabilidad protogeométrica

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / CLOCK-SYSTEM / CHARACTERISTIC-FUNCTION / DILATION`  
**Veredicto:** `PASS_RELATIONAL_CLOCK_DYNAMICS / PASS MULTIGAP FALSIFIER / FAIL HGMF CORRECTION DERIVATION / FAIL DISTINGUISHABILITY FROM STANDARD QM`

## 0. Veredicto

```text
PASS_RELATIONAL_CLOCK_DYNAMICS
PASS_CLOCK_GAUGE_QUOTIENT
PASS_CLOCK_REPARAMETRIZATION_THEOREM
PASS_SINGLE_GAP_NONIDENTIFIABILITY
PASS_MULTI_GAP_SCALAR_TIME_FALSIFIER
PASS_STANDARD_QM_DILATION_BOUNDARY
PASS_EXPERIMENTAL_FALSIFIER_BASIS

FAIL_NONZERO_HGMF_CORRECTION_DERIVATION
FAIL_SCALE_IDENTIFICATION
FAIL_DISTINGUISHABILITY_FROM_STANDARD_QM

HOLD_PHYSICAL_PROTOGEOMETRY
```

## 1. Reloj relacional

El estado reloj–sistema se condiciona sobre un POVM físico del reloj. En el límite covariante ideal recupera la dinámica de Schrödinger. Relojes interactuantes y no ideales ya pueden producir dinámica condicional temporalmente no local, no unitaria o con memoria dentro de la mecánica cuántica estándar.

## 2. Cociente exacto

Para

\[
i\hbar\partial_\tau\psi=
\left[a(\tau)H_0+b(\tau)I\right]\psi,
\]

una recalibración del reloj y un gauge de fase reducen exactamente la ecuación a

\[
i\hbar\partial_s\widetilde\psi=H_0\widetilde\psi.
\]

HG15 verificó el cociente con error vectorial máximo

\[
8.474e-16.
\]

Estas correcciones no constituyen física nueva.

## 3. No-go monogap

Todo contraste complejo \(c\), con \(|c|\le1\), posee una representación mediante smearing de dos tiempos. En 256 construcciones exactas, el error máximo de reconstrucción fue

\[
4.536e-16.
\]

Por tanto, una transición, una fase y una visibilidad nunca bastan para identificar HGMF.

## 4. Teorema multigap

Una distribución escalar de tiempo relacional genera una única función característica para todos los gaps energéticos. En niveles equiespaciados, la matriz de coherencias es Toeplitz y positiva semidefinida.

El testigo exacto de tiempo escalar posee autovalor mínimo

\[
-2.851e-16,
\]

que es cero dentro del error numérico.

Un canal de dephasing distinto y físicamente válido posee autovalor mínimo

\[
0.198623,
\]

pero factores de coherencia 0.8 y 0.44 para gaps adyacentes iguales, con defecto

\[
\boxed{0.36}.
\]

Esto falsifica el smearing temporal escalar, pero sigue siendo dephasing cuántico estándar.

## 5. No-go de dilatación

El testigo de amplitude damping fue reconstruido mediante una dilatación unitaria con error máximo de canal

\[
0.000e+00.
\]

Toda anomalía reducida CPTP puede representarse, por tanto, dentro de QM estándar sobre un sistema ampliado. La atribución requiere una clase nuisance congelada y una ley de escala nueva.

## 6. Jerarquía de falsadores

El primer programa decisivo no es una fase interferométrica aislada. Requiere:

1. controles de gauge y recalibración;
2. espectroscopia multigap;
3. sustitución del reloj;
4. protocolos forward/reverse y echo;
5. cambios de orden con endpoints emparejados;
6. covariancia entre temporal quantum reference frames;
7. tomografía de entorno o process tensor;
8. una ley dimensional de escala preregistrada.

## 7. Adjudicación de escala

No se derivó ninguna constante de acoplamiento, energía, tiempo o longitud HGMF. Por tanto:

```text
EXPERIMENTAL MAGNITUDE = ABSTAIN
```

## 8. Cierre científico

HG15 cierra la lógica experimental, no la extensión física. Los experimentos actuales con relojes cuánticos pueden sondear efectos de proper time cuántico dentro de QM estándar. Un claim HGMF deberá predecir un patrón residual que sobreviva esas explicaciones.

## 9. Portfolio

- **Paper A:** experiment-ready bajo UMI‑17.
- **Paper B:** núcleo formal sustancialmente completo; claim multifractal empírico en abstención.
- **Paper C:** dinámica relacional de reloj y base de falsadores en `PASS`; corrección física y escala en `HOLD`.

## 10. Próximo gate

`HGMF‑HG16 — Base de correcciones protogeométricas y espectroscopia multigap`.
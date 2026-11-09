# HGMF‑HG20 — Selección del acoplamiento adimensional y tribunal residual transcarrier

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / COMPOSITION / CHERN–WEIL / CROSS-CARRIER HOLDOUT`

## Veredicto vinculante

```text
PASS_SAME-BUNDLE_ZERO-FLUX_THEOREM
PASS_MONOIDAL_COMPOSITION_NO-GO
PASS_TOPOLOGICAL_NORMALIZATION
PASS_CROSS-CARRIER_ZERO-COUPLING_THEOREM
PASS_MEAN-ZERO_RESIDUAL_CLASS
PASS_FORMAL_FUTURE-ONLY_HOLDOUT

FAIL_NONZERO_UNIVERSAL_LOCAL_AREA_COUPLING
FAIL_MIXED-STATE_METRIC_INDEPENDENCE
FAIL_HISTORICAL_CONSTANT_SELECTION
FAIL_STANDARD_GEOMETRY_EXCLUSION

HOLD_PHYSICAL_PROTOGEOMETRY
```

## 0. Resultado rector

El ansatz mínimo heredado de HG19,

\[
\delta\mathcal F
=
\frac{c_{\rm HG}}{\hbar^2}dA_{\rm act}
=
c_{\rm HG}dA_Q,
\]

no admite un coeficiente universal no nulo si se exige cualquiera de estas tres condiciones fuertes:

1. misma topología de line bundle sobre una superficie cerrada;
2. composición aditiva de sistemas producto independientes;
3. universalidad entre carriers con volúmenes cuánticos incommensurables.

En los tres tribunales:

\[
\boxed{c_{\rm HG}=0.}
\]

El resultado no elimina toda corrección HGMF. Elimina una clase concreta: local, constante, de signo fijo, puramente proporcional al área y universal.

## 1. Mismo bundle

La diferencia de curvaturas de dos conexiones sobre el mismo line bundle es exacta:

\[
\delta\mathcal F=d\alpha.
\]

En una superficie cerrada:

\[
\int_M\delta\mathcal F=0.
\]

Como \(dA_Q>0\):

\[
\int_M c\,dA_Q=cV_Q=0
\Rightarrow c=0.
\]

## 2. Composición

Para estados producto:

\[
Q_{AB}=Q_A+Q_B,
\qquad
\mathcal F_{AB}=\mathcal F_A+\mathcal F_B.
\]

Pero el área métrica no es lineal. El testigo

\[
g_A=\operatorname{diag}(1,4),
\quad
g_B=\operatorname{diag}(4,1)
\]

da:

\[
A_A=2,\quad A_B=2,\quad A_{AB}=5.
\]

La ley universal predice \(5c\) para el compuesto; la aditividad independiente predice \(4c\). Luego \(c=0\).

## 3. Topología y cross-carrier

Si se permite cambiar el Chern number:

\[
\Delta C_1=\frac{cV_Q}{2\pi}\in\mathbb Z.
\]

- esfera de Bloch: \(V_Q=\pi\Rightarrow c/2\in\mathbb Z\);
- carrier hidden-ancilla de HG18: \(V_Q=\pi\sqrt5\Rightarrow c\sqrt5/2\in\mathbb Z\).

No existe solución común no nula.

## 4. Holdout formal

Calibrar \(\Delta C_1=1\) en la esfera de Bloch fija \(c=2\). El carrier retenido predice:

\[
\Delta C_1=\sqrt5,
\]

no entero.

Calibrar en el carrier hidden-ancilla fija \(c=2/\sqrt5\). La esfera retenida predice:

\[
\Delta C_1=1/\sqrt5.
\]

Ambos holdouts fallan.

## 5. Mixed-state boundary

El mismo residual produce distintos \(c\) bajo SLD, Wigner–Yanase y BKM. Sin una métrica preregistrada, el coeficiente es representation-dependent. Seleccionar Bures condicionalmente no evita los no-go globales.

## 6. Constantes históricas

\(\pi/6\), \(\pi/18\), \(4\pi/9\) y \(4\sqrt\pi/3\) no satisfacen la integrality del ansatz sobre la esfera de Bloch. No quedan refutadas en otros roles; quedan excluidas como este coeficiente concreto.

## 7. Clase sobreviviente

Sobre el mismo bundle:

\[
\delta\mathcal F=f\,dA_Q,
\qquad
\int_M f\,dA_Q=0.
\]

El modo constante queda eliminado. Sobreviven:

- perfiles sign-changing;
- formas exactas de flujo cero;
- kernels no locales;
- términos interaction-dependent;
- cambios topológicos discretos con datos adicionales.

## 8. Portfolio

- **Paper A:** `EXPERIMENT_READY_UMI17_UNCHANGED`.
- **Paper B:** `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- **Paper C:** `UNIVERSAL LOCAL AREA COUPLING NONZERO RULED OUT; ZERO-FLUX/NONLOCAL FRONTIER OPEN`.

## 9. Próxima frontera

`HGMF‑HG21 — Campos residuales de flujo cero, modos de Hodge y acoplamiento no local`.

# HGMF‑HG02 — Tomografía protogeométrica multicontexto y saturación observacional

**Veredicto:** `PASS_PROTO_TOMOGRAPHY_THEOREM / PASS_OBSERVATIONAL_SATURATION / FAIL_FULL_IDENTIFIABILITY`

## Resultado rector

\[
\Phi_A(P)=\left(\Phi_\lambda(P)\right)_{\lambda\in A},
\qquad
\ker\Phi_A=\bigcap_{\lambda\in A}\sim_\lambda.
\]

Por tanto:

\[
\Phi_A\text{ es inyectiva}
\iff
\bigcap_{\lambda\in A}\sim_\lambda=\Delta_{\mathcal P}.
\]

La tomografía multicontexto no consiste en acumular datos indiferenciados, sino en refinar particiones hasta separar las diferencias pertinentes.

## Saturación e hiperacceso

En el modelo testigo exacto existen 16 estados protogeométricos y cuatro contextos admisibles `G,O,N,P`.

- cualquier tres de los cuatro alcanzan saturación;
- la cuarta sonda admisible aporta ganancia marginal cero;
- la saturación contiene 8 clases de tamaño 2;
- persiste un bit latente `z` por clase;
- la identificación completa exige un metacontexto adicional `Z`.

El perfil de hiperacceso es:

| Contextos | Clases | Peor fibra | Pares separados |
|---|---:|---:|---:|
| ninguno | 1 | 16 | 0 |
| G | 2 | 8 | 64 |
| G,O | 4 | 4 | 96 |
| G,O,N | 8 | 2 | 112 |
| G,O,N,P | 8 | 2 | 112 |
| G,O,N,P,Z | 16 | 1 | 120 |

La función de pares separados es monótona y submodular.

## Proto-certidumbre

Una propiedad puede ser exacta sin que el código completo esté identificado. En el testigo, el contexto de paridad determina exactamente

\[
g\oplus o\oplus n
\]

mientras deja una fibra de ocho estados.

```text
EXACT_TRANSITION_PROPERTY != FULL_PROTO_IDENTIFICATION
```

## Claim boundary

HG02 no deriva ni postula Born, spin, probabilidad cuántica, una microdinámica pregeométrica ni las constantes especiales del programa.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `PROTO_TOMOGRAPHY_FORMAL_PASS / PHYSICAL_CONTEXT_SET_HOLD`.

## Next gate

`HGMF‑HG03 — Residual Fibres, Decodependence and Observer‑Induced Probability`.

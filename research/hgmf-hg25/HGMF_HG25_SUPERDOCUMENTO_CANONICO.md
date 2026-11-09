# HGMF‑HG25 — Espectroscopia causal modal y ejecución dual-carrier: cierre de ejecutabilidad

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `EXACT EXECUTION AUDIT / NO-IMPUTATION / PROSPECTIVE DESIGN`

## Veredicto

```text
PASS_EXECUTION_AVAILABILITY_AUDIT
PASS_GRID_AND_RECTANGLE_THEOREMS
PASS_MODAL_RANK_CONTRACT
PASS_PRECISION_AND_HOLDOUT_CONTRACT
PASS_ANALYSIS_FREEZE

FAIL_CURRENT_CORPUS_IDENTIFIABILITY
ABSTAIN_INSUFFICIENT_EXECUTION
HOLD_PHYSICAL_PROTOGEOMETRY
```

## 1. Resultado principal

HG25 fue concebido como primer cierre empírico de HG23–HG24. La auditoría de las ramas vigentes demuestra que los datos requeridos no han sido ejecutados.

La salida correcta no es reemplazarlos por una simulación, una imputación o una extensión retrospectiva del corpus público. Es:

\[
\boxed{\texttt{ABSTAIN\_INSUFFICIENT\_EXECUTION}.}
\]

## 2. Datos existentes frente a datos requeridos

El corpus público previo conserva cuatro loops magnéticos de una reversión y cuatro runs de adsorción. No implementa el grid crossed de HG25.

UMI‑17 conserva un diseño robusto de 99 loop blocks y declara explícitamente `HOLD_EXPERIMENTAL_EXECUTION`.

El diseño HG25 exige un grid magnético:

\[
3\times8\times3=72
\]

y un segundo carrier homólogo de 72 runs.

## 3. Corrección del número 18

Los 18 loops son un **incremento condicional**:

\[
\text{UMI17+UMI22 ejecutados}
\Longrightarrow
54/72\text{ loops disponibles}
\Longrightarrow
18\text{ loops faltantes}.
\]

Sin receipts de los dos programas previos, no puede afirmarse que sólo falten 18. El backlog certificado del grid HG25 es 72.

## 4. Rectángulos causales

Un grid completo produce:

\[
42
\]

rectángulos adyacentes por componente.

El programa condicional UMI17+22 produciría 24, y los 18 loops finales desbloquearían los 18 restantes.

En el estado certificado actual:

\[
0/42
\]

rectángulos pertenecen al target grid ejecutado.

## 5. Modalidad

Los kernels de dos parámetros totales pueden interpolarse con dos modos y, por eso mismo, no quedar falsados. El primer tribunal útil usa tres modos de training. La recomendación robusta es:

\[
3\text{ training}+2\text{ holdout}.
\]

Deben cumplirse:

- source support;
- distinct eigenvalues;
- full-rank training Jacobian;
- no refit;
- componentwise scoring.

## 6. Precisión

Con incertidumbre igual \(\sigma^2\) por celda:

\[
SE(\bar I)=2\sigma/\sqrt W.
\]

Tres waves no garantizan detección de interacciones pequeñas. La validez depende de conservar la incertidumbre de los componentes extraídos del trace y de predefinir el error model.

## 7. Estado de los gates

| Gate | Resultado |
|---|---|
| Magnetic completion | `ABSTAIN_NOT_EXECUTED` |
| Causal rectangles | `ABSTAIN_NO_TARGET_GRID` |
| Modal training | `PASS_DESIGN / ABSTAIN_DATA` |
| Wave-3 holdout | `PASS_CONTRACT / ABSTAIN_DATA` |
| Second carrier | `ABSTAIN_NOT_EXECUTED` |
| Carrier transfer | `PASS_CONTRACT / ABSTAIN_DATA` |
| Attribution | `PASS_NUISANCE_CONTRACT / ABSTAIN_DATA` |

## 8. Estado coordinado

- **Paper A:** design complete, execution pending.
- **Paper B:** unchanged except for a sharper execution/transport boundary.
- **Paper C:** formal empirical architecture complete; no empirical causal-modal result.

## 9. Próximo gate

`HGMF‑HG26 — Receipts de adquisición y primera adjudicación empírica dual-carrier`.

# HGMF‑HG27 — Núcleo formal

## 1. Objetos de adquisición

El target dual-carrier contiene:

\[
72\text{ loops magnéticos}+72\text{ runs de adsorción}.
\]

Las waves 1–2 son training y la wave 3 es holdout.

## 2. Orden de adquisición

Dentro de cada wave, la adquisición debe ser prefix-closed. El schedule canónico es Pareto-óptimo: máxima disponibilidad temprana de rectángulos con el mínimo número de cambios de eje compatible con esa utilidad.

## 3. Interacción simétrica y orden

El grid base identifica

\[
I_{VH}=m_{11}-m_{10}-m_{01}+m_{00}.
\]

No identifica por sí solo

\[
I_{\rm ord}=\tfrac12(I_{H\circ V}-I_{V\circ H}).
\]

Sin ambos joint-order outcomes, el commutator queda en `ABSTAIN`.

## 4. Reestimación ciega

Para varianza por celda \(\sigma_j^2\) y \(W\) waves/replicates independientes:

\[
SE(\bar I_j)=2\sigma_j/\sqrt W.
\]

Para half-width \(h_j\):

\[
W_{\rm req,j}=\left\lceil(2z_{1-\alpha_j/2}\widehat\sigma_j/h_j)^2\right\rceil.
\]

Para potencia sobre \(\Delta_j^\star\):

\[
W_{\rm req,j}=\left\lceil\left[2(z_{1-\alpha_j/2}+z_{1-\beta_j})\widehat\sigma_j/\Delta_j^\star\right]^2\right\rceil.
\]

Sólo se permiten nuisance/uncertainty summaries cegados al efecto.

## 5. Stopping

- QC/safety: anytime.
- Precision futility: tras wave 1.
- Structural futility: tras waves 1–2.
- Early success: prohibido.
- Final: one-shot después de wave 3 en ambos carriers.

## 6. Optional stopping

El modo canónico evita inspección de efectos antes del holdout y no gasta alpha durante adquisición. Cualquier monitoring de efectos exige migrar explícitamente a confidence sequences, e-processes o un design group-sequential.

## 7. Evidence budget

\[
\mathbf B=(B_{grid},B_{order},B_{precision},B_{nuisance},B_{transfer}).
\]

\[
B_{grid}=144.
\]

Los restantes términos requieren thresholds y restricciones físicas preregistradas.

## 8. Frontera

HG27 selecciona plan y reglas de parada. No ejecuta datos, no selecciona kernel físico y no identifica protogeometría.

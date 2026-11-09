# HGMF‑HG37 — Formal core

## 1. Calibration-observability theorem

Let the observable law be indexed by target parameter \(\theta\) and unobserved calibration nuisance \(\eta\):

\[
P_{Y\mid\theta,\eta}.
\]

Define the observable images:

\[
\Pi(H_0)=\{P_{Y\mid\theta,\eta}:\theta\in H_0,\eta\in\mathcal E\},
\]

\[
\Pi(H_1)=\{P_{Y\mid\theta,\eta}:\theta\in H_1,\eta\in\mathcal E\}.
\]

If

\[
P^\star\in\Pi(H_0)\cap\Pi(H_1),
\]

then no test based only on \(Y\) can distinguish \(H_0\) and \(H_1\) at \(P^\star\) with nontrivial uniform power while controlling type-I error.

An auxiliary calibration measurement \(Z\) can restore identifiability only if the joint image

\[
\Pi_{Y,Z}(H_0)
\]

no longer overlaps the relevant alternative image.

Thus missing calibration is an observation-fibre problem, not merely a larger standard error.

## 2. Magnetic rescue threshold theorem

For trained loops \(n=2,\ldots,5\):

\[
h_n^{obs}=\mu_n+\delta_n+\varepsilon_n,
\qquad |\delta_n|\le\Delta_H.
\]

Under the trained zero-bias null:

\[
\mu_n=0.
\]

Ignoring the already quantified small \(\varepsilon_n\) for set-membership, the vector null can reproduce the observed trained vector iff

\[
\|h^{obs}_{2:5}\|_\infty\le\Delta_H.
\]

Therefore the global null ceases to saturate exactly when

\[
\boxed{\Delta_H < \|h^{obs}_{2:5}\|_\infty}.
\]

For HG36 values:

\[
\|h\|_\infty=4.0754321208\ \mathrm{mT}.
\]

For all four trained loops to be individually nonabsorbable:

\[
\boxed{\Delta_H<\min_n |h_n|=0.8838269371\ \mathrm{mT}}.
\]

The current source field-step bound is 4.2932274337 mT.

## 3. Gaussian \(E=140\) heuristic boundary

This is diagnostic only, because bootstrap normality is not exact confirmatory authority.

For one loop with Gaussian scale \(\sigma\), a residual \(r\) contributes

\[
\log LR=\frac{r^2}{2\sigma^2}.
\]

Requiring

\[
\log LR\ge\log 140
\]

gives

\[
r\ge\sigma\sqrt{2\log 140}.
\]

For the controlling loop, HG37 obtains a heuristic field-nuisance bound near 4.055711429 mT.

This is **not** promoted to a confirmatory threshold.

## 4. Vycor rescue boundary

Cimino-type observation mapping requires an external film reference \(V_s\).

Brown/NIST does not contain that object. Therefore that particular observation map is not point-identifiable from the Brown corpus alone.

Mason (1988) supplies a different standard network route applied to the same Brown Xe/Vycor benchmark and explicitly avoids requiring prior separation of surface adsorption from capillary condensation.

Hence

\[
\text{Cimino bridge not identified}
\not\Rightarrow
\text{standard network physics excluded}.
\]

## 5. Historical-route conclusion

Current public data cannot produce a complete confirmatory standard-null denominator for HG31.

This blocks both:

- rejection of the full standard envelope;
- any physical HGMF attribution.

The correct action is a prospective pivot.

# HGMF‑HG41 — Maximal-invariant likelihoods and quotient-space universal e-values

## Objective

Convert the reference-free invariants of HG40 into statistically calibrated likelihoods/e-values without reintroducing the eliminated affine nuisance.

## Gate A — quotient observation measure

Define the measurable space and Jacobian for labelled affine coordinates:

\[
\rho_i=(Y_i-Y_r)/(Y_s-Y_r).
\]

Handle anchor degeneracy and label-preserving branch selection fail-closed.

## Gate B — magnetic maximal-invariant model

Construct a distribution on:

- affine HEB coordinates;
- normalized loop-to-trained contrast;
- branch-width ratios;
- transition-asymmetry coordinates.

Model the shared field calibration only through the quotient action. Do not assign independent offsets after quotienting.

## Gate C — adsorption quotient model

At fixed pressure and temperature, build a joint distribution for cross-history affine coordinates and cross-ratios.

Preserve:

- segment labels;
- ancestry;
- local pressure grain;
- covariance induced by interpolation;
- quoted last-digit uncertainty.

Do not average pressure-local invariants into a Gaussian global summary by default.

## Gate D — Bethe quotient predictions

Map Bethe/network states to quotient observables without selecting \(V_s\) or \(V_c\).

Freeze:

- topology range;
- reversal ancestry;
- stable branch;
- no-passing constraints;
- admissible latent initial-state family.

## Gate E — finite-sample numerator and null upper bound

Construct:

\[
E_{\rm quotient}
=
\frac{g_T(\rho_H)}
     {U_{0,\rm quotient}(\rho_H)}.
\]

Both numerator and denominator must be proper densities/masses on the same quotient observation measure.

## Gate F — retrospective authority boundary

Historical execution remains SHADOW/RETROSPECTIVE unless a split frozen before outcomes can be demonstrated.

Authorized historical outputs:

- structural compatibility;
- power audit;
- model criticism;
- prospective design.

Not authorized:

- confirmatory beyond-standard claim;
- physical protogeometry.

## Gate G — local information accounting

Report pressure-by-pressure and loop-by-loop contributions. Means/global Gaussian summaries are secondary diagnostics only.

## Authorized outcomes

- PASS_QUOTIENT_OBSERVATION_MEASURE
- PASS_MAGNETIC_MAXIMAL_INVARIANT_LIKELIHOOD
- PASS_ADSORPTION_MAXIMAL_INVARIANT_LIKELIHOOD
- PASS_QUOTIENT_NULL_UPPER_BOUND
- PASS_QUOTIENT_UNIVERSAL_EVALUE_THEOREM
- FAIL_QUOTIENT_MODEL_IDENTIFIABILITY
- FAIL_QUOTIENT_POWER
- ABSTAIN_RETROSPECTIVE_CONFIRMATORY_AUTHORITY
- HOLD_PHYSICAL_PROTOGEOMETRY

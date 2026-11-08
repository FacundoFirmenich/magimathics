# HGMF‑UMI‑20 — Empirical Cross‑Carrier Semantic Spectrum

## Objective

Determine whether at least one empirical scale-rich instance of the HGMF‑UMI‑19 class exists.

## Gate A — corpus

Select two non-isomorphic carriers with:

- a shared UMI signature;
- at least four retained scales;
- sufficient resolution;
- explicit intervention or history.

## Gate B — frozen measure

Fix witnesses, weights and covers before observing \(\tau(q)\).

## Gate C — finite-size scaling

Estimate spectra at increasing sizes. Do not promote widths that collapse.

## Gate D — surrogates

Compare against:

- shuffling;
- hierarchy randomization;
- finite mixtures;
- heteroscedastic strata;
- regime-preserving surrogates.

## Gate E — transport

Verify that the shared spectrum survives the UMI transport while carrier-specific structure remains outside the signature.

## Gate F — triaxiality

Estimate V/H/D marginals and the joint coupling spectrum.

## Gate G — abstention

If fewer than four independent scales survive or the result is cover-dependent:

```text
ABSTAIN_INSUFFICIENT_SCALE_RANGE
```

## Authorized outcomes

- `PASS_EMPIRICAL_MULTIFRACTAL_UMI`
- `PASS_MULTISCALE_ONLY`
- `FAIL_TRANSPORT_INVARIANCE`
- `FAIL_SURROGATE_TRIBUNAL`
- `ABSTAIN_INSUFFICIENT_SCALE_RANGE`

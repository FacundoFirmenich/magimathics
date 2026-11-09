# HGMF-HG37 — Prospective pivot protocol

## Principle

The next experiment must measure the calibration variables that make the historical observation maps noninjective.

No retrospective tuning of the missing nuisance is allowed.

## A. Magnetic cartridge

### Required measurements

For every field point:
- commanded field;
- independently calibrated field readback;
- calibration device/model/serial;
- calibration date and certificate;
- bounded uncertainty or full calibration distribution;
- raw repeated Hall voltages;
- current-polarity reversal ancestry;
- temperature and timing.

### Identifiability targets

Historical engineering references only:

1. Global trained-vector non-saturation:
[
u_H < 4.0754321208 mathrm{mT}.
]

2. Every historical trained offset individually nonabsorbable:
[
u_H < 0.8838269371 mathrm{mT}.
]

These values are planning references derived from historical data, not future confirmatory effect thresholds.

For the future experiment, a minimum physically relevant bias (Delta^star) and target calibration bound must be frozen **before acquisition**.

### Minimal logical acquisition

At each coercive transition:
- at least two calibrated field values bracketing the crossing;
- raw repeated (V_{xy}) at each point.

### Robust acquisition

Use enough local points to audit interpolation curvature and preserve the complete (V_{xy}(H)) shape. The field-axis nuisance should be shared through a calibration model, not profiled independently per loop.

## B. Adsorption cartridge

Preferred clean route:

1. same adsorbate Xe;
2. same target temperature as the Vycor boundary/scans;
3. nonporous silica reference of matched surface chemistry;
4. independently measured surface area / mass normalization;
5. (V_s(p)) measured over the full pressure range used by network inference;
6. Vycor boundary isotherm;
7. preregistered scanning histories;
8. replicate measurements sufficient for an observation-error model.

Then:

[
V_s,V_c,V	o Q	o q
]

is identified with propagated uncertainty.

### Independent topology layer

Prefer an independent connectivity constraint (e.g. tomography/digital reconstruction or a separate sorption characterization) so the confirmatory scan does not simultaneously choose topology and test it.

## C. Alternative Mason route

A second legitimate research branch is to implement Mason's 1988 Brown-specific Bethe-tree method directly.

It may rescue a standard-network likelihood without a separate (V_s) measurement, but it must first be:
- reconstructed from the full published method;
- frozen before holdout;
- supplied with an observation-error model;
- converted to a likelihood upper bound/e-value interface.

Until then:

ABSTAIN_MASON_CONFIRMATORY_IMPLEMENTATION.

## D. Future-only seal

Historical Brown/FGT results may be used only for:
- design;
- scale selection;
- power planning.

They may not contribute to the confirmatory likelihood of the prospective run.

## E. Success conditions

A future carrier enters HG31 X only when:
- calibration receipts are admissible;
- observation map is identified;
- nuisance family is physically frozen;
- holdout outcomes were not used to set those objects.

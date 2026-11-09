# HGMF‑HG36 — Observation bridges and completed carrier-specific X denominator

## Gate A — Vycor reference isotherms

Recover the 151 K Brown boundary isotherm and construct admissible families for:

- Vs(p): reversible adsorption-film reference;
- Vc(p): condensed-fluid reference.

Do not hard-code expert-selected A/B/C/E points without uncertainty. Prefer a set-valued envelope over all reference curves satisfying published physical/shape constraints.

## Gate B — q(p) reconstruction

For each admissible Vs/Vc pair, derive:

Q+(p), Q-(p), q(p)

using the Bethe equations and the frozen z range [6.6,7.2].

Quantify the induced uncertainty/slack.

## Gate C — network likelihood upper bound

Construct a likelihood or certified upper bound on the actual adsorption-mass observations, marginalizing or maximizing conservatively over the admissible reference-curve family.

## Gate D — magnetic raw-voltage uncertainty

Use the raw repeated voltage arrays in the HDF5 source, not the field step alone, to propagate measurement uncertainty through:

Vxy -> normalized crossing fields -> C1,C2 -> HEB.

## Gate E — magnetic summary likelihood

Build a probabilistic likelihood for the source structural summary:
- loop1 nonzero-bias metastable state;
- loops2-5 trained near-zero state.

Do not claim a full micromagnetic Vxy likelihood unless the source theory supplies a calibrated forward map.

## Gate F — universal X denominator

Only after both carrier-specific physical nulls have likelihood upper bounds may HG31 universal e-values be computed.

## Gate G — claim boundary

Authorized outcomes:
- PASS_VYCOR_REFERENCE_BRIDGE
- PASS_CONSTRAINED_NETWORK_LIKELIHOOD
- PASS_MAGNETIC_SUMMARY_LIKELIHOOD
- PASS_CARRIER_SPECIFIC_X_DENOMINATOR
- FAIL_STANDARD_CARRIER_NULL
- ABSTAIN_REFERENCE_ISOTHERM_NONIDENTIFIABLE
- ABSTAIN_RAW_NOISE_MODEL
- HOLD_PHYSICAL_PROTOGEOMETRY

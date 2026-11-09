# HGMF-HG36 — Observation-bridge identifiability and summary-power no-go

**Fecha:** 9 de noviembre de 2026

## Veredicto

PASS_REAL_OBSERVATION_BRIDGE_EXECUTION  
PASS_RAW_VOLTAGE_NOISE_PROPAGATION  
PASS_MAGNETIC_FIELD_RESOLUTION_NUISANCE_THEOREM  
PASS_VYCOR_SET_VALUED_REFERENCE_AUDIT  
PASS_VYCOR_REFERENCE_NONIDENTIFIABILITY_THEOREM  
PASS_EXACT_BETHE_Q_INVERSION  

FAIL_HEB_SUMMARY_CONFIRMATORY_POWER  
FAIL_VYCOR_POINT_IDENTIFICATION  
FAIL_CARRIER_SPECIFIC_UNIVERSAL_EVALUE_DENOMINATOR  

ABSTAIN_MAGNETIC_EXACT_LIKELIHOOD_AUTHORITY  
ABSTAIN_VYCOR_NETWORK_LIKELIHOOD  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG36 closes the observation-bridge audit by showing that the two present carriers fail confirmatory identification for **different** reasons.

### Magnetism

The raw HDF5 files contain five nanovoltmeter samples per source row. A 5000-replicate nonparametric bootstrap propagated those samples through current-reversal subtraction, Vxy normalization, coercive interpolation and HEB.

Bootstrap standard deviations are only:

- loop 1: 0.00653 mT;
- loop 2: 0.00535 mT;
- loop 3: 0.00627 mT;
- loop 4: 0.01047 mT;
- loop 5: 0.01411 mT.

Thus the trained-loop HEB offsets are not voltage-noise artifacts. However each trained-loop |HEB| remains within the source field-step bound (~4.293 mT).

With

h_obs = mu + delta + epsilon,
|delta| <= Delta_H,

the trained null mu=0 can choose delta=h_obs whenever |h_obs|<=Delta_H. The HEB summary null then reaches zero stochastic residual and has no universal-evalue power.

### Xe/Vycor

The Brown boundary/scanning data do not contain the external nonporous Xe/silica film reference required to point-identify Vs(p).

Using only order constraints from the Brown boundary loop yields:

- 614 Q intervals;
- median Q interval width = 0.28585;
- mean Q interval width = 0.30631;
- max Q interval width = 0.99660.

For run-1 Bethe inversion:

- 89 q intervals;
- median q interval width = 0.21412;
- mean q interval width = 0.23213;
- max q interval width = 0.71584.

Therefore Brown alone constrains but does not point-identify Vs, Q or q.

## Consequence

The carrier-specific HG31 denominator is still not available. This is now an identifiability result, not an unspecified missing-model problem.

## Próxima frontera

HGMF-HG37 — External calibration closure versus prospective-pivot theorem.

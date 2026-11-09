# HGMF‑HG35 — Quantitative standard-null bridge

**Fecha:** 9 de noviembre de 2026

## Veredicto

PASS_REAL_QUANTITATIVE_EXECUTION  
PASS_MAGNETIC_SOURCE_INTERVAL_NULL  
PASS_MAGNETIC_TRAINING_ONE_SHOT_COMPATIBILITY  
PASS_BETHE_TOPOLOGY_CORE  
PASS_XE_VYCOR_NETWORK_NULL_EXISTS  
PASS_NETWORK_CONNECTIVITY_RANGE_FREEZE  
PASS_BETHE_NUMERICAL_ROOT_CERTIFICATION  

FAIL_FULL_MAGNETIC_VXY_LIKELIHOOD_BRIDGE  
FAIL_COMPLETE_XE_VYCOR_OBSERVATION_LIKELIHOOD  
FAIL_BEYOND_STANDARD_CLAIM_FROM_HG34_RPM_RESIDUALS  

ABSTAIN_UNIVERSAL_EVALUE_X  
ABSTAIN_PHYSICAL_IDT_REJECTION  
HOLD_PHYSICAL_PROTOGEOMETRY

## Magnetic result

The source-specific interval null is supported at the source field-resolution level:

- loop 1 HEB = -48.4257 mT with deterministic field-resolution interval [-53.5776,-43.2738] mT, excluding zero;
- loops 2–5 HEB = 0.8838, -4.0754, 3.3383, 1.3417 mT;
- all four later resolution intervals include zero;
- maximum |HEB| / field-resolution among loops 2–5 = 0.94927.

A one-shot trained-state model gives Hinf = 0.3721 mT and RMSE 2.7286 mT over loops 2–5.

A Binek recursive diagnostic gives RMSE 2.5692 mT, a relative improvement of only 5.84%, with fitted Hinf = 16.4833 mT. It remains a diagnostic, not an identified source mechanism.

The source repository contains theoretical M/MS curves and FM/AFM magnetization profiles, but not a calibrated stochastic forward map to Vxy(H). Therefore no pointwise source-model likelihood or e-value is authorized.

## Xe/Vycor network result

The published Bethe/percolation topology core is executable with externally frozen Vycor connectivity:

- z in [6.6,7.2];
- qc = 1/(z-1) in [0.1612903,0.1785714];
- published scan examples Q+ = 0.12 and 0.34.

The bracketed solver passes:
- primary threshold behavior;
- probability bounds;
- scanning monotonicity.

However the adsorption-mass observation bridge still requires reference isotherms Vs(p), Vc(p), and q(p). Therefore the physical network family is alive but not yet a complete likelihood family inside HG31 X.

## Consequence

The RPM residuals found in HG34 cannot be promoted to beyond-standard evidence. A standard pore-network/percolation family has been applied historically to the same Brown Xe/Vycor benchmark and remains unresolved in our confirmatory denominator.

## Próxima frontera

HGMF‑HG36 — Set-valued reconstruction of Vs/Vc/q(p), raw-voltage uncertainty propagation for magnetic HEB, and completion of the carrier-specific universal-evalue denominator.

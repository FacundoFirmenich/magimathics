# HGMF‑HG35 — Quantitative source-specific standard-null bridge

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

## 1. Magnetic summary null

HG35 deliberately does not manufacture a probability distribution from the source field step.

It uses deterministic set membership:
- loop 1: HEB = -48.4257 mT, interval [-53.5776,-43.2738] mT;
- loop 2: 0.8838 mT, interval [-3.4094,5.1771];
- loop 3: -4.0754 mT, interval [-8.3687,0.2178];
- loop 4: 3.3383 mT, interval [-0.9550,7.6315];
- loop 5: 1.3417 mT, interval [-2.9515,5.6349].

Thus the source statement “first loop exchange-biased, trained loops approximately zero-bias” passes at the measurement-resolution level.

## 2. Training-law diagnostics

A one-shot model predicts a common trained-state HEB of 0.3721 mT and gives RMSE 2.7286 mT on loops 2–5.

A Binek recursive comparator gives RMSE 2.5692 mT, only 5.84% lower. Its fitted Hinf = 16.4833 mT is not treated as a physical asymptote with only five loops.

Therefore Binek is retained only as a comparator. The source metastable-state transition remains structurally and quantitatively viable.

## 3. Magnetic likelihood boundary

The public source contains:
- Vxy(H);
- HEB/coercivity summaries;
- theoretical CrSBr M/MS vs field;
- FM/AFM Mz/Ms spatial profiles;
- phenomenological free-energy support for metastability/domain formation.

It does not contain a calibrated stochastic forward map to Vxy. No source-specific pointwise likelihood or HG31 e-value denominator is authorized.

## 4. Vycor Bethe/percolation null

A standard network model has already been applied to the Brown Xe/Vycor benchmark.

HG35 freezes the published connectivity range:
- z = 6.6 to 7.2;
- qc = 0.16129 to 0.17857;
- representative scan initial unfilled fractions Q+ = 0.12 and 0.34.

The executed Bethe core passes threshold, probability-bound and monotonicity checks.

## 5. Observation bridge boundary

The network state fraction must be related to measured adsorption through

Q(p) = [Vc(p)-V(p)]/[Vc(p)-Vs(p)].

The literature defines Vs as an extrapolated adsorption-film reference and Vc as a condensed-fluid reference. q(p) is then reconstructed from primary/scanning desorption.

Those objects are not yet frozen in our pipeline. A topology model without this bridge is not a complete likelihood on adsorption mass.

## 6. Consequence for HG34

The 37/57 digitized RPM mismatches cannot be promoted to beyond-standard evidence while a physically established percolation/network family on the same Xe/Vycor benchmark remains untested in our denominator.

## 7. Próxima frontera

HG36 will reconstruct Vs, Vc and q(p) in a set-valued/auditable way that avoids cherry-picking A/B/C/E; in parallel it will propagate raw AHE voltage uncertainty into HEB summaries to build a probabilistic magnetic source-summary likelihood.

# HGMF‑HG42 — Prospective quotient noise laws and split-sealed e-values

## Verdict

PASS_CALIBRATION_AUGMENTED_QUOTIENT_EVALUE_THEOREM  
PASS_FROZEN_COMPRESSION_PUSHFORWARD  
PASS_DEPENDENCE_FIREWALL  
PASS_SAFE_WEIGHTED_MEAN_AGGREGATION  
PASS_INTERSECTION_MIN_EVALUE  
PASS_SEQUENTIAL_CONDITIONAL_PRODUCT_RULE  
PASS_GAUSSIAN_PROFILE_REPLICATE_RANK_THEOREM  
PASS_INTERPOLATION_COVARIANCE_PROPAGATION  
PASS_MAGNETIC_QUOTIENT_NOISE_LAW_CONTRACT  
PASS_ADSORPTION_QUOTIENT_NOISE_LAW_CONTRACT  
PASS_FAIL_CLOSED_PROSPECTIVE_SEAL  

FAIL_PRODUCT_OF_MARGINAL_EVALUES_UNDER_DEPENDENCE  
FAIL_HISTORICAL_MAGNETIC_NOISE_LAW_READINESS  
FAIL_HISTORICAL_ADSORPTION_NOISE_LAW_READINESS  
FAIL_ACTUAL_QUOTIENT_EVALUE_EXECUTION  

ABSTAIN_REAL_REPLICATES_MISSING  
ABSTAIN_PROPER_QUOTIENT_DENSITIES_MISSING  
ABSTAIN_NULL_UPPER_DENSITY_CERTIFICATE  

HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. The probabilistic object

The confirmatory evaluation object is not quotient holdout alone. It is

X=(C,Z),

where C contains calibration/reference data and Z is the holdout maximal invariant.

For a training-frozen proper density g_T(C,Z) and a null upper density U_0(C,Z),

E(C,Z)=g_T(C,Z)/U_0(C,Z)

is finite-sample valid whenever U_0 upper-bounds every carrier-standard joint null density on the same measure.

This absorbs calibration uncertainty into the confirmatory model rather than pretending that calibration is known.

## 2. Dependence firewall

A weighted mean of e-values is valid under arbitrary dependence. The minimum is also valid and enforces all-cell evidence.

A product of marginally valid e-values is not generally valid. HG42 verifies a counterexample with expectation two.

Products are authorized only as conditional e-factors under a frozen filtration.

## 3. Replicate-rank frontier

For a d-dimensional quotient vector with a rank-r fitted mean design, an unrestricted covariance needs at least

n >= d+r

independent replicate vectors for finite Gaussian profile likelihood.

Historical magnetism:
- d=3;
- n=1;
- minimum n=4.

Historical adsorption:
- d=242 for the uncompressed HG40 vector;
- one correlated history ensemble;
- unrestricted full covariance minimum n=243.

The adsorption number is not a recommended experiment. It proves that the full historical vector requires either training-only compression or a structured covariance family with its own certificate.

## 4. Interpolation covariance

For raw covariance Sigma_raw, interpolation A and quotient Jacobian G,

Sigma_Q=G A Sigma_raw A^T G^T.

Shared nodes create dependence. Treating interpolated coordinates as independent changes the observation law and can manufacture evidence.

## 5. Compression

A compression frozen on training may reduce quotient dimension. Proper candidate and null laws must be pushed to the same compressed measure.

Compression preserves validity, not lost information.

## 6. Carrier contracts

### Magnetism

The law must be joint in field calibration and replicated full-curve quotient observations. It must preserve cross-loop, field-map, anchor and interpolation covariance. HEB alone remains inadmissible as the primary confirmatory object.

### Adsorption

The law must include raw reference/sample covariance, pressure interpolation, cross-history covariance, anchor uncertainty and network/reference uncertainty. Pressure nodes are not replicates.

## 7. Current seal

The protocol validator returns:

ABSTAIN_REAL_REPLICATES_OR_DENSITY_PROOFS_MISSING.

There are no schema errors. Blockers are substantive:

- no numeric anchor-degeneracy threshold;
- no real magnetic replicate receipt;
- magnetic replicate-rank deficit;
- no real adsorption replicate receipt;
- no structured adsorption covariance proof;
- no proper candidate density proof;
- no certified null upper-density proof.

No acquisition or holdout evaluation is authorized.

## 8. Next frontier

HG43 must ingest real receipts, fit the two quotient laws on training only, certify every null upper density, compute local maximin power and decide whether the future-only e-value can be armed.

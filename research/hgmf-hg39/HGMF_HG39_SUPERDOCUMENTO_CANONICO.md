# HGMF‑HG39 — Commissioning dossier and arming preflight

## Veredicto

PASS_COMMISSIONING_ROUTE_CLOSURE  
PASS_MAGNETIC_TRACEABILITY_ROUTE  
PASS_ADSORPTION_REFERENCE_ROUTE  
PASS_INDEPENDENT_TOPOLOGY_ROUTE  
PASS_FITNESS_RULE_COMPILER  
PASS_COMMISSIONING_EVIDENCE_SCHEMA  
PASS_FAIL_CLOSED_PREARMING_VALIDATOR  
PASS_LOCAL_AND_NATIONAL_CAPABILITY_DISCOVERY  

ABSTAIN_REAL_MAGNETIC_CALIBRATION_RECEIPT  
ABSTAIN_REAL_ADSORPTION_REFERENCE_RECEIPT  
ABSTAIN_REAL_TOPOLOGY_RECEIPT  
ABSTAIN_SIGNED_SCOPE_CONFIRMATIONS  
ABSTAIN_NUMERIC_FITNESS_LIMITS  
ABSTAIN_HG38_ARMING  

HOLD_ACQUISITION  
HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. What HG39 closes

HG38 defined what a prospective identifiable experiment must contain. HG39 identifies executable provider/method routes, formalizes evidence levels, compiles fitness-for-purpose calculations, and creates a fail-closed pre-arming validator.

HG39 does **not** claim that commissioning has occurred.

## 2. Evidence cannot be promoted by prose

The hierarchy is:

CAPABILITY_DISCOVERY  
→ ACCREDITED_SCOPE  
→ SIGNED_SERVICE_CONFIRMATION  
→ ACTUAL_MEASUREMENT_RESULT.

Each arrow requires a new object. None is automatic.

A laboratory can be competent in a general scope while the requested sample-plane geometry, range, covariance or Xe protocol remains outside that service. The future HGMF result becomes traceable only through the complete measurement system and actual result receipt.

## 3. Magnetic route

The strongest identified Spanish route is the ENAC-accredited UPM Laboratorio de Medidas Magnéticas, complemented by CEM MAGLAB as national-metrology route. NPL is an international backup with broad magnetic-instrument validation.

The service must not end at calibrating a loose Hall probe. It must connect the final sample-plane field to command/readback over the complete experiment, with:

- pre/post calibration;
- both directions;
- reversal-region density;
- positioning and gradient sensitivity;
- drift and hysteresis;
- covariance;
- signed scope and actual certificate.

The primary scientific observable remains the full Vxy versus reference-field curve.

## 4. Adsorption route

Local facilities exist for BET/porosimetry and electron microscopy, but routine N2 BET capability does not establish Xe at the target temperature.

The commissioning request therefore specifies a custom campaign with:

- matched nonporous silica;
- same pretreatment and Xe lot;
- traceable pressure, temperature and mass;
- interleaved reference/sample/reference order;
- full-domain Vs and Vc;
- curve covariance;
- independent topology.

Certified BET or SAXS standards are instrument-performance controls, not substitutes for the scientific film reference.

## 5. Topology route

The proposed stack is deliberately plural:

- SAXS/USAXS for size/surface information;
- a connectivity-sensitive 3D method or conservative connectivity set;
- explicit resolution-adequacy analysis;
- sample-split ancestry and uncertainty.

ALBA NCD-SWEET provides a local SAXS/WAXS route for porous materials. TEM tomography or advanced nanotomography requires a service-specific resolution confirmation before it can populate the topology receipt.

## 6. Fitness compiler

Magnetic expanded uncertainty is compiled from component standard uncertainties and the frozen coverage factor.

Adsorption uncertainty propagates the full covariance of V, Vs and Vc through:

Q=(Vc-V)/(Vc-Vs).

The Bethe q covariance is propagated from Qplus, Qminus and z.

The current numeric input is intentionally incomplete. The compiler returns:

ABSTAIN_NUMERIC_FITNESS_INPUT_INCOMPLETE.

## 7. Current adjudication

The current dossier has no validation errors. It is a valid uncommissioned dossier.

Its blockers are:

- missing three signed service confirmations;
- missing three actual result receipts;
- numeric limits not frozen;
- fitness artifacts absent;
- state not commissioned.

Therefore:

ABSTAIN_REAL_COMMISSIONING_NOT_COMPLETE.

No acquisition authority is granted.

## 8. Strategic outcome

The next work is external and finite:

1. obtain signed scopes;
2. execute calibrations/references/topology;
3. freeze limits;
4. run validators;
5. either arm or fail closed.

There is no scientific reason to inspect holdout outcomes before these steps.

## 9. Next gate

HGMF‑HG40 — Signed scopes, real commissioning measurements and HG38 arming decision.

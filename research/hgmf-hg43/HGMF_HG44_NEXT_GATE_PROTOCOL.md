# HGMF‑HG44 — Anytime-valid quotient e-process and stopping constitution

HG44 is conditional on a future PASS_ARMED_RECEIPT_CONDITIONED_QUOTIENT_EVALUE from HG43.

## Gate A — filtration

Freeze the order in which calibration, replicate and carrier information becomes available.

## Gate B — conditional e-factors

For each increment e_t prove:

E[e_t | F_{t-1}] <= 1

under every admitted standard null.

## Gate C — adaptive replication

Permit additional replicates only through a rule frozen before observing their outcomes. Adaptation may depend on past admissible information but may not alter the model family or claim semantics.

## Gate D — local cell budgets

Preserve preregistered local cells. Optional continuation cannot abandon a weak cell and retain the original conjunction claim.

## Gate E — drift and calibration triggers

Freeze fail-closed rules for recalibration, reference failure and ancestry breaks. Triggered recalibration creates a new admissible epoch rather than silently overwriting the previous receipt.

## Gate F — anytime-valid stopping

The cumulative process

E_t = product_{i<=t} e_i

may be stopped at any stopping time only after the conditional e-factor proof is frozen.

## Gate G — final claim

Map carrier-local, mixture and conjunction claims to their authorized e-process aggregation. No retrospective relabelling is allowed.

## Authorized outcomes

PASS_ANYTIME_VALID_QUOTIENT_EPROCESS
PASS_ADAPTIVE_REPLICATION_RULE
PASS_OPTIONAL_STOPPING_SAFETY
PASS_LOCAL_CELL_PRESERVATION
FAIL_CONDITIONAL_EFACTOR_PROOF
FAIL_STOPPING_CONSTITUTION
ABSTAIN_HG43_NOT_ARMED
HOLD_PHYSICAL_PROTOGEOMETRY

# MGM‑UMI‑REAL‑04 — Blind Adversarial Benchmark

**Date:** 6 November 2026  
**Authority:** `MAGIMATICS / METHOD SELECTIVITY GATE`  
**Verdict:** `PASS_INTERNAL_BLINDED_SELECTIVITY / EXTERNAL_BLIND_VALIDATION_HOLD`

A ten-family adversarial benchmark was frozen before unblinding: five established UMI-positive functions and five close decoys. Truth labels were sealed behind SHA‑256 commitment `818553b951d819db9679318f83f816fbc2730173d8143b143fc64507d1b769bb`.

## Strict result

```text
TP = 5
FP = 0
TN = 5
FN = 0
precision = 1.000
recall = 1.000
specificity = 1.000
accuracy = 1.000
FDR = 0.000
```

Wilson 95% intervals remain broad: sensitivity 0.566–1.000, specificity 0.566–1.000, accuracy 0.722–1.000. This is strong internal calibration, not external validation.

## Semantic-signature sensitivity

- strict: precision 1.000, FDR 0.000;
- moderate: precision 0.833, FDR 0.167;
- weak: precision 0.500, FDR 0.500.

The decisive finding is that the tribunal cannot rescue a badly specified semantic signature. Selectivity comes from the conjunction of frozen semantics, substitution, rewiring, ablation, transport and minimality.

## Missing evidence

Conservative abstention produced zero false positives and perfect accuracy among adjudicated cases when one or two tribunal dimensions were withheld, at the cost of coverage.

## Status

```text
INTERNAL_ADVERSARIAL_SELECTIVITY = PASS
GROUND_TRUTH_COMMITMENT          = PASS
MISSING_EVIDENCE_ABSTENTION      = PASS
EXTERNAL_REVIEWER_BLIND          = HOLD
NATURALISTIC_OUT_OF_SAMPLE_SET   = HOLD
METHODS_PREPRINT                 = READY_FOR_EXTERNAL_REVIEW
```

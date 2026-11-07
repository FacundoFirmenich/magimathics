# HGMF‑UMI‑10 — Canonical Adjudication

**Date:** 7 November 2026  
**Verdict:** `PASS_SHARED_HISTORY_SEMANTIC_CORE / FAIL_UNCONDITIONAL_SINGLE_OPERATOR / HOLD_RPM`

## 1. Primary result

The same minimal semantic requirement is supported in adsorption and magnetism:

\[
\Sigma_{\rm hist}
=
(\text{same-input multiplicity},
\text{branch dependence},
\text{history-bearing state}).
\]

Hence instantaneous input alone is not a sufficient state in either domain.

However, semantic equivalence does not imply operator identity:

\[
\equiv_\mu\Rightarrow\equiv_{\rm op}\Rightarrow\equiv_{\rm sem},
\qquad
\equiv_{\rm sem}\not\Rightarrow\equiv_{\rm op}.
\]

## 2. Magnetic tribunal

Four public HDF5 minor loops were recovered and decoded using the source repository's current-reversal logic. One isolated +2500 mT pre-field point was removed by an independently specified jump rule.

- processed points: 141, 121, 101, 81;
- one reversal / two monotonic segments per file;
- aggregate best model: `fading`;
- aggregate RMSE: 0.587540;
- memoryless RMSE: 0.753018;
- aggregate improvement: 21.98%;
- mean normalized return error: 0.740872.

### SNR stratification

High-SNR loops 1–2:

- amplitude/median error: 8781 and 9362;
- RPM relays win both blocked holdouts;
- RPM mean RMSE: 0.520430;
- memoryless mean RMSE: 0.816650;
- improvement: 36.27%.

Low-SNR loops 3–4:

- amplitude/median error: 5.92 and 4.81;
- fading memory wins both;
- normalized point error is 0.169–0.208;
- RPM is 3.53% worse than memoryless on average.

Adjudication: `PASS_PRELIMINARY_RPM_HIGH_SNR / ABSTAIN_LOW_SNR_OPERATOR_IDENTITY`.

The protocol cannot identify nested return-point memory because each magnetic file has only one reversal.

## 3. Adsorption tribunal

Complete NIST runs 5, 8, 9 and 10 were preserved as continuous histories.

- 572 points;
- 20, 22, 27 and 36 reversals;
- aggregate best model: `rpm_relays`;
- RPM mean RMSE: 0.346994;
- memoryless RMSE: 0.358008;
- aggregate improvement: 3.08%;
- mean normalized return error: 0.307740.

But RPM wins only 2 of 4 whole-run holdouts:

- run 5: fading;
- run 8: RPM;
- run 9: RPM;
- run 10: branch.

Adjudication: `PASS_MEAN_ONLY / FAIL_ROBUST_RPM_SELECTION`.

## 4. Final gate result

```text
PASS_BINARY_RECOVERY
PASS_REAL_DATA_WHOLE_RUN_TRIBUNAL
PASS_SHARED_HISTORY_SEMANTIC_CORE
PASS_CONDITIONAL_HIGH_SNR_RPM_TRANSFER

FAIL_UNCONDITIONAL_SINGLE_OPERATOR_CLASS
FAIL_ROBUST_ADSORPTION_RPM_SELECTION

HOLD_RETURN_POINT_MEMORY
HOLD_FUTURE_ONLY_ABSOLUTE_FORECAST
HOLD_PHYSICAL_OPERATOR_TRANSITION
```

## 5. Scientific interpretation

The empirically supported UMI is not a Preisach bank, a stack or a fading kernel. Those are operator shells. The shared unit is the minimal semantic conformational requirement that the active history must be retained.

This is a jurisdictional result for General Systems Theory: a semantic invariant can be transported while the realizing operator changes or remains conditionally identifiable.

## 6. Execution provenance

Validated GitHub Actions execution before canonical documentation:

- run: `42410952034`;
- artifact: `13589427583`;
- artifact digest: `sha256:9d917cc3d73afcf79b402afff6d4a9385a4656c44d0d82771f0d1f066c06c704`;
- branch: `hgmf-umi10-rpm-completion`;
- pull request: `#10`.

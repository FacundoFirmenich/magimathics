# HGMF‑UMI‑11 — Memory Universality Classes and Resolution Gates

## Primary question

Is the observed operator change a physical transition between memory classes, or a loss of identifiability caused by measurement resolution and protocol depth?

## Gate A — Error-aware tribunal

Use point-wise experimental uncertainty in the likelihood or scoring rule. Do not normalize a signal by an amplitude comparable to measurement error without an abstention state.

## Gate B — Nested magnetic protocols

Audit magnetic histories containing at least three nested reversals per trajectory. Required observables:

- return-point error;
- wiping-out error;
- loop congruency;
- stack-depth recovery;
- retained-extremum ablation.

## Gate C — Future-only absolute forecasting

Freeze all scaling, thresholds and parameters on training runs. Predict absolute output and future branch without using the complete held-out range.

## Gate D — Memory universality classes

Compare preregistered classes:

1. memoryless;
2. branch memory;
3. fading memory;
4. finite reversal stack;
5. RPM/Preisach;
6. context-conditioned mixtures with a physically defined gate.

## Gate E — Resolution gate

Test whether the selected class changes systematically with:

- amplitude / point-error ratio;
- reversal depth;
- loop width;
- temperature;
- sweep rate;
- temporal resolution.

The gate must be frozen before evaluating held-out results.

## Gate F — UMI semantic core

Test whether

\[
\Sigma_{\rm hist}
=
(\text{same-input multiplicity},
\text{branch dependence},
\text{history-bearing state})
\]

remains invariant when the operator shell changes.

## Gate G — Cross-domain transfer

Train one state-update law in one domain and transfer it to the other, allowing only domain-specific readout maps. No retuning of the update law.

## Gate H — Admissible outcomes

```text
PASS_UNIVERSAL_HISTORY_CORE
PASS_CONTEXT_CONDITIONED_OPERATOR_FAMILY
PASS_RPM_IN_IDENTIFIABLE_REGIME
FAIL_OPERATOR_TRANSFER
FAIL_SEMANTIC_CORE
HOLD_PROTOCOL_DEPTH
```

## Hard promotion rule

No operator may be called universal because it wins an aggregate mean while losing in half of the complete held-out histories or in a preregistered quality stratum.

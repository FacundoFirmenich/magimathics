# P2b Production Gate 01 — Primary Biological Evidence Freeze

**Closed:** 2026-11-07  
**Verdict:** `PASS_P2B_PROD01`

## Gate objective

Convert the biological companion manuscript into a traceable evidence architecture that cleanly separates exact results, mechanistic models, direct experiments, physical interventions, cross-substrate transport and unresolved causal cases.

## Pass criteria

1. P2/P2b editorial ownership frozen;
2. six positive biological mechanism classes and one abstention case fixed;
3. strict biological semantic signature defined for every case;
4. source-by-source intervention and outcome extraction completed;
5. causal limitations recorded rather than omitted;
6. published experiments separated from our model counterfactuals;
7. primary bibliography created with DOI/PMID where verified;
8. figure sources derived only from persisted numerical records.

## Receipts

```text
MANUSCRIPT_V0_1               = PASS
EDITORIAL_SEPARATION          = PASS
BIOLOGICAL_EVIDENCE_MATRIX    = PASS
PRIMARY_EVIDENCE_LEDGER       = PASS_25_RECORDS
CLAIM_LEDGER                  = PASS
SOURCE_DEPENDENCY_MAP         = PASS
BIBTEX_LIBRARY                = PASS_V0_1
FIGURE_2A_SOURCE              = PASS
FIGURE_2B_SOURCE              = PASS
FIGURE_3_SOURCE               = PASS
QUORUM_SENSING_ABSTENTION     = PRESERVED
```

## Evidence classes frozen

```text
T1 = exact theorem or exhaustive result
M1 = explicit mechanistic model
P1 = direct physical experiment
P2 = physical intervention or perturbation
P3 = independent substrate or implementation
S1 = controlled literature synthesis
A  = ambiguous or incomplete causal evidence
```

## Scientific boundary

The gate authorizes a biological mechanism-adjudication paper. It does not claim discovery of the repressilator, integral control, bistable switches, kinetic proofreading, Turing instability or RAF closure. It does not infer organismal autonomy from local closure and does not promote unresolved quorum-sensing causality.

## Next gate

`P2B-PROD02 — Figure, Table and LaTeX Integration`

Required outputs:

- complete bioRxiv LaTeX source tree;
- Figures 1–7 and Tables 1–4;
- source-to-claim citation map;
- primary-evidence supplement;
- compiled-PDF receipt;
- bioRxiv source-package validation.

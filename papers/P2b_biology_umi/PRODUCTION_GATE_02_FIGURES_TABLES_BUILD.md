# P2b Production Gate 02 — Figures, Tables and Clean Build

**Closed:** 2026-11-07  
**Verdict:** `PASS_P2B_PROD02`

## Completed objects

```text
FIGURES                    = 7/7 (+ separate repressilator phase panel)
TABLES                     = 4/4
FIGURE_PROVENANCE          = PASS
PRIMARY_EVIDENCE_LEDGER    = PASS_25_RECORDS
LATEX_SOURCE_TREE          = PASS
CLEAN_UBUNTU_BUILD         = PASS
BIORXIV_SOURCE_PACKAGE     = PASS
SHA256_RECEIPTS            = PASS
ARTIFACT_UPLOAD            = PASS
```

## Clean-build receipt

- workflow run: `42319477429`;
- job: `128240328888`;
- head SHA: `cf527ab1971a620eeae5b8cae1fb0788a35b610a`;
- artifact: `P2b-production-build`;
- artifact ID: `13551658668`;
- artifact digest: `sha256:b37fe5352ba6d75e768c3960ba3bbca7582a7a3b009a0e8933b83b7e94a9d929`.

The clean runner generated:

- compiled biological manuscript PDF;
- isolated bioRxiv source tarball;
- LaTeX build receipt;
- bioRxiv package receipt;
- SHA-256 manifests.

## Included production figures

1. motif-to-UMI biological qualification;
2. repressilator intervention and phase panels;
3. RPA relation-subset minimality;
4. writable bistable memory;
5. proofreading/Turing mechanism–phenotype separation;
6. RAF closure and quorum-competence abstention;
7. biological carrier atlas.

## Included production tables

1. biological evidence classes;
2. biological UMI portfolio;
3. comparator frameworks;
4. biological claim boundary.

## Remaining gate

`P2B-PROD03 — Citation Integration, Evidence Supplement and Release Freeze`

Required:

- insert evidence-ledger citations into manuscript v0.2;
- complete citation-key and source-line audit;
- produce the primary-evidence supplement;
- reserve Zenodo software and evidence-dataset DOIs;
- rebuild source package with DOI metadata;
- final bioRxiv metadata and category freeze.

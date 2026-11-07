# P2 Production Gate 02 — Figures, Tables and Clean Build

**Closed:** 2026-11-07  
**Verdict:** `PASS_P2_PROD02`

## Completed objects

```text
FIGURES                   = 6/6 (+ two data panels in Figure 4)
TABLES                    = 4/4
FIGURE_PROVENANCE         = PASS
LATEX_SOURCE_TREE         = PASS
CLEAN_UBUNTU_BUILD        = PASS
ARXIV_SOURCE_PACKAGE      = PASS
SHA256_RECEIPTS           = PASS
ARTIFACT_UPLOAD           = PASS
```

## Clean-build receipt

- workflow run: `42319450073`;
- job: `128240158788`;
- head SHA: `6e8d86db15e4157c8575d145223c6e4d64af902c`;
- artifact: `P2-production-build`;
- artifact ID: `13551498882`;
- artifact digest: `sha256:167d1ffbac8920cd688d989f4020ce92b8808e1abe2794b2453edc3773cc111e`.

The clean runner generated:

- compiled PDF;
- isolated arXiv source tarball;
- LaTeX build receipt;
- arXiv package receipt;
- SHA-256 manifests.

## Included production figures

1. frozen tribunal architecture;
2. cross-domain carrier atlas;
3. relation-first intervention asymmetry;
4. semantic sensitivity and missing-evidence abstention;
5. naturalistic mechanism–decoy pairs;
6. UMI refinement order.

## Included production tables

1. formal objects and decision outputs;
2. comparator frameworks;
3. evidence hierarchy;
4. claim boundary.

## Remaining gate

`P2-PROD03 — Citation Integration, Priority Audit and Release Freeze`

Required:

- insert verified citations into manuscript v0.2;
- complete reference-key audit;
- complete line-by-line priority audit;
- reserve Zenodo software and dataset DOIs;
- rebuild source archive with DOI metadata;
- final editorial review and arXiv metadata freeze.

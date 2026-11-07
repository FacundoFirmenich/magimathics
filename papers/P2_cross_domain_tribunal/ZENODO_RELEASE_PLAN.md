# P2 Zenodo Release Plan

## Record A — Software

Contents:

- tribunal implementation;
- exact and exhaustive verifiers from REAL‑01 through REAL‑05;
- figure-generation scripts;
- build scripts;
- environment manifest;
- software SHA-256 manifest.

Metadata source: `zenodo_software_metadata.json`.

## Record B — Dataset

Contents:

- `CASE_MATRIX.csv`;
- claim and citation maps;
- intervention and minimality tables;
- blind packets, predictions and reveal data;
- benchmark metrics;
- provenance manifests;
- verification receipts.

Metadata source: `zenodo_dataset_metadata.json`.

## DOI workflow

1. create both Zenodo drafts;
2. reserve both DOIs;
3. insert reserved DOI values in manuscript and CFF metadata;
4. build and verify arXiv package;
5. publish Zenodo records;
6. release arXiv v1 referencing both immutable records;
7. add the arXiv identifier back to each Zenodo record as a related identifier.

## Release prohibition

No Zenodo record is published until:

- citation-key audit passes;
- all files appear in the SHA-256 manifest;
- the isolated LaTeX build passes;
- claim ledger contains no unresolved promoted claim;
- P2/P2b overlap audit passes.

# P2b Zenodo Release Plan

## Record A — Software

Contents:

- exact and numerical verifiers;
- intervention-analysis scripts;
- figure-generation scripts;
- build scripts;
- environment and software manifests;
- SHA-256 receipt.

Metadata source: `zenodo_software_metadata.json`.

## Record B — Biological evidence dataset

Contents:

- `PRIMARY_EVIDENCE_LEDGER.csv`;
- `BIOLOGICAL_EVIDENCE_MATRIX.csv`;
- `CITATION_CLAIM_MAP.csv`;
- claim ledger;
- source manifests;
- intervention and minimality tables;
- evidence-class definitions;
- verification receipts.

Metadata source: `zenodo_dataset_metadata.json`.

## DOI workflow

1. create draft software and dataset records;
2. reserve both DOI values;
3. insert DOI values in manuscript, CFF and bioRxiv metadata;
4. complete isolated LaTeX/bioRxiv build;
5. publish both Zenodo records;
6. submit bioRxiv v1;
7. add the bioRxiv identifier to the Zenodo related identifiers.

## Release prohibition

No record is published until:

- every P1/P2/P3 claim resolves to one evidence-ledger row;
- exact and model results are not described as wet-lab observations;
- all citation keys resolve;
- LaTeX package compiles in isolation;
- P2/P2b overlap audit passes;
- no license metadata is inferred without an explicit author decision.

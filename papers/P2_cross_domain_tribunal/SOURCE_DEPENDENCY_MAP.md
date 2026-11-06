# P2 Source Dependency Map

P2 is built entirely from repository-persisted sources. No claim in the current manuscript depends exclusively on a temporary chat attachment.

## Formal and conceptual sources

- `docs/01_TABLA_ROSETTA.md` — terminology and comparator mapping;
- `docs/02_FORMULARIO_CANONICO.md` — formal definitions;
- `docs/03_ESTADO_DEL_ARTE_Y_FRONTERA.md` — prior state-of-the-art audit;
- `docs/04_HIPERCORPUS_CANONICO.md` — canonical programme;
- `docs/05_GENEALOGIA_DE_CORRECCIONES.md` — correction history;
- `docs/07_BIBLIOGRAFIA.md` — inherited bibliography;
- `data/master_claim_ledger.csv` — programme-level claim status.

## Real-case sources

### Oscillation

- `research/umi-real01/README.md`;
- `research/umi-real01/data/intervention_results.csv`;
- `research/umi-real01/data/sign_topology_audit.csv`;
- `research/umi-real01/data/substitution_and_phase.csv`;
- `research/umi-real01/verify_umi_real01.py`.

### Robust perfect adaptation

- `research/umi-real02/README.md`;
- `research/umi-real02/METHODS.md`;
- `research/umi-real02/data/intervention_results.csv`;
- `research/umi-real02/data/minimality_audit.csv`;
- `research/umi-real02/data/evidence_matrix.csv`;
- `research/umi-real02/verify_umi_real02.py`.

### Error correction, memory, homeostasis and consensus

- `research/umi-real03/README.md`;
- `research/umi-real03/METHODS.md`;
- `research/umi-real03/data/candidate_matrix.csv`;
- `research/umi-real03/data/claim_ledger.csv`;
- `research/umi-real03/verify_umi_real03_portfolio.py`.

## Selectivity and abstention sources

### Designed adversarial benchmark

- `research/umi-real04/README.md`;
- `research/umi-real04/METHODS.md`;
- `research/umi-real04/BLINDING_PROTOCOL.md`;
- `research/umi-real04/data/BLINDED_CASES.json`;
- `research/umi-real04/data/BLIND_PREDICTIONS.csv`;
- `research/umi-real04/data/METRICS_BY_SIGNATURE.csv`;
- `research/umi-real04/data/MISSING_EVIDENCE_ROBUSTNESS.csv`;
- `research/umi-real04/verify_umi_real04.py`.

### Naturalistic matched pairs

- `research/umi-real05/README.md`;
- `research/umi-real05/METHODS.md`;
- `research/umi-real05/LITERATURE.md`;
- `research/umi-real05/data/BLINDED_EVIDENCE.csv`;
- `research/umi-real05/data/BLIND_PREDICTIONS.csv`;
- `research/umi-real05/data/RESULTS.json`;
- `research/umi-real05/data/CLAIM_LEDGER.csv`;
- `research/umi-real05/verify_umi_real05.py`.

## Traceability rule

Every numeric claim in the final manuscript must resolve to:

1. one repository source path;
2. one claim-ledger row;
3. one evidence class;
4. one verification receipt where computation is involved.

External literature claims must additionally resolve to a verified bibliographic record in the final BibTeX library.

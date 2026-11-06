# Coordinated Submission Sequence

## Recommended release order

### Stage 1 — Shared release freeze

Create one shared Zenodo software release containing:

- tribunal implementation and exact verifiers;
- frozen case matrices;
- benchmark packets and commitments;
- provenance and claim ledgers.

Create a separate Zenodo dataset record for benchmark and biological evidence tables if size or citation granularity warrants separation.

### Stage 2 — P2 public preprint

Release P2 to arXiv first because it defines the domain-general tribunal and terminology used by the companion biological paper.

Suggested primary category: `nlin.AO`.

### Stage 3 — P2b companion preprint

Release P2b to bioRxiv immediately after P2 has a stable identifier. P2b cites P2 for the general formal tribunal and contains the biological mechanism depth.

Suggested category: `Systems Biology`.

### Stage 4 — Journal submissions

Do not submit both manuscripts to the same journal simultaneously.

- P2: target broad systems/methods venues.
- P2b: target systems-biology or synthetic-biology venues.

## Cross-citation language

P2:

> A companion study applies the tribunal in depth to synthetic and systems biology, separating biological mechanism identity from motif occurrence and phenotype resemblance.

P2b:

> The domain-general formalism, cross-domain portfolio and blinded selectivity analyses are reported in the companion methods manuscript; the present work addresses biological mechanisms and evidence.

## Independence criterion

Each paper must remain understandable and publishable if the companion is delayed. Shared definitions may be restated briefly, but data, central figures and primary results must remain non-overlapping.

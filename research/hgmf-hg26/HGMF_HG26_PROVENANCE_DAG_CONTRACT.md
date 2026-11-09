# HGMF‑HG26 — Contrato del DAG de provenance

## Nodos

- raw artifact;
- acquisition receipt;
- calibration receipt;
- reset receipt;
- component extraction receipt;
- causal rectangle receipt;
- modal projection receipt;
- carrier-map receipt;
- holdout score receipt.

## Aristas

- `used`;
- `wasGeneratedBy`;
- `wasDerivedFrom`;
- `wasAssociatedWith`;
- `previousCycle`;
- `resetRoot`;
- `conformsToSeal`.

## Invariantes

1. DAG acíclico.
2. generation precedes later use.
3. every derived output has admitted parents.
4. every activity has code/environment and agent.
5. every magnetic cycle has a unique sequential parent.
6. every holdout output references the frozen analysis seal.
7. no admitted cell is silently overwritten.

## Hashes

- raw artifacts: SHA‑256 over bytes;
- receipt self-hash: SHA‑256 over canonical metadata excluding self-hash/signature;
- bundle manifest: sorted file path + SHA‑256;
- future data root: Merkle root over admitted receipt leaf hashes.

## Frontera

El DAG aporta chain-of-custody y reproducibilidad. No certifica por sí solo la corrección sustantiva de instrumento, calibración o modelo causal.

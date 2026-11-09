# HGMF‑HG26 — Perfil de provenance y RO‑Crate

## Base

El bundle se alinea con:

- W3C PROV: Entity, Activity, Agent, usage, generation, derivation and responsibility;
- RO‑Crate 1.2 metadata packaging;
- JSON Schema Draft 2020‑12;
- SHA‑256 para digests;
- canonical JSON subset para self-hashes.

## Mapeo

| HG26 | PROV | RO‑Crate |
|---|---|---|
| raw file | Entity | File |
| acquisition receipt | Entity | CreativeWork / File |
| acquisition | Activity | CreateAction |
| instrument | Agent/Entity specialized | IndividualProduct |
| operator | Agent | Person |
| software/commit | Entity/Agent | SoftwareApplication |
| component extraction | Activity | CreateAction |
| output table | Entity | File |
| analysis seal | Plan/Entity | CreativeWork |
| target grid | Collection/Entity | Dataset |

## Regla de cierre

Todo output derivado enlaza:

- `used` parents;
- `wasGeneratedBy` activity;
- `wasAssociatedWith` agents;
- `wasDerivedFrom` parents;
- code/environment identifiers.

## Frontera

RO‑Crate organiza y describe artefactos. W3C PROV expresa su genealogía. Ninguno sustituye los gates experimentales HGMF.

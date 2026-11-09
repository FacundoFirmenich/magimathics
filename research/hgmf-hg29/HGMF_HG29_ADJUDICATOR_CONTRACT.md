# HGMF‑HG29 — Contrato del adjudicator

El adjudicator recibe únicamente outputs confirmatorios ya derivados de receipts holdout admitidos.

## Nunca hace

- fit de modelo;
- selección de dirección;
- selección de carrier;
- imputación;
- selección de componente;
- cambio de kernel;
- corrección de p-values ausentes;
- pooling de carriers.

## Hace

1. valida presencia de los siete componentes;
2. exige holdout-only;
3. convierte discordancia direccional en p=1;
4. replica mediante max-p;
5. combina nuisance mediante max-p de todas las familias requeridas;
6. aplica la secuencia C -> M -> N -> X -> O;
7. compara contra alpha/7;
8. emite la claim máxima autorizada;
9. mantiene PHYSICAL_PROTOGEOMETRY=false.

## Failure closed

- missing p => ABSTAIN;
- missing nuisance family => ABSTAIN;
- missing carrier => ABSTAIN;
- non-holdout => ABSTAIN;
- optional order absent => conserva el nivel X si X pasó, sin inventar O.

# HGMF‑HG26 — Perfil de receipt de adquisición

## Required identity

- receipt profile/version;
- receipt id;
- carrier;
- experimental cell;
- raw artifact path/hash/size/type;
- acquisition timestamps;
- instrument/operator;
- protocol commit;
- environment digest;
- calibration receipts;
- reset root;
- previous-cycle receipt;
- provenance parents;
- train/holdout role;
- analysis seal;
- QC;
- self-hash.

## Magnetic cell key

```text
(wave, preset, field_mT, cycle)
```

## Adsorption cell key

```text
(wave, control_slot, reversal_depth)
```

## No-replacement rule

A cell may have multiple physical replicates only when a replicate axis and combination rule were preregistered. Otherwise, the second receipt is a `DUPLICATE_CELL`, not a replacement.

## No-filename authority

No experimental fact is inferred solely from a filename. Cell fields and ancestry live inside the receipt and are independently validated.

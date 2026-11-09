# HGMF‑HG26 — Scope del analysis seal

El `self_hash` del analysis seal compromete el contenido lógico del seal. Los hashes declarados en `files` corresponden a los bytes canónicos incluidos en el bundle descargable HG26.

Las copias visibles en GitHub son mirrors de revisión. Si una API normaliza whitespace o serialización, la autoridad criptográfica permanece en:

1. el bundle SHA‑256;
2. `HGMF_HG26_HASH_MANIFEST.csv` dentro del bundle;
3. los hashes de archivos declarados en el analysis seal;
4. el checker exacto ejecutado sobre esos bytes.

Toda adquisición futura debe referenciar el `analysis_seal_sha256` y no un hash inferido de una copia renderizada.

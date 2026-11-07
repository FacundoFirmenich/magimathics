# HGMF–UMI 01–09 · recuperación canónica

Esta carpeta persiste en **Magimathics** la serie HGMF‑UMI‑01…09 desarrollada después del hipercorpus inicial.

## Contenido

- `HGMF_UMI01_09_CANONICAL_TEXT_RECOVERY.tar.gz`: archivo de recuperación con el corpus textual exacto.
- Dentro del archivo:
  - `CANONICAL_TEXT_CORPUS.jsonl`: 112 archivos UTF‑8 preservados íntegramente —Markdown, CSV, JSON, Python, TeX y salidas de verificación—, un registro por línea.
  - `MANIFEST.json`: rutas originales, tamaños, SHA‑256 y límites de recuperación.
  - `BUNDLE_HASHES.json`: recibos de los bundles HGMF‑UMI‑01…09.
  - `SHA256SUMS.txt`: hashes internos.
  - `README.md`: instrucciones de reconstrucción.

## Estado de recuperación

- **UMI‑01 y UMI‑02:** reconstruidos desde la Library persistente de ChatGPT porque los ZIP originales ya no estaban montados. Se preservaron todos los archivos de texto, datos y código localizados; no se inventaron los visuales históricos faltantes.
- **UMI‑03 a UMI‑09:** representados desde los bundles completos que seguían montados; sus hashes de bundle quedan congelados dentro del archivo.
- Los 19 binarios/derivados no embebidos individualmente están enumerados con sus hashes y procedencia en `MANIFEST.json`.

## Integridad

```text
SHA-256 del archivo de recuperación:
600a66178b71ddfea12d03f8743e114822c6d483a3b126870a54a9022573e0b7

SHA-256 de CANONICAL_TEXT_CORPUS.jsonl:
8078f942d08e0c9cbb64bec55829acec0c46830c61163cd0577a31c94c055aa3
```

Verificación local:

```bash
sha256sum HGMF_UMI01_09_CANONICAL_TEXT_RECOVERY.tar.gz
tar -tzf HGMF_UMI01_09_CANONICAL_TEXT_RECOVERY.tar.gz
tar -xzf HGMF_UMI01_09_CANONICAL_TEXT_RECOVERY.tar.gz
```

## Regla de no borrado

Esta rama es estrictamente **aditiva**. No reescribe ni elimina `Ulalito's-Island`, las ramas `umi-real*`, las ramas de papers, los PR existentes ni ningún artefacto anterior.

## Reconstrucción exacta

Cada registro del JSONL contiene `path`, `bytes`, `sha256`, `encoding` y `content`. La reconstrucción consiste en escribir `content` como UTF‑8 en `path` y comprobar el SHA‑256 asociado.

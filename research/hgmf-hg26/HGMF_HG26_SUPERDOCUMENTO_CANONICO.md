# HGMF‑HG26 — Receipts de adquisición, integridad causal y sellado prospectivo

## 0. Veredicto vinculante

```text
PASS_RECEIPT_PROFILE
PASS_PROVENANCE_DAG_CONTRACT
PASS_CAUSAL_ANCESTRY_CONTRACT
PASS_ANALYSIS_SEAL
PASS_ADMISSION_VALIDATOR
PASS_RO_CRATE_MAPPING
PASS_CURRENT_ZERO-DATA_AUDIT

FAIL_DATA_ADMISSION
ABSTAIN_FIRST_EMPIRICAL_ADJUDICATION
HOLD_PHYSICAL_PROTOGEOMETRY
```

HG26 no adjudica resultados empíricos porque no existen receipts de adquisición para el target grid. Su cierre consiste en hacer que una futura ejecución sea auditable, no imputable y causalmente trazable.

## 1. Cinco niveles de autoridad

### L0 — identidad de bytes

El raw file posee un digest SHA‑256 verificable. Esto prueba que el archivo examinado coincide con los bytes hasheados.

### L1 — procedencia

El archivo se vincula con actividad de adquisición, instrumento, operador, software/firmware, calibración, timestamps y entidades usadas/generadas.

### L2 — admisibilidad experimental

La unidad pasa reset, calibración, secuencia/prefix closure, ausencia de duplicado de celda, QC y contrato de intervención.

### L3 — completitud causal

Las cuatro esquinas de cada rectángulo están observadas y admitidas. No se permite completar una esquina con modelo o interpolación.

### L4 — identificabilidad inferencial

El split, kernel family, components, nuisance class, tolerancias y scoring rules fueron sellados antes del holdout.

Ningún nivel implica automáticamente el siguiente.

## 2. Receipt de adquisición

Cada receipt raw debe declarar:

- perfil y versión;
- identificador;
- carrier;
- celda experimental;
- raw artifact con hash y bytes;
- actividad, agentes y software;
- calibración y reset;
- historia secuencial;
- split train/holdout;
- analysis seal;
- QC;
- self-hash canónico.

## 3. Causal ancestry

En magnetismo, para cada bloque `(wave,preset,field)`:

- ciclo 1 referencia el reset root;
- ciclo `c>1` referencia el receipt del ciclo `c-1`;
- todos los ciclos comparten el mismo reset root;
- timestamps respetan el orden;
- el DAG de parents es acíclico.

Una violación implica `QUARANTINE_CAUSAL_ANCESTRY`. No basta con que el filename contenga “cycle_5”.

## 4. Derivación

Todo componente, rectángulo, proyección modal o score debe incluir parents admitidos, code commit, environment digest, parameters hash, output hashes, activity, agents y timestamps. Un artefacto derivado sin closure queda `ORPHAN_DERIVATION`.

## 5. Seal prospectivo

El analysis seal fija por hash:

- schemas;
- validator;
- target grids;
- split waves 1–2 / wave 3;
- outputs `(A,B,C,K,E,Q,Z)`;
- kernel candidates;
- nuisance class;
- abstention rules;
- node/sign/modal scores.

Wave 3 no puede usarse para modificar esos elementos. Toda enmienda crea un nuevo seal y sólo puede aplicarse a datos todavía no observados.

## 6. Admission lattice

```text
RECEIVED
  -> BYTE_INTEGRITY_PASS
  -> SCHEMA_PASS
  -> PROVENANCE_CLOSURE_PASS
  -> CALIBRATION_PASS
  -> RESET_AND_PREFIX_PASS
  -> QC_PASS
  -> HOLDOUT_SEAL_PASS
  -> ADMITTED
```

Un error verificable produce `QUARANTINED`; información ausente produce `ABSTAIN_INCOMPLETE_RECEIPT`.

## 7. Target grids

Magnetismo:

\[
3\text{ fields}\times8\text{ cycles}\times3\text{ waves}=72.
\]

Adsorción:

\[
3\text{ control slots}\times8\text{ reversal depths}\times3\text{ waves}=72.
\]

Los slots de adsorción son de diseño; los valores físicos deben sellarse antes del primer run.

## 8. Current audit

No se encontraron acquisition receipts admitibles:

```text
0/72 magnetic
0/72 adsorption
0/42 magnetic adjacent rectangles
```

La salida empírica es `ABSTAIN_NO_RECEIPTS`.

## 9. Frontera

HG26 prueba que la futura evidencia puede tener cadena verificable, holdout materialmente sellado y derivaciones con ancestry. No prueba que un instrumento sea veraz sólo por tener hash, ni que exista señal, ni que HGMF sea físico.

## 10. Próxima frontera

`HGMF‑HG27 — Adquisición secuencial, stopping rules y presupuesto de evidencia`.

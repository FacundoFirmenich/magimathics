# HGMF‑HG25 — Auditoría de disponibilidad y corrección del backlog

## Estado certificado

La rama base y las ramas experimentales contienen:

- diseños;
- scripts;
- ledgers;
- resultados archivados de corpora públicos;
- protocolos future-only.

No contienen receipts de ejecución de:

- los 99 loop blocks UMI‑17;
- los 39 loops UMI‑22;
- los 18 loops HG23–HG25;
- los 72 runs homólogos del segundo carrier.

## Corrección conceptual

La frase “faltan 18 loops” sólo es verdadera bajo la precondición:

```text
UMI17 EXECUTED
AND UMI22 EXECUTED
```

Sin esa precondición, el grid magnético HG25 debe contabilizarse como 72 loops desde cero.

## Corpora públicos existentes

El corpus magnético UMI‑10 contiene cuatro whole loops, cada uno con una sola reversión. El corpus de adsorción contiene cuatro runs. Sirven para memoria/histéresis y model comparison, pero no realizan el diseño crossed field×cycle×wave de HG25.

Por tanto:

```text
PUBLIC CORPUS != HG25 INTERVENTION GRID
```

## Backlogs distintos

| Objeto | Unidades |
|---|---:|
| UMI‑17 robust bridge | 99 loop blocks |
| UMI‑22 extension | 39 loops |
| HG23/HG25 final magnetic increment | 18 loops |
| Programa magnético acumulado | 156 loops |
| Grid magnético específico HG25 | 72 loops |
| Segundo carrier | 72 runs |

El grid de 72 loops es un subconjunto del programa magnético acumulado de 156 loops, no 72 loops adicionales.

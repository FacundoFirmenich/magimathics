# HGMF‑HG33 — Jurisdicción de adsorción: Xe/Vycor scanning hysteresis

## Source object

El corpus UMI‑10 proviene de:

NIST-ISODB/AJBrownThesisIsotherms / Scanning_Isotherms/xe_scanning_isotherms.csv.

Metadata recuperada del propio archivo:

- adsorbent: Vycor Glass;
- adsorbent mass: 61.6 mg;
- adsorbate: Xe;
- molar mass: 131.293 g/mol;
- pressure: relative pressure;
- adsorption: mg;
- temperature: valores run-specific alrededor de 151 K;
- UMI‑10: runs 5, 8, 9 y 10.

La landing NIST contiene una mención 131 K, pero el repository README y el CSV analizado sitúan los scanning isotherms alrededor de 151 K. Para nuestra provenance manda el archivo realmente analizado.

## Historical standard model

NIST documenta que los datos de Brown se utilizaron originalmente para testar independent domain theory.

Cada domain tiene:

- empty/filled state;
- condensation pressure;
- evaporation pressure;
- history-dependent domain complexion.

Este core es matemáticamente Preisach-like.

## Successor physical models

La literatura de scanning isotherms en Vycor muestra que independent-domain behavior no cubre necesariamente:

- pore blocking;
- connectivity;
- cavitation;
- network percolation.

Los percolation/pore-network models son por tanto un successor physical core, no un optional decorative comparator.

## HG33 coverage

### Historical core

Independent-domain / scalar Preisach shell:

PASS_FINITE_PATH_OUTER_BOUND.

### Network core

Pore-network/percolation/pore-blocking/cavitation:

FAIL_ADSORPTION_PERCOLATION_NETWORK_ADAPTER.

### Conditional DFT layer

NLDFT/QSDFT or related DFT kernels require a material/pore model consistent with Xe/Vycor. They are not yet frozen.

## Claim boundary

Un eventual rechazo del independent-domain shell no autoriza una beyond-standard claim mientras el network/percolation null siga ausente.

Resultado:

ABSTAIN_ADSORPTION_PHYSICAL_NULL_CLOSURE.

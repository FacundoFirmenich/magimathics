# HGMF‑HG33 — Jurisdicción magnética: FGT/CrSBr

## Source object

Los cuatro loops de UMI‑10 provienen del directorio de minor loops con prior field del dataset de Kumar et al. sobre Fe3GeTe2/CrSBr.

Condiciones recuperadas:

- Fe3GeTe2 / CrSBr AFM/FM van der Waals heterostructure;
- anomalous Hall voltage \(V_{xy}\);
- 10 K;
- preset OOP de +2.5 T;
- source paper: FGT aproximadamente 87 ± 2 nm y CrSBr aproximadamente 30 ± 2 nm;
- current de 50 µA en la medición AHE.

## Mechanism in source paper

La explicación física fuente combina:

1. interfacial exchange coupling;
2. anisotropía OOP de FGT e IP de CrSBr;
3. flux-closure / stripe-like domains;
4. domain nucleation, propagation y annihilation;
5. estado cantado de CrSBr;
6. training effect: el primer loop tras preset presenta la asimetría/EB más marcada y los siguientes se vuelven gradualmente simétricos.

## Consecuencia para el null

### REQUIRED_PHYSICAL_CORE

FGT_CrSBr_INTERFACIAL_DOMAIN_TRAINING.

No existe aún en nuestro repo un mapa likelihood completo desde el modelo micromagnético/fenomenológico de la fuente hasta el \(V_{xy}\) de cada minor-loop trace.

Resultado:

FAIL_MAGNETIC_SOURCE_DOMAIN_MODEL_LIKELIHOOD_BRIDGE.

### PHENOMENOLOGICAL_CORE_CONTROL

Scalar Preisach.

Su uso es legítimo como shell de hysteresis/path dependence y ahora posee un finite-path likelihood upper bound.

### SECONDARY CONTROL

Jiles–Atherton/Duhem.

Es un modelo macroscópico estándar de histéresis ferromagnética, pero no debe sustituir al mecanismo interfacial/domain-specific identificado para esta heteroestructura.

## Claim boundary

Rechazar Preisach y Jiles–Atherton, aun si fuera posible, no excluiría el source-specific domain/exchange mechanism.

Por tanto el carrier magnético permanece:

ABSTAIN_MAGNETIC_PHYSICAL_NULL_CLOSURE.

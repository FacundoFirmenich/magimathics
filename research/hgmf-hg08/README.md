# HGMF‑HG08 — Peso cuadrático, typicality frecuencial y chance de caso único

**Veredicto:** `PASS_FINITE_FREQUENCY_TYPICALITY / PASS_EXCHANGEABILITY_BOUNDARY / PASS_SEMANTIC_UNDERDETERMINATION / FAIL_SINGLE_CASE_BRIDGE / HOLD_FULL_BORN`.

## Resultado central

Bajo preparación producto independiente y peso cuadrático `q`, la frecuencia exacta es binomial y se concentra exponencialmente alrededor de `q`.

Pero:

- exchangeability no implica IID;
- typicality no implica actuality;
- frecuencia límite no implica chance individual;
- decisión racional no implica chance objetiva;
- propensity, credencia o chance requieren un puente semántico adicional.

## Teoremas

1. `W_N(k)=C(N,k) q^k(1-q)^(N-k)` y satisface bounds finitos de Hoeffding/Chernoff.
2. `q` es el centro único de concentración bajo el contrato producto-IID.
3. Una ley exchangeable es una mezcla de leyes IID; el marginal de una copia no fija la mezcla.
4. La secuencia mecánica determinista `x_n=floor((n+1)q)-floor(nq)` tiene frecuencia límite `q` con error `<1/N`, sin chance estocástica.
5. El mismo peso cuadrático admite semánticas incompatibles: chance, branch typicality, decisión, credencia y propensity.

## Born boundary

```text
BORN FUNCTIONAL FORM = PASS CONDITIONAL
FINITE-N FREQUENCY TYPICALITY = PASS
IID/PRODUCT ASSUMPTION = REQUIRED
TYPICALITY-TO-ACTUALITY = EXTRA PRINCIPLE
SINGLE-CASE CHANCE = FAIL/HOLD
FULL BORN DERIVATION = HOLD
```

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `FREQUENCY_TYPICALITY_PASS / SINGLE_CASE_CHANCE_FAIL_HOLD`.

## Next gate

`HGMF‑HG09 — Rol funcional de chance, calibración e intervención`.

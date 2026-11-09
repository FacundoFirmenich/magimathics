# HGMF‑HG33 — Carrier-specific standard-null tribunal

## Veredicto

PASS_SOURCE_PROVENANCE_RECOVERY  
PASS_MAGNETIC_JURISDICTION_RECOVERY  
PASS_ADSORPTION_JURISDICTION_RECOVERY  
PASS_FINITE_PATH_PREISACH_PATTERN_THEOREM  
PASS_PREISACH_IDT_OUTER_LIKELIHOOD_BOUND  
PASS_SINGLE_PATH_PREISACH_POWER_NOGO  
PASS_ADSORPTION_IDT_HISTORICAL_MATCH  
PASS_MAGNETIC_PREISACH_PHENOMENOLOGICAL_CONTROL  

FAIL_MAGNETIC_SOURCE_DOMAIN_MODEL_LIKELIHOOD_BRIDGE  
FAIL_ADSORPTION_PERCOLATION_NETWORK_ADAPTER  
FAIL_COMPLETE_CARRIER_STANDARD_NULL_ENVELOPE  

ABSTAIN_MAGNETIC_PHYSICAL_NULL_CLOSURE  
ABSTAIN_ADSORPTION_PHYSICAL_NULL_CLOSURE  
ABSTAIN_EMPIRICAL_ADJUDICATION  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. Provenance recuperada

### Magnetismo

Los cuatro public minor loops de UMI‑10 provienen del dataset de Kumar et al.:

- Fe3GeTe2 / CrSBr van der Waals heterostructure;
- anomalous Hall voltage;
- 10 K;
- +2.5 T OOP preset;
- FGT ≈ 87 ± 2 nm;
- CrSBr ≈ 30 ± 2 nm.

El source paper atribuye la asimetría a interfacial exchange, competing orthogonal anisotropies, flux-closure/stripe domains, domain nucleation/propagation y training effect.

Por tanto el physical core null no puede reducirse a Jiles–Atherton.

### Adsorción

El corpus es:

- Xe;
- Vycor Glass;
- 61.6 mg;
- relative pressure;
- scanning hysteresis;
- run-specific temperatures alrededor de 151 K;
- UMI‑10 runs 5, 8, 9, 10.

NIST documenta que Brown utilizó estos scanning isotherms para independent domain theory y que successor explanations incluyen network/percolation approaches.

## 2. Corrección de temperatura

Una landing NIST menciona 131 K. El repository README y el CSV usado contienen scanning data alrededor de 151 K.

En provenance, el objeto realmente analizado domina sobre el prose summary:

\[
\boxed{\text{ANALYZED FILE METADATA}>\text{LANDING-PAGE SUMMARY}.}
\]

## 3. UMI‑10 rpm_relays

UMI‑10 construía una grid finita de relays y después ajustaba Ridge sobre sus features.

Eso era un **useful operator shell**, pero no una identificación del full physical Preisach/IDT family.

HG33 corrige esa frontera.

## 4. Finite-path Preisach theorem

En cualquier trayectoria finita hay sólo finitísimos relay patterns distintos, aunque los thresholds sean continuos.

Así se puede enumerar exactamente el set de patterns sin elegir una discretización física arbitraria.

Cualquier scalar Preisach/IDT relay superposition queda contenida en el span de esos patterns.

## 5. Likelihood outer bound

Si \(X_R\) contiene intercept, reversible basis y todos los patterns:

\[
\mathcal M_{\rm physical}\subseteq\operatorname{col}(X_R).
\]

Luego:

\[
\sup_{\mathcal M_{\rm physical}}L
\le
\sup_{\beta}L(y;X_R\beta,\Sigma).
\]

El lado derecho es un GLS profile exacto y, por tanto, un valid null-likelihood upper bound para HG31 universal inference.

## 6. Single-path no-go

Para una strictly monotone path, relay step functions más intercept generan \(\mathbb R^T\).

Para un generic single-reversal path, los relays generan interval indicators que permiten igualmente rango completo.

Entonces:

\[
\operatorname{rank}(X_R)=T,
\]

y:

\[
E_X\le1.
\]

Así un unrestricted Preisach outer null no es confirmatoriamente falsable por un único loop simple.

## 7. Qué debe sustituir ese intento

Preisach/IDT debe atacarse mediante:

- return-point memory;
- wiping-out;
- congruency;
- Everett-function consistency;
- cross-history shared-density constraints;
- physically bounded density families.

Esto revaloriza el tipo de whole-history tests ya iniciado en UMI‑10.

## 8. Magnetismo

El source-specific FGT/CrSBr mechanism sigue sin likelihood bridge directo hacia los minor-loop AHE traces.

Precio científico:

ABSTAIN_MAGNETIC_PHYSICAL_NULL_CLOSURE.

Preisach es un control fenomenológico. Jiles–Atherton es secondary control. Ninguno reemplaza el physical source model.

## 9. Adsorción

Independent-domain/Preisach shell está formalizado.

Pero el physical successor null de pore connectivity, pore blocking, cavitation y percolation continúa ausente.

Precio científico:

ABSTAIN_ADSORPTION_PHYSICAL_NULL_CLOSURE.

## 10. Próxima frontera

HGMF‑HG34 — Structural Everett/Preisach falsifiers, source-specific magnetic domain-state likelihood y adsorption percolation adapter.

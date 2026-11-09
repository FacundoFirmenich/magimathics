# HGMF-HG35 — Quantitative standard-null bridge

**Fecha:** 9 de noviembre de 2026

## Veredicto preliminar del gate

PASS_MAGNETIC_SOURCE_INTERVAL_NULL  
PASS_MAGNETIC_TRAINING_LAW_DIAGNOSTIC  
PASS_VYCOR_BETHE_TOPOLOGY_CORE  
PASS_PUBLISHED_XE_VYCOR_NETWORK_NULL_EXISTS  
PASS_NETWORK_CONNECTIVITY_RANGE_FREEZE  

FAIL_FULL_MAGNETIC_VXY_LIKELIHOOD_BRIDGE  
FAIL_COMPLETE_XE_VYCOR_OBSERVATION_LIKELIHOOD  
FAIL_BEYOND_STANDARD_CLAIM_FROM_HG34_RPM_RESIDUALS  

ABSTAIN_UNIVERSAL_EVALUE_X  
ABSTAIN_PHYSICAL_IDT_REJECTION  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG35 separa tres niveles: structural null, quantitative observation null y confirmatory likelihood/e-value null.

Para FGT/CrSBr, el source paper soporta un null cuantitativo sobre summaries de training: loop 1 metastable/exchange-biased; loops posteriores con exchange bias aproximadamente cero y switching simétrico. Con los field-resolution bounds del propio loader, el primer loop excluye cero y los loops 2–5 incluyen cero. Esto da un source-specific interval null cuantitativo sin convertir el field step en un sigma.

El source repository contiene theoretical magnetization profiles M/MS de CrSBr y FM/AFM profiles, pero no un observation model probabilístico que produzca Vxy(H). El full likelihood bridge sigue abierto.

Para Xe/Vycor, la literatura estándar ya contiene un network null directamente aplicado al benchmark Brown. Mason (1988) aplicó un cavity/window Bethe-tree model a los scanning isotherms de Brown, Xe/Vycor 151 K. Cimino et al. (2013) obtuvieron para Vycor effective coordination z≈6.6–7.2 y qc≈0.16–0.18; z=6.6 reproduce bien los scanning desorption curves salvo la scan más baja.

HG35 implementa el topology core exacto de ese Bethe model:

Qp(q)=1-y^z,
y=(1-q)+q y^(z-1)

y para scanning desorption:

alpha(q,Q+)=1-y^z,
y=(1-q)+q(1-Q+) y^(z-1),
Q-=Q+ +(1-Q+) alpha.

El bridge completo a adsorption mass requiere reference isotherms Vs(p), Vc(p) y q(p). Esos objetos no están congelados todavía en nuestro pipeline.

## Consecuencia

Los residuos RPM de HG34 no son evidencia beyond-standard: existe una familia estándar network/percolation históricamente aplicada al mismo benchmark que aún no fue excluida por nuestro tribunal.

## Próxima frontera

HGMF-HG36 — Reconstruct Vycor reference isotherms Vs/Vc and q(p); source-summary likelihood for magnetic training; complete standard X denominator.

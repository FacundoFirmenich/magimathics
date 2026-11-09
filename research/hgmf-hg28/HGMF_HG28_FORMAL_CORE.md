# HGMF‑HG28 — Núcleo formal

## 1. Componentes y nivel global

Sea

\[
J=\{A,B,C,K,E,Q,Z\},
\qquad \alpha=0.05,
\qquad \alpha_j=\alpha/7=1/140.
\]

No se promedian componentes.

## 2. Cadena por componente

Para cada \(j\in J\):

\[
C_j\to M_j\to N_j\to X_j\to O_j.
\]

Todos los nodos se prueban al mismo nivel local \(\alpha_j\), pero sólo si todos los nodos previos de esa cadena fueron rechazados.

La cadena fija controla su FWER a \(\alpha_j\). Por Bonferroni entre siete cadenas:

\[
\mathrm{FWER}_{global}
\le\sum_j\alpha_j
=\alpha.
\]

No se requiere independencia entre componentes ni entre carriers.

## 3. Replicación 2/2

Para un nodo y componente dados, sean \(p_{M,j}\) y \(p_{A,j}\) p-values válidos en los dos carriers, calculados sólo con holdout. Defina

\[
p_{rep,j}=\max(p_{M,j},p_{A,j}).
\]

Bajo el null de no replicación, al menos uno de los carrier-null es verdadero, por lo que

\[
\Pr(p_{rep,j}\le t)\le t.
\]

Así, \(p_{rep}\) es válido sin asumir independencia.

## 4. Dirección

La dirección se aprende sólo en waves 1–2 y se congela antes de wave 3. Si el mapa QGT/UMI invierte orientación, el signo se transporta antes de comparar carriers.

Un componente sin dirección estable en training queda ABSTAIN_DIRECTION_UNSTABLE.

## 5. Holdout

Todos los p-values confirmatorios proceden de wave 3. Training puede seleccionar dirección, kernel, modal blocks, nodal targets, carrier map y order contexts. No puede contribuir a la estadística confirmatoria final.

## 6. Fixed final mode

HG28 adopta definitivamente NO EARLY EFFICACY y ONE FINAL CONFIRMATORY LOOK. QC y futilidad ciega siguen disponibles según HG27.

## 7. Order module

El order node \(O_j\) es un claim mecanístico opcional situado al final de la cadena. No es requisito para una candidate signature genérica.

## 8. Claim boundary

Una cadena que alcanza \(X_j\) autoriza CANDIDATE_BEYOND_STANDARD_COMPONENT_SIGNATURE.

No autoriza PHYSICAL_PROTOGEOMETRY, que requiere replicación externa adicional y una atribución física más fuerte.

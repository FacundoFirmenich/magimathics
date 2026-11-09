# HGMF‑HG29 — Especificación ejecutable de tests

## Causal

Input:

- 24 holdout estimates;
- 24×24 covariance;
- fixed 14×24 rectangle matrix;
- 14-vector training template.

Output:

- z;
- one-sided p;
- variance;
- status.

ABSTAIN si covariance/template no son válidos.

## Modal

Input:

- modal coefficient vector;
- covariance;
- training-frozen modal prediction.

Output:

- matched-filter z/p;
- weighted residual diagnostic.

La confirmación es alignment predictivo, no aceptación de goodness-of-fit por no-rechazo.

## Nodal

Input:

- flank estimates;
- standard errors;
- expected signs.

Output:

- one-sided flank p-values;
- IUT p-value = max flank p.

No se prueba “distancia pequeña” con una tolerancia inventada.

## Nuisance

Input:

- un p-value predictivo calibrado por cada familia requerida.

Output:

\[
p_X=\max p_k.
\]

Missing family => ABSTAIN.

## Order

Input:

- ocho paired differences holdout por carrier;
- training-frozen direction.

Output:

- exact one-sided sign-test p-value;
- number positive/negative/ties.

## Replication

Cada nodo:

\[
p_{rep}=\max(p_{mag},p_{ads}).
\]

## Gatekeeping

Alpha por componente:

\[
1/140.
\]

Chain:

Causal -> Modal -> Nodal -> FrozenNuisanceExclusion -> optional Order.

El adjudicator nunca rellena un p-value ausente, nunca selecciona el mejor carrier y nunca salta un gate.

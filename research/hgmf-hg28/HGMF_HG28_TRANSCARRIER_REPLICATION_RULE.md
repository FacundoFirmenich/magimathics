# HGMF‑HG28 — Regla de replicación transcarrier

Para un componente \(j\) y un nodo confirmatorio, el null de replicación es

\[
H^{rep}_{0,j}
=
H^{mag}_{0,j}\cup H^{ads}_{0,j}.
\]

Rechazarlo significa que ambos carriers contienen señal en la dirección preregistrada.

La regla es

\[
\boxed{p^{rep}_j=\max(p^{mag}_j,p^{ads}_j).}
\]

Es un intersection-union test válido bajo dependencia arbitraria.

## Signo

1. training congela una dirección;
2. el mapa transcarrier congela orientación;
3. holdout se prueba one-sided en la dirección transportada;
4. signos discordantes producen \(p^{rep}=1\) para la claim direccional.

## Missing carrier

Si un carrier está ausente, quarantined o carece de test válido: ABSTAIN_REPLICATION.

No sustituyen replicación:

- pooled mean;
- meta-analysis dominado por un carrier;
- Fisher combination;
- overall significant;
- mejor carrier;
- carrier selection posterior.

# HGMF‑HG29 — Teorema de la envolvente nuisance y no-go de la clase irrestricta

## 1. Envelope finita

Sea una colección preregistrada

\[
\mathcal N^\star=\{N_1,\ldots,N_K\}.
\]

Cada \(N_k\) incluye:

- algoritmo de fit training-only;
- complejidad/regularización elegida sin holdout;
- predictive distribution de wave 3;
- discrepancy statistic congelado;
- p-value predictivo calibrado.

El null global es

\[
H_0^X=\bigcup_k H_{0,k}.
\]

La regla

\[
p_X=\max_k p_k
\]

es un intersection-union test válido del union null.

## 2. Envolvente mínima requerida

HG29 exige como mínimo adapters para:

1. drift/control baseline;
2. finite hidden-state response;
3. bounded-memory process-tensor response;
4. alternative standard spectral-kernel response;
5. hidden-ancilla/control-geometry response.

Outcome rescaling se trata como una órbita de invariancia dentro de cada familia, no como una familia independiente.

## 3. Split predictive calibration

Cada familia se ajusta sólo con training y se critica sobre holdout. Un split/holdout predictive check evita la reutilización del mismo dato para fit y crítica.

## 4. No-go de clase saturada

Sea \(\mathcal P\) la clase de distributions observables sobre el target experiment. Si el null nuisance contiene \(\mathcal P\), entonces cualquier test de nivel \(\alpha\),

\[
\sup_{P\in H_0}E_P[\phi]\le\alpha,
\]

satisface también

\[
E_P[\phi]\le\alpha
\]

para toda alternativa observable \(P\in\mathcal P\). No existe potencia no trivial contra esas alternativas.

Por tanto, una nuisance class suficientemente saturada no es falsable por el mismo dataset.

## 5. Aplicación a process tensors

El process-tensor framework es una representación general de procesos multitiempo no-Markovianos. Sin bounds físicos o computacionales sobre memoria, dimensión/bond dimension, estructura o algoritmo, usar “process tensor estándar” como un único null irrestricto haría vacía la exclusión.

HG29 exige una familia bounded y preregistrada. Rechazarla significa únicamente que la envolvente congelada falló predictivamente.

# HGMF‑HG08 — Núcleo formal

## Concentración producto

Para preparaciones tensor-product y un evento binario de peso `q`:

\[
W_N(k)=\binom Nk q^k(1-q)^{N-k}.
\]

La frecuencia `f_N=k/N` satisface

\[
W_N(|f_N-q|\ge\varepsilon)\le 2e^{-2N\varepsilon^2}.
\]

Para todo centro `r != q` y `delta < |r-q|`, el peso de `|f_N-r| <= delta` decrece exponencialmente.

## Exchangeability

Una familia exchangeable infinita es una mezcla de leyes IID:

\[
P_N(k)=\int\binom Nk\theta^k(1-\theta)^{N-k}d\nu(\theta).
\]

El marginal de una copia

\[
\bar q=\int\theta d\nu(\theta)
\]

no determina `nu` ni fuerza concentración alrededor de `bar q`.

## Secuencia determinista típica

Para

\[
x_n=\lfloor(n+1)q\rfloor-\lfloor nq\rfloor,
\]

\[
\sum_{n=0}^{N-1}x_n=\lfloor Nq\rfloor,
\]

y el error frecuencial es menor que `1/N` pese a que cada outcome está fijado.

## No-go semántico

La estructura matemática de HG07-HG08 admite expansiones semánticas incompatibles: chance objetiva, typicality, decisión, credencia, propensity y determinismo típico. Ninguna queda seleccionada sin axioma puente.

## Corolario

\[
\text{frequency typicality}\not\Rightarrow\text{single-case chance}.
\]

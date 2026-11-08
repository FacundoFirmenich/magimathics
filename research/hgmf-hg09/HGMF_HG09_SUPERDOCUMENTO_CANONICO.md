# HGMF‑HG09 — Rol funcional de chance, calibración e intervención

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / OPERATIONAL ROLE / DETERMINISTIC DILATION / SEMANTIC BOUNDARY`  
**Veredicto:** `PASS_OPERATIONAL_CHANCE_ROLE_CONDITIONAL / FAIL_SINGLE-CASE CHANCE UNIQUENESS / HOLD FULL BORN`

## 0. Resultado rector

El peso cuadrático q satisface, condicionalmente al kernel operacional y a la preparación producto, un rol completo de forecast:

- calibración;
- optimalidad bajo scores estrictamente propios;
- estabilidad bajo preparaciones operacionalmente equivalentes;
- sensibilidad causal a intervenciones;
- screening-off de la historia bajo estado operacional suficiente.

Pero ese rol no identifica azar intrínseco. Todo kernel puede representarse como una dinámica determinista sobre un estado ampliado con una variable auxiliar. Por tanto:

\[
\boxed{\text{operational chance role}\not\Rightarrow\text{primitive stochasticity}.}
\]

## 1. Tres nociones de chance

### Rol predictivo

q es el único reporte que minimiza la pérdida esperada bajo todo score estrictamente propio dentro del kernel declarado.

### Rol causal

Intervenciones que cambian la preparación cambian q y las frecuencias futuras en la dirección predicha.

### Rol modal irreducible

Manteniendo fijo el estado físico completo y las leyes, persisten varios outcomes posibles con peso no trivial.

HG09 cierra los dos primeros condicionalmente. El tercero no queda identificado.

## 2. Calibración y scores propios

Para un outcome Bernoulli Y y reporte r:

\[
L_{\rm Brier}(r;q)=q(1-r)^2+(1-q)r^2
=q(1-q)+(r-q)^2.
\]

El mínimo único es r=q.

Para log-loss:

\[
L_{\log}(r;q)=-q\log r-(1-q)\log(1-r),
\]

el mínimo único también es r=q.

Así q ocupa un rol predictivo único dentro del modelo. Esto no demuestra qué tipo de entidad física es q.

## 3. Intervención

En el modelo umbral:

\[
Y=\mathbf1_{\{U<q\}},
\]

una intervención do(q=q') produce frecuencia q'. La auditoría determinista utiliza una malla fija de 10.000 estados ocultos y obtiene error menor o igual a 1/(2N), sin aleatoriedad en los outcomes individuales.

La sensibilidad causal del output a q no distingue chance primitiva de una regla determinista con microestado oculto.

## 4. Teorema de dilatación determinista

Para cualquier kernel K(x,dy) sobre un espacio de outcomes estándar existe una función medible f(x,u), con u en [0,1], tal que el pushforward de la medida uniforme reproduce K.

En el caso finito, se particiona [0,1] en intervalos cuyas longitudes son las probabilidades del kernel.

Por tanto, todo perfil operacional de probabilidades condicionales puede reproducirse mediante:

\[
Y=f(X,U).
\]

Condicionado en el estado completo (X,U), el outcome es determinista.

## 5. Screening-off

Sea el hidden state una secuencia completa de bits y la dinámica el shift determinista. Bajo la medida producto uniforme, los outcomes observados son IID y la preparación q bloquea la historia operacional.

No obstante, dado el seed completo:

\[
H(Y_{1:N}\mid\text{seed})=0.
\]

Screening-off operacional y determinismo ontológico son compatibles.

## 6. Calibration no selecciona chance

Una secuencia determinista puede ser perfectamente calibrada por bloques y responder a intervenciones q sin que exista chance individual.

La calibración evalúa la relación entre predicciones y resultados. No caracteriza por sí sola la ontología generadora.

## 7. Principal Principle

El Principal Principle prescribe deference credencial a una chance ya identificada. No identifica qué magnitud es chance. Utilizarlo para definir chance y luego usar chance para justificar deference sería circular.

El peso q puede ser estrictamente propio y calibrado sin que quede decidida su lectura como chance objetiva, typicality, credencia o medida de ensemble.

## 8. No-go del caso único

La representación funcional muestra que el mismo kernel, las mismas intervenciones, la misma calibración y el mismo screening-off admiten:

- una lectura estocástica primitiva;
- una lectura determinista con estado oculto medido;
- una lectura de typicality;
- una lectura de chance funcional determinista.

Ningún test formulado sólo en el nivel del kernel observado separa esas ontologías.

## 9. Veredicto Born

```text
BORN FUNCTIONAL FORM = PASS CONDITIONAL
FREQUENCY TYPICALITY = PASS
OPERATIONAL FORECAST ROLE = PASS CONDITIONAL
CAUSAL INTERVENTION ROLE = PASS CONDITIONAL
INTRINSIC SINGLE-CASE CHANCE = FAIL/HOLD
FULL BORN DERIVATION = HOLD
```

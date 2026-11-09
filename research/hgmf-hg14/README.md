# HGMF‑HG14 — Dinámica canónica de contacto y falsadores helicoidales

**Veredicto:** `PASS_CONTACT_DYNAMIC_SELECTION_CONDITIONAL / PASS_RELATIVE_PHASE_FALSIFIER / FAIL_INTRINSIC_ABSOLUTE_HELICAL_SELECTION`.

## Resultado rector

La acción de Dirac–Frenkel selecciona el flujo de Schrödinger en la esfera unitaria y su descomposición única en componente horizontal y componente de Reeb:

\[
X_H=-\frac{i}{\hbar}(H-\langle H\rangle)\psi
-\frac{\langle H\rangle}{\hbar}R.
\]

La componente vertical absoluta permanece gauge porque `H -> H + cI` no cambia el rayo. En dos ramas coherentes, en cambio, la conexión relativa

\[
\mathcal A_{rel}=\mathcal A_1-\mathcal A_2
\]

sobrevive al cociente por la fase diagonal y vuelve observable la diferencia de Reeb:

\[
\nu_{rel}=-\frac{\langle H_1\rangle-\langle H_2\rangle}{\hbar}.
\]

Por tanto, la helicoidalidad físicamente defendible es relacional, no absoluta.

## Falsadores

- shift común: señal relativa nula;
- shift diferencial: misma trayectoria de rayos y fase `-cT/hbar`;
- loop y loop inverso: parte even = drift dinámico; parte odd = holonomía geométrica;
- residual de fase frente a longitud: cero, lineal o no lineal para pitch cero, constante o variable;
- pérdida de referencia: desaparece la señal vertical relativa;
- echo: elimina drift y conserva holonomía geométrica.

## Auditoría

- 400 descomposiciones de contacto;
- error máximo de conexión `2.22e-16`;
- error máximo de horizontalidad `7.89e-16`;
- infidelidad máxima de rayo bajo shift diferencial `1.11e-15`;
- error de fase `4.97e-16`;
- recuperación forward/reverse al nivel de precisión de máquina.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `RELATIONAL_CONTACT_HELICAL_FLOW_PASS_CONDITIONAL / ABSOLUTE_HELICITY_FAIL / SPIN HOLD`.

## Next gate

`HGMF‑HG15 — Dinámica relacional de reloj y falsabilidad protogeométrica`.

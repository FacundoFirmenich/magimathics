# HGMF‑HG26 — Núcleo formal de provenance y admisión

## 1. Entidades, actividades y agentes

Sea el provenance graph:

\[
\mathcal P=(E,A,G,U,D,R),
\]

donde \(E\) son entidades, \(A\) actividades, \(G\) agentes, \(U\) usos, \(D\) derivaciones y \(R\) asociaciones/responsabilidades.

Toda entidad derivada admitida debe poseer una actividad generadora y parents admitidos.

## 2. Integridad no implica validez

Sea

\[
H:\{0,1\}^*\to\{0,1\}^{256}
\]

el digest SHA‑256. La igualdad \(H(x)=h\) certifica identidad respecto de \(h\), no la verdad experimental de \(x\):

\[
\text{HASH_PASS}
\not\Rightarrow
\text{CALIBRATION_PASS}
\not\Rightarrow
\text{CAUSAL_ADMISSIBLE}.
\]

## 3. Self-hash

Sea \(R^{-}\) el receipt sin `self_hash` ni `signature`. El perfil canónico HG26 serializa \(R^{-}\) en UTF‑8, con keys ordenadas, sin whitespace y sin floats no exactos:

\[
h_R=\operatorname{SHA256}(\operatorname{canon}(R^{-})).
\]

## 4. Provenance closure

Un conjunto de receipts es cerrado si:

1. todo parent declarado existe;
2. todo output deriva de parents admitidos;
3. toda actividad posee agente;
4. generation precede usages posteriores;
5. el parent graph es acíclico.

## 5. Ancestry prefix-closed

Para un bloque magnético \(B=(w,p,f)\), sea \(r_c\) el receipt de ciclo \(c\). Se exige:

\[
\operatorname{parent}(r_1)=r_{reset},
\]

\[
\operatorname{previous}(r_c)=r_{c-1}\quad(c>1),
\]

y un reset root común. Si falta \(r_j\), ningún \(r_c\) con \(c>j\) recibe autoridad prefix-closed.

## 6. Unicidad de celda

Para la key experimental \(k(r)\):

\[
r\neq r'\Rightarrow k(r)\neq k(r')
\]

entre receipts admitidos. Réplicas requieren eje y combinación preregistrados; no se permite overwrite silencioso.

## 7. Holdout independence

Si cualquier elemento del analysis seal se modifica después de acceder a wave 3, el score deja de ser un holdout prospectivo bajo ese seal.

## 8. Rectángulos

Un rectángulo causal sólo se admite cuando sus cuatro acquisition receipts están `ADMITTED` y comparten carrier, wave, component extraction version, calibration jurisdiction y ancestry contract.

## 9. Frontera

Provenance closure es condición necesaria para auditabilidad, no condición suficiente para causalidad o verdad física.

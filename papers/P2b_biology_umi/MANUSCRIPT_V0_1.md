# Minimal Invariant Relational Units in Synthetic and Systems Biology
## An intervention tribunal across oscillation, adaptation, memory, proofreading, patterning and autocatalytic closure

### Abstract

Biological networks are commonly decomposed into motifs, modules and design principles, but a recurrent topology is not by itself a biological unit: the same graph may support different dynamics, and different molecular implementations may realize the same function. We develop a relation-first intervention tribunal for identifying **minimal invariant relational units** (UMIs) in synthetic and systems biology. Under a declared biological jurisdiction, a candidate must realize a frozen semantic signature, preserve it under admissible component, parameter or substrate substitution, lose it under critical relation ablation or cardinality-preserving rewiring, transport across at least two implementations, and contain no proper subcarrier that retains the full signature. We apply the tribunal to six mechanism classes: closed cyclic repression in the repressilator; constant-signal internal-model closure in robust perfect adaptation; regenerative bounded writeable closure in bistable genetic memory; driven multistage rejection in kinetic proofreading; finite-wavenumber reaction–transport instability in synthetic Turing patterning; and reflexively autocatalytic food-generated closure. Exact and computational analyses are combined with primary experimental evidence without treating model counterfactuals as wet-lab results. The repressilator carrier survives cyclic relabeling and cross-substrate implementation but loses sustained phase-ordered oscillation under every critical edge deletion or frozen rewiring. Robust perfect adaptation is transported across bacterial chemotaxis, antithetic biomolecular controllers, cell-free systems and mammalian circuits, whereas proportional regulation and broken sensor–integrator–actuator closures fail. Biological phenotype decoys—equilibrium recognition for proofreading and instructed stripe formation for Turing patterning—are rejected despite superficial output similarity. A quorum-sensing competence switch is assigned abstention because current evidence does not identify a unique minimal carrier. The tribunal does not replace network-motif, control-theoretic or organisational-closure theories; it provides a common intervention grammar for deciding when a biological relation class warrants treatment as a unit.

**Keywords:** systems biology; synthetic biology; network motifs; gene circuits; causal intervention; robust perfect adaptation; bistability; kinetic proofreading; Turing patterns; autocatalytic sets

---

## 1. Introduction

The search for biological building blocks has produced a rich hierarchy of concepts: genes and proteins, pathways, network motifs, modules, dynamical motifs, control architectures, autocatalytic sets and organisational closures. Each captures a different aspect of biological unity. Yet none of these labels alone answers a practical experimental question:

> Which relational configuration is the smallest carrier of a declared biological function, and how can that carrier be distinguished from a structural lookalike or a phenotypic decoy?

Network motifs are recurrent subgraphs found more often than expected under a null model. They have transformed the study of regulatory networks, but structural recurrence does not determine function. A signed topology can exhibit different dynamics across parameter regimes, and similar dynamics can arise from different molecular substrates. Synthetic biology makes this problem particularly visible. The repressilator is not simply three proteins; the toggle switch is not simply two repressors; antithetic feedback is not simply two sequestration species. Their biological identity depends on how relations, kinetics, memory and boundary conditions close a function.

Control theory and systems biology provide stronger domain-specific results. Integral feedback explains robust perfect adaptation. Opposer and balancer modules generate topological bases for adaptation. Kinetic proofreading explains beyond-equilibrium discrimination. Turing theory specifies a transport-induced instability, not merely a spatial stripe. RAF theory distinguishes collectively autocatalytic closure from an open catalytic chain. These theories identify mechanism classes, but their evidential grammars differ and are rarely compared through one frozen intervention protocol.

We introduce an operational criterion for a biological unit. A **minimal invariant relational unit** (UMI) is an inclusion-minimal relation class that preserves a strict biological semantic signature under admissible substitutions and transports, while losing that signature under critical ablation or rewiring. The definition is jurisdictional. It includes the relevant kinetic and physical regime and does not claim a context-free or ontological atom.

The manuscript has four aims. First, it adapts the general UMI tribunal to biological evidence, separating direct experiments, physical perturbations, mechanistic models and exact results. Second, it provides detailed adjudications across six biological mechanism classes. Third, it tests mechanism–phenotype distinctions using matched decoys. Fourth, it identifies where the tribunal must abstain because biological causality is mixed or insufficiently resolved.

---

## 2. Biological jurisdiction and evidence architecture

### 2.1 Biological UMI carrier

A candidate biological carrier is represented as

\[
C=(V,R,\Theta,E),
\]

where:

- \(V\) is the molecular, cellular or reaction-component set;
- \(R\) is a typed and signed relation set;
- \(\Theta\) is the admissible kinetic, thermodynamic and spatial regime;
- \(E\) is the environmental and experimental context included in the jurisdiction.

The inclusion of \(\Theta\) and \(E\) prevents a bare graph from being treated as a mechanism. A negative-feedback loop may stabilize, oscillate or fail depending on gain, delay, nonlinearity and timescale. A spatial circuit may form a Turing pattern only under a specific mobility contrast and local stability regime.

### 2.2 Strict semantic signature

A biological signature specifies function, horizon and tolerance. Examples are:

- sustained limit-cycle oscillation with cyclic phase order;
- return to the same setpoint after a persistent perturbation;
- two bounded persistent states plus controlled set/reset;
- discrimination beyond the equilibrium limit at nonzero throughput;
- spontaneous finite-wavenumber patterning from a homogeneous state;
- collective autocatalytic and food-generated closure.

A weaker phenotype is not silently substituted for the declared function.

### 2.3 Evidence classes

We distinguish:

- `T1`: exact theorem, algebraic proof or exhaustive finite result;
- `M1`: explicit mechanistic model;
- `P1`: direct physical experiment;
- `P2`: physical intervention or perturbation series;
- `P3`: independent physical or biochemical substrate;
- `S1`: literature synthesis linking nonidentical implementations.

Model ablations are never described as experimental knockouts. Literature synthesis is never treated as a new experiment.

### 2.4 Biological tribunal

The tribunal comprises:

1. freeze the biological signature and jurisdiction;
2. verify baseline function;
3. substitute labels, components, parameters or substrate while preserving the proposed relation class;
4. ablate each critical relation;
5. rewire source, target or sign while preserving cardinality where possible;
6. test transport to another biological implementation or substrate;
7. enumerate proper subcarriers;
8. assign `POSITIVE`, `NEGATIVE`, `ABSTAIN` or `NO_UNIQUE_MINIMAL_CARRIER`.

---

## 3. Closed cyclic repression as an oscillatory unit

### 3.1 Candidate

The repressilator candidate is

\[
\mathcal U_{\mathrm{OSC}}=(V,E^-,\Theta_{\mathrm{osc}}),
\]

with three repressors connected in a closed inhibitory cycle and a kinetic jurisdiction supporting a stable limit cycle. The unit is not the set of molecular names \(\{\mathrm{LacI},\mathrm{TetR},cI\}\). It is the signed cyclic relation under an admissible nonlinear delay/degradation regime.

### 3.2 Frozen signature

The signature contains:

- self-sustained oscillation after transients;
- cyclic phase ordering;
- approximately one-third-period separation among successive repressors;
- recoverable oscillator identity under relabeling;
- transport of the functional relation class.

In the curated deterministic model, the mean protein period is approximately 125.35 min and the three phase fractions are approximately

\[
(0.333478,0.333261,0.333261).
\]

### 3.3 Substitution

A cyclic relabeling of the three species, with congruent permutation of the state, preserves the numerical trajectory to solver precision. Published redesigns alter reporter placement, degradation machinery, leakage and auxiliary binding sites while preserving oscillation. An electronic analog transports the cyclic inhibitory architecture outside the biochemical substrate.

### 3.4 Ablation and rewiring

Deleting any one critical repression in the frozen model destroys the limit cycle and yields a fixed point. Physical deactivation of a repressor edge in optogenetic or chemical implementations similarly changes the dynamical regime. Cardinality-preserving source duplication or sign reversal also destroys the strict signature under the frozen parameters. Across all eight sign assignments, only the all-repression cycle oscillates in the declared regime.

### 3.5 Minimality

One-node self-repression and two-node mutual repression, instantiated in the same kinetic family, converge to fixed points. The three relations are inclusion-minimal in this jurisdiction.

### 3.6 Adjudication

```text
UMI-OSC = PASS
MULTIFRACTAL QUALIFIER = NOT TESTED
```

The result does not state that every biological oscillator requires three repressors. It identifies the minimal carrier of this strict oscillator class under the declared family.

---

## 4. Internal-model closure in robust perfect adaptation

### 4.1 Candidate

The candidate is the relation class

\[
\mathcal U_{\mathrm{RPA}}
=
\text{output sensing}
\rightarrow
\text{persistent error integration}
\rightarrow
\text{corrective actuation}
\rightarrow
\text{output}.
\]

### 4.2 Exact control result

For

\[
\dot y=-ay+bz+d,
\qquad
\dot z=k(r-y),
\]

a stable equilibrium satisfies

\[
y^*=r,
\qquad
z^*=\frac{ar-d}{b}.
\]

By contrast, proportional feedback gives

\[
y^*-r=\frac{d-ar}{a+bK_p},
\]

and retains a disturbance-dependent error.

For antithetic feedback,

\[
\dot z_1=\mu-\eta z_1z_2,
\qquad
\dot z_2=\theta y-\eta z_1z_2,
\]

so

\[
\frac{d}{dt}(z_1-z_2)=\mu-\theta y
\]

and a stable equilibrium satisfies

\[
y^*=\frac{\mu}{\theta}.
\]

### 4.3 Substitution and transport

The relation class is realized by:

- receptor-methylation feedback in bacterial chemotaxis;
- classical integral controllers;
- antithetic biomolecular sequestration;
- engineered bacterial regulation;
- cell-free transcription–translation systems;
- mammalian synthetic proportional–integral circuits.

The material components differ, while persistent error memory and corrective closure remain.

### 4.4 Ablation, rewiring and minimality

Removal of sensing, integration or actuation destroys the strict signature. Sign reversal destabilizes or amplifies error. Integrating disturbance or a constant source rather than output error fails. In the enumerated three-relation family, only the complete sensor–integrator–actuator closure passes.

### 4.5 Adjudication

```text
UMI-RPA = PASS
MATERIAL CARRIER = CLASS-VALUED
```

This result is aligned with, and does not replace, the internal model principle and established RPA module theories.

---

## 5. Regenerative bounded closure in bistable genetic memory

### 5.1 Frozen signature

A biological memory unit must exhibit:

- two bounded stable states;
- controlled `SET` and `RESET`;
- persistence after input withdrawal;
- admissible transport across implementations.

### 5.2 Candidate

\[
\mathcal U_{\mathrm{MEM}}
=
\text{regenerative feedback}
+
\text{nonlinear saturation}
+
\text{write coupling}.
\]

The genetic toggle implements regenerative opposition through mutual repression and cooperative nonlinearities. The canonical double-well model and electronic latch provide formal and cross-substrate realizations.

### 5.3 Interventions

Without regeneration, deviations decay to one state. Without saturation, positive feedback is not bounded. Without write coupling, existing states may persist, but the system does not satisfy the frozen controllably writable signature. Only the full three-relation carrier passes the relation-subset audit.

### 5.4 Adjudication

```text
UMI-MEM = PASS
```

The claim concerns the strict writable-memory class, not every possible molecular memory mechanism.

---

## 6. Driven multistage discrimination in kinetic proofreading

### 6.1 Frozen signature

The signature is specificity beyond the equilibrium discrimination limit with nonzero throughput.

### 6.2 Candidate

\[
\mathcal U_{\mathrm{KPF}}
=
\text{energy-driven multistage progression}
+
\text{reject/reset pathway}.
\]

Equilibrium binding exploits a free-energy difference once. Kinetic proofreading uses nonequilibrium progression and repeated rejection to amplify discrimination. The relation class appears in translation, immune-receptor signaling and synthetic strand-displacement networks.

### 6.3 Matched decoy

Equilibrium recognition may show high specificity and the same input/output labels, but it cannot realize the strict beyond-equilibrium signature under the declared thermodynamic contract. The distinction is mechanistic rather than visual.

### 6.4 Ablation and transport

Removing the irreversible progression or reset relation collapses the proofreading advantage. Substitution of molecular species and reaction chemistry preserves the class across enzymatic, receptor and synthetic nucleic-acid implementations.

### 6.5 Adjudication

```text
UMI-KPF = PASS
EQUILIBRIUM RECOGNITION = NEGATIVE FOR THE STRICT SIGNATURE
```

---

## 7. Finite-wavenumber instability in synthetic pattern formation

### 7.1 Frozen signature

The system must:

- possess a homogeneous state stable without transport;
- become unstable for at least one finite spatial wavenumber when transport is included;
- generate a characteristic spatial scale without an externally imposed positional template.

### 7.2 Candidate

\[
\mathcal U_{\mathrm{TUR}}
=
\text{local reaction stability}
+
\text{mobility contrast}
+
\text{finite-}k\text{ instability}.
\]

The class is realized in chemical cells, synthetic bacterial populations and engineered multi-node gene circuits.

### 7.3 Matched decoy

A circuit that reads an externally supplied morphogen gradient can produce a stripe with similar morphology. It fails the strict signature because position and scale are instructed rather than generated by spontaneous reaction–transport instability.

### 7.4 Ablation and rewiring

Equalizing transport coefficients, removing the critical inhibitory or activatory relation, or changing the sign structure can remove the finite-wavenumber instability even when the same components remain.

### 7.5 Adjudication

```text
UMI-TUR = PASS
INSTRUCTED STRIPE = NEGATIVE FOR THE STRICT SIGNATURE
```

---

## 8. Minimal autocatalytic closure

### 8.1 Frozen signature

A reaction set must be:

- reflexively autocatalytic;
- food-generated;
- inclusion-minimal under the declared reaction universe.

### 8.2 Candidate

The candidate is a minimal RAF set rather than an individual catalyst. In a two-reaction example, neither reaction alone is both food-generated and internally catalyzed, while the pair closes the required production and catalysis relations.

### 8.3 Transport

Autocatalytic closure has been realized or analyzed in peptide self-replication, ribozyme systems, organic chemistry and inorganic cluster networks. The chemistry changes while collective catalytic closure persists.

### 8.4 Matched decoy

An open catalytic chain can produce amplification but relies on an external catalyst not regenerated by the set. It therefore fails closure.

### 8.5 Adjudication

```text
UMI-RAF = PASS
OPEN CATALYTIC CHAIN = NEGATIVE
```

RAF theory already supplies the domain formalism; the tribunal contributes cross-case comparability, transport and matched-decoy logic.

---

## 9. Abstention in quorum-sensing competence

Quorum-sensing competence circuits combine extracellular signal accumulation, receptor activation, feedback, density dependence, environmental history and intracellular switching. Under the evidence packet currently available, more than one carrier can explain the strict history-dependent collective switch, and critical interventions do not isolate a unique minimal relation class.

```text
QUORUM-SENSING COMPETENCE = ABSTAIN
```

The abstention is not a negative biological judgment. It records causal nonuniqueness or insufficient intervention resolution.

---

## 10. Relation to biological unit concepts

### 10.1 Network motifs

Motif analysis identifies recurrent topology. The biological UMI tribunal requires function-specific sufficiency, kinetic jurisdiction, negative interventions, transport and minimality. A motif is a candidate carrier, not an automatic unit.

### 10.2 Dynamical modules and design principles

Dynamical modules connect topology to function and can identify reusable computations. The tribunal adds one evidence grammar across different functions and explicitly separates positive preservation tests from destructive relation tests.

### 10.3 Control-theoretic modules

Internal-model and RPA module theories provide stronger necessary results for adaptation than the general tribunal. They are incorporated as high-grade domain evidence rather than rebranded.

### 10.4 Organisational closure

Closure-of-constraints approaches address mutually sustaining biological organisation. The present carriers are more local and task-relative. A repressilator or proofreading module need not be autonomous or self-producing to qualify under its jurisdiction.

### 10.5 Mechanistic explanation

The tribunal is compatible with interventionist mechanism accounts but adds an invariance requirement: the proposed unit must survive admissible substitutions and transports, not merely show causal necessity in one realization.

---

## 11. Discussion

Across the six positive classes, the same relation-first asymmetry recurs. Preserving the component inventory while breaking a critical relation destroys the function. Replacing components, species or substrate while preserving the relation class can preserve the function. Biological unity therefore resides neither in molecule names nor in a bare graph. It resides in a typed relation class constrained by kinetics, thermodynamics, spatial coupling and context.

This result also explains why phenotype-based classification is insufficient. A transient oscillator resembles sustained oscillation; proportional feedback resembles adaptation; equilibrium binding resembles proofreading; an instructed stripe resembles a Turing pattern; an open catalytic chain resembles collective autocatalysis. The strict semantic signature and negative interventions separate these cases.

The cases do not imply one universal biological topology. The carrier types are heterogeneous: signed feedback, persistent error memory, regenerative boundedness, nonequilibrium rejection, reaction–transport instability and catalytic closure. What is invariant is the adjudication logic.

The tribunal can support experimental design. For a new candidate, it specifies which evidence is still missing: component substitution, edge-specific ablation, sign-preserving or sign-reversing rewiring, cross-context transport, or proper-subcarrier enumeration. It can also prevent premature mechanism naming by returning abstention.

---

## 12. Claim boundary

This manuscript does not claim discovery of the repressilator, genetic toggle, integral feedback, chemotaxis adaptation, antithetic control, kinetic proofreading, Turing patterning or RAF theory. It does not claim that all biological functions possess one unique carrier, that biological units are substrate-free, or that the identified carriers are empirically multifractal.

The proposed contribution is:

1. a biologically explicit UMI definition;
2. one frozen intervention tribunal across six mechanism classes;
3. evidence separation between exact, model and physical interventions;
4. mechanism–phenotype decoy tests;
5. cross-substrate and cross-implementation transport;
6. principled abstention for unresolved hybrid mechanisms.

---

## 13. Data, code and release

The release will include:

- curated model identifiers and source manifests;
- intervention-result tables;
- relation-subset audits;
- exact symbolic checks;
- literature evidence matrix with evidence classes;
- claim ledger and provenance manifest;
- software and data Zenodo records;
- manuscript source and `CITATION.cff`.

The biological evidence table will explicitly separate published experimental observations from our model-based counterfactuals.

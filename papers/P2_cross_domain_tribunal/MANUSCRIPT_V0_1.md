# Minimal Invariant Relational Units Across System Functions
## A cross-domain intervention tribunal for identifying units whose identity resides in relations

### Abstract

A general theory of systems requires an operational criterion for identifying units whose identity is not reducible to a component inventory. Structural motifs, minimal realizations, dynamical modules, internal models, bisimulation classes and organisational closure each capture important parts of this problem, but they do not supply one common adjudication protocol across physical, biological, computational and informational systems. We introduce an intervention tribunal for identifying **minimal invariant relational units** (UMIs). Under a declared jurisdiction, a candidate carrier must preserve a frozen semantic signature under admissible component or substrate substitution and cross-context transport, while losing that signature under critical relational ablation or cardinality-preserving rewiring; no proper subcarrier may retain the full signature. We apply the frozen tribunal to sustained oscillation, robust perfect adaptation, single-error correction, writable bistable memory, distributed-consensus safety, kinetic proofreading, finite-wavenumber Turing instability, mutual synchronization, topological edge transport and reflexively autocatalytic food-generated closure. The resulting carriers differ in material substrate and mathematical form, but share relational minimality and functional invariance. A homeostatic negative-feedback carrier is identified as a parent class rather than an independent unit relative to robust perfect adaptation, showing that UMI classes can form a refinement order. In a designed blinded benchmark, strict semantic signatures separated five carriers from five close decoys, whereas weakened signatures admitted false positives. A second evidence-blind naturalistic benchmark separated five established mechanism classes from matched phenotypic decoys and abstained on two mixed-mechanism hybrids. The contribution is not the discovery of the underlying mechanisms, but a domain-general procedure for determining when a relational configuration warrants treatment as an operational unit.

**Keywords:** general systems theory; relational mechanism; intervention; minimality; invariance; network motifs; dynamical systems; causal mechanism; substrate independence; abstention

---

## 1. Introduction

Systems science repeatedly encounters objects that behave as units although none of their components, considered separately, carries the relevant function. A negative-feedback loop regulates; a closed inhibitory cycle oscillates; a parity-check family corrects; a quorum system protects agreement; an autocatalytic set sustains collective production. In each case, the operative identity is relational. Yet the disciplines that study these examples use different unit concepts and different evidential standards.

Network-motif analysis identifies statistically overrepresented subgraphs and has revealed recurrent architectures across biological, ecological, neural and technological networks. This is a major structural result, but motif occurrence alone does not establish a unique dynamical function. The same graph can support different or opposite behaviors under different kinetic regimes, and distinct graph implementations can realize the same function. Dynamical modules and design principles address this limitation by relating architecture to behavior, while realization theory and bisimulation define equivalence and minimality relative to input–output behavior. Control theory identifies internal models and topological requirements for robust regulation. Organisational accounts characterize biological systems through closure among mutually sustaining constraints. These frameworks are complementary, but their admissible transformations, semantic targets and intervention criteria are usually domain-specific.

The present work asks a narrower and operational question:

> When should a relational configuration be treated as one system-level unit rather than as an arbitrary collection of components?

We answer by replacing intuitive unity with a falsifiable tribunal. A candidate unit is evaluated relative to a declared **jurisdiction**: a semantic signature, admissible substitutions, intervention class, transport class, tolerance and cost contract. The candidate must satisfy four requirements: closure, sufficiency, inclusion-minimality and invariance. The evidence is asymmetric. If components or substrate are replaced while the relation class is preserved, the signature should survive. If the critical relation is removed or rewired while the component count is held fixed, the signature should fail. The unit is therefore located neither in the parts nor in a bare topology, but in the smallest relational mechanism class that survives the admissible changes.

We call such a carrier a **minimal invariant relational unit** (UMI). The term is operational rather than ontological. It denotes an equivalence class under a declared tribunal, not a new material atom. The same physical system may contain different UMIs under different semantic signatures, and a candidate may receive `ABSTAIN` when evidence is incomplete or several minimal carriers remain plausible.

The paper contributes four results. First, it formalizes the tribunal and its decision rule. Second, it applies the same rule to heterogeneous mechanisms whose equations and substrates are not mutually reducible. Third, it distinguishes independent UMI classes from nested refinements. Fourth, it tests selectivity against designed and naturalistic decoys, including sensitivity to semantic under-specification.

---

## 2. Operational framework

### 2.1 Jurisdiction

A jurisdiction is a tuple

\[
\mathcal J=(\Sigma,\mathcal T,\mathcal I,\mathcal X,\varepsilon,\mathcal C),
\]

where:

- \(\Sigma\) is the frozen semantic signature to be preserved;
- \(\mathcal T\) is the set of admissible substitutions and transports;
- \(\mathcal I\) is the intervention family, including ablations and rewires;
- \(\mathcal X\) specifies the relevant contexts, inputs and continuation tasks;
- \(\varepsilon\) specifies exact or approximate equivalence tolerances;
- \(\mathcal C\) records declared resource and cost constraints.

The jurisdiction prevents the word “same” from drifting between topology, waveform, task performance, qualitative function and exact trajectory. For example, an electronic repressilator analog may preserve cyclic inhibition and sustained oscillation without preserving every biochemical timescale. This is a valid functional transport but not a quantitative conjugacy.

### 2.2 Relational carrier

A candidate carrier is represented as

\[
C=(V,R,\Theta),
\]

where \(V\) is a component set, \(R\) is a typed and possibly signed relation set, and \(\Theta\) is the admissible dynamical, algebraic or physical regime required by the signature. Including \(\Theta\) is essential. A graph alone seldom determines behavior.

### 2.3 UMI definition

A carrier \(C\) is a UMI in \(\mathcal J\) when

\[
\mathrm{UMI}_{\mathcal J}(C)
\iff
\operatorname{Closed}(C)
\land
\operatorname{Sufficient}_{\mathcal J}(C)
\land
\operatorname{Minimal}_{\subseteq,\mathcal J}(C)
\land
\operatorname{Invariant}_{\mathcal J}(C).
\]

**Closure** means that the relations required to realize the declared signature are contained in the candidate rather than supplied by an uncounted external mechanism.

**Sufficiency** means that the carrier realizes the full frozen signature within tolerance.

**Inclusion-minimality** means that no proper admissible subcarrier realizes the full signature. This is not minimum cardinality: two inclusion-minimal carriers may contain different numbers or types of components.

**Invariance** means that the signature is preserved under the admissible substitutions and transports declared in \(\mathcal T\).

When several non-equivalent minimal carriers survive, the result is `NO_UNIQUE_MINIMAL_CARRIER` or a class-valued result. When necessary evidence is unavailable, the result is `ABSTAIN`.

---

## 3. Frozen intervention tribunal

The tribunal is evaluated in the following order.

### 3.1 Semantic-signature freeze

The function, horizon, tolerance and continuation tasks are specified before the candidate carrier is adjudicated. “Produces several peaks” is not equivalent to “supports a self-sustained limit cycle.” “Detects an error” is not equivalent to “corrects every single-bit error.” “Forms a stripe” is not equivalent to “undergoes a finite-wavenumber instability from a homogeneous state.”

### 3.2 Baseline sufficiency

The unperturbed candidate must realize the strict signature. A system that fails the baseline is a decoy or an instance of a weaker function, regardless of superficial resemblance.

### 3.3 Substitution

Components, labels, parameters, implementation details or physical substrate are replaced while the candidate relation class is preserved. The signature must remain within the jurisdictional tolerance.

### 3.4 Relational rewiring

The number of components and, where possible, the relation count are preserved while source, target, sign, phase, orientation or incidence is changed. This distinguishes relational identity from cardinality and component inventory.

### 3.5 Critical ablation

Each relation claimed as necessary is removed or disabled. A critical ablation must destroy at least one indispensable element of the signature.

### 3.6 Transport

The carrier is sought in a distinct implementation, context or substrate. Transport is typed:

- `T1`: formal relation or topology preserved;
- `T2`: qualitative functional class preserved;
- `T3`: quantitative behavioral equivalence preserved.

### 3.7 Minimality enumeration

All admissible proper subcarriers are tested exactly when the candidate is finite and small. For larger systems, a declared search or proof strategy is required.

### 3.8 Decision

A strict positive requires baseline sufficiency, substitution and transport, critical ablation, rewiring sensitivity and minimality. An observed hard failure yields `NEGATIVE`. Missing evidence without a hard failure yields `ABSTAIN`.

---

## 4. Cross-domain portfolio

### 4.1 Sustained oscillation

The repressilator carrier is a closed signed three-cycle under a kinetic regime supporting a limit-cycle attractor. Cyclic label substitution preserves the trajectory, while deletion or sign reversal of any critical edge destroys sustained oscillation in the frozen regime. One- and two-node reductions converge to fixed points. Biological variants and an electronic analog preserve the functional class.

### 4.2 Robust perfect adaptation

The carrier is a constant-signal internal-model closure: regulated output to error sensing, error to persistent integration, and memory to corrective actuation in a stable loop. Classical integral feedback, nonlinear chemotaxis-like dynamics and antithetic molecular feedback realize the same class. Proportional control, sign reversal, loss of sensing, loss of integration or loss of actuation fails the strict signature.

### 4.3 Single-error correction

For the Hamming \((7,4)\) case, three independent syndrome relations assign seven distinct nonzero columns to seven error positions. Changes of syndrome basis and bit permutation preserve correction. Deleting one relation leaves too few nonzero syndromes; duplicating a syndrome column destroys unique identification. The class transports from communication coding to error-correcting memory and quantum-code syndrome structure.

### 4.4 Writable bistable memory

The carrier combines regenerative feedback, nonlinear saturation and a write coupling capable of crossing the separatrix. Canonical double-well dynamics, a genetic toggle and an electronic latch realize the class. Without regeneration the system has no persistent alternative states; without saturation it is unbounded; without write coupling it is not a controllably writable memory under the frozen signature.

### 4.5 Consensus safety

The carrier for single-decree agreement safety combines quorum intersection with persistent single-vote memory. Node relabeling and majority systems of different sizes preserve the signature. Disjoint quorums or double voting permit conflicting decisions. Liveness and leader election are outside the jurisdiction.

### 4.6 Kinetic proofreading

The carrier is a driven multistage discrimination relation with a reject/reset path. It preserves specificity beyond the equilibrium discrimination limit while retaining nonzero throughput. Equilibrium recognition is a matched decoy: it discriminates, but it does not realize the strict beyond-equilibrium signature.

### 4.7 Turing finite-wavenumber instability

The carrier combines local reaction stability, differential transport and instability at nonzero wavenumber. Chemical and synthetic biological implementations preserve the class. An externally imposed morphogen stripe is a matched phenotype decoy because it does not generate the pattern through spontaneous finite-wavenumber instability.

### 4.8 Mutual synchronization

The carrier is feedback through phase difference or another mutual coupling variable sufficient to generate phase and frequency locking. Common forcing can align phases without mutual interaction and therefore fails the strict causal signature.

### 4.9 Topological edge transport

The carrier combines a bulk invariant, protecting gap or symmetry and a boundary. Photonic and wave implementations transport the class. A trivial defect-localized mode can mimic spatial localization but lacks the declared disorder robustness and bulk–boundary relation.

### 4.10 Reflexively autocatalytic food-generated closure

The carrier is a minimal RAF reaction set: every reaction is catalyzed from within the set and all reactants can be generated from the food set. Open catalytic chains can amplify production without satisfying collective closure.

### 4.11 Nested class: homeostasis and robust perfect adaptation

Negative-feedback homeostasis passes the tribunal for disturbance attenuation, but robust perfect adaptation adds an internal model that forces zero steady-state error for the declared signal class. The relation is therefore a refinement:

\[
\mathcal U_{\mathrm{HOM}}
\succ
\mathcal U_{\mathrm{RPA}},
\]

where the ordering denotes strengthening of the semantic signature and carrier constraints. UMI classes need not form a flat catalogue.

---

## 5. Adversarial selectivity

### 5.1 Designed benchmark

Five established carriers were paired with close functional decoys:

- sustained oscillator versus damped oscillator;
- robust perfect adaptation versus high-gain proportional regulation;
- correction versus detection-only parity;
- persistent writable memory versus finite-horizon leaky retention;
- multiround agreement safety versus volatile single-round majority.

With strict signatures, the frozen rule yielded five true positives and five true negatives. With a moderate signature, one decoy passed. With a weak signature, all five decoys passed. The false-discovery rate therefore increased from 0 to \(1/6\) to \(1/2\) as semantics were weakened.

This result identifies a central property of the method: selectivity does not arise from intervention counts alone. It arises from the conjunction of a strict semantic signature and a relational intervention tribunal.

### 5.2 Naturalistic matched-pair benchmark

Five literature-derived mechanism classes were paired with naturalistic decoys:

- kinetic proofreading versus equilibrium binding;
- Turing instability versus instructed stripe formation;
- mutual synchronization versus common forcing;
- topological edge transport versus trivial defect localization;
- minimal RAF closure versus an open catalytic chain.

All five mechanism classes and all five decoys were separated under the frozen rule. Two mixed-mechanism cases—quorum-sensing competence and coupling plus common noise—were assigned `ABSTAIN` because evidence did not identify one unique minimal carrier.

### 5.3 Missing evidence

Under conservative adjudication, incomplete evidence without observed failure produces abstention rather than a positive classification. This protects against inventing unity from absent interventions.

---

## 6. Relation to established frameworks

### 6.1 Network motifs

Network motifs identify recurrent structural patterns relative to a null model. UMI adjudication does not require statistical overrepresentation and does not infer function from topology alone. Motifs may be candidates for UMIs, but only after kinetic jurisdiction, semantic sufficiency, intervention sensitivity, transport and minimality are established.

### 6.2 Dynamical and functional modules

Dynamical modules identify reusable behaviors or causal pathways. The UMI tribunal adds a fixed cross-domain evidence grammar and an explicit negative test: the carrier must fail under critical rewiring or ablation while surviving admissible substitution.

### 6.3 Minimal realization and bisimulation

Realization theory and bisimulation formalize behavioral equivalence and minimal state descriptions. UMI minimality is relative to a semantic signature and intervention family rather than a complete external behavior. UMI transport may be weaker than bisimulation and stronger than phenotype similarity. The two concepts should therefore be related by explicit implication results rather than treated as synonyms.

### 6.4 Internal-model and design-principle theory

Control theory derives necessary carriers for specific functions, particularly regulation and adaptation. The tribunal does not replace these theorems; it uses them as strong domain-specific evidence and asks whether the same adjudication logic extends to unrelated functions.

### 6.5 Organisational closure

Closure-of-constraints theories characterize mutually sustaining biological organisation. UMI closure is narrower and task-relative. A UMI need not be self-producing, autonomous or alive. Organisational closure is therefore a possible biological specialization, not a universal synonym.

### 6.6 Causal-mechanistic explanation

Interventionist accounts identify causal relevance by changes under manipulations. The UMI tribunal combines this with substitution and transport, thereby testing not only necessity but invariance of a mechanism class across implementations.

---

## 7. Discussion

The cross-domain results support a relation-first conception of system units. The strongest recurring asymmetry is:

\[
\text{same components + altered critical relations}
\Rightarrow
\text{different system-level function},
\]

while

\[
\text{different components or substrate + preserved relation class}
\Rightarrow
\text{preserved functional class}.
\]

This asymmetry does not imply unrestricted substrate independence. Every carrier includes a jurisdiction \(\Theta\) specifying the physical or dynamical conditions under which the relation is realizable. The claim is therefore neither that topology determines function nor that matter is irrelevant. It is that operational unity is adjudicated at the level of a typed relation class under explicit physical constraints.

The framework also clarifies why semantic specification is constitutive. A damped oscillator is a valid unit for transient ringing but not for sustained oscillation. A parity check is a valid detector but not a single-error corrector. A trivial defect state is a valid localized mode but not a topologically protected edge carrier. “Negative” means failure relative to the frozen task, not absence of organization.

The discovery of nested classes suggests a refinement structure. A carrier can be sufficient for a weaker signature and become a parent class of a more constrained carrier. Future work should formalize meet, join and partial-order properties among UMI classes and determine when different minimal carriers are equivalent, incomparable or context-dependent.

The current portfolio spans graph-theoretic, dynamical, informational, control, topological and chemical carriers. This rules out defining UMI as a graph motif alone. The general object is a minimal relational mechanism class, which may include equations, signs, memory, spatial transport, global invariants or closure conditions.

---

## 8. Claim boundary

This work does **not** claim discovery of the repressilator, integral control, Hamming codes, bistable switches, consensus protocols, kinetic proofreading, Turing instability, synchronization, topological protection or RAF theory. It does not claim that every system possesses a unique UMI, that UMI is an ontological primitive, or that the present carriers are empirically multifractal.

The proposed contribution is the conjunction of:

1. a jurisdiction-dependent formal unit criterion;
2. a frozen intervention tribunal;
3. cross-domain application without changing the decision logic after inspecting each case;
4. explicit decoy and ambiguity handling;
5. refinement classification among carriers;
6. reproducible ledgers linking claims, interventions and transport evidence.

---

## 9. Reproducibility and data availability

All frozen case definitions, intervention matrices, exact verifiers, blind commitments, predictions and reveal files are maintained in the Magimatics repository. The release associated with the preprint will include:

- a versioned software archive;
- case and intervention tables;
- blind benchmark packets;
- machine-readable claim ledger;
- provenance manifest;
- exact verification output;
- `CITATION.cff` and Zenodo metadata.

The manuscript will cite separate Zenodo DOIs for software and benchmark data when the final release is frozen.

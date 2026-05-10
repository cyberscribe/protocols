# Prufrock Protocol: FPT SIG Positioning Analysis

**Prepared**: May 2026
**Purpose**: Map the Prufrock Protocol's formal elements onto the Formal Protocol Theory SIG's conceptual frameworks. Identify alignments, divergences, novel contributions, and productive questions for presentation.

---

## 1. Concept Mapping

This section takes each major element of the Prufrock formalisation and identifies which FPT SIG frameworks it maps to, where it extends them, and where the mapping is imprecise.

### 1.1 The Contribution Tuple

**Prufrock**: $\ell = (x, \Pi, a, t_p, t_r, g, \sigma)$ — text, parent hashes, author key, prompt time, response time, location, signature.

**SIG mapping**: The contribution tuple is an *actor message* in the Hewitt sense — a signed, timestamped communication from an opaque agent to a shared environment. The SIG's Actor Models session (Dec 12) established that actors receive messages, update state, and emit messages; the contribution tuple is a maximally constrained version of this: no state update is visible (the participant's internal experience is not recorded), and the message carries its own authentication.

The tuple also maps to the SIG's **process calculi** substrate. In session-types terms (the multiparty session types literature from Aug 8), each contribution is a message in a structured communication session where the type signature enforces lineage, punctuality, and self-exclusion. The form constraint $\mathcal{F}$ functions as a session-type refinement — narrowing admissible messages at each position.

The geolocation field $g$ and the dual timestamps $(t_p, t_r)$ have no direct analogue in the SIG's existing formalisms. These are novel: they bind the message not just to its sender and logical position in a conversation, but to a physical moment. The SIG has discussed **observability** extensively (June 27 session), and the contribution tuple can be read as an *observability instrument* — each field records a different observable dimension of the act of composition.

**Fit quality**: Strong for actor model and session types mapping. The spatiotemporal binding is genuinely new territory for the SIG.

### 1.2 The Ledger

**Prufrock**: $\mathcal{L}^*$ — an append-only authenticated log. The parent relation $\prec$ forms either a directed forest ($k=1$) or a DAG ($k>1$).

**SIG mapping**: The ledger maps directly to two SIG concerns:

First, **stigmergy** (May 1 session). The ledger is a *sematectonic* stigmergic surface — the Parunak taxonomy's term for coordination through the state of a constructed environment rather than through deposited markers. Each contribution modifies the shared structure, and that structure cues subsequent contributions. The SIG discussed how stigmergy externalises state from agents into the environment; the Prufrock ledger does exactly this. The poem-in-progress *is* the coordination medium.

Second, **blockchain/hardness** (Stark's *Atoms, Institutions, Blockchains* framework from the Protocol Reader). The ledger's append-only, hash-chained structure is a *cast* — a future-state claim that prior contributions existed and were valid — whose hardness derives from cryptographic rather than institutional or physical sources. The SIG has discussed ledger structures in the context of Ethereum ossification; Prufrock's ledger is interesting because it uses cryptographic hardness to authenticate *aesthetic* rather than *financial* commitments.

**Fit quality**: Very strong. The SIG already thinks about ledgers, and the stigmergy mapping is tight. The novelty is in what the ledger records — situated human expression rather than transactions.

### 1.3 The Schedule (Interruption + Prompt Selection)

**Prufrock**: Interruption timing ($\mathrm{Mode}_\tau$: uniform, Poisson, scheduled), prompt selection ($\mathrm{Sel}$: chosen rotation, random peer, weighted peer, round robin), availability windows $W_p$, response window $R$, minimum inter-arrival $\Delta$.

**SIG mapping**: The schedule maps onto several SIG frameworks:

**Maneuver Automata** (Oct 17 session). The SIG studied Frazzoli's formalism of trim states (steady-state behaviours) connected by maneuver transitions. In Prufrock, a participant alternates between a "trim state" of ordinary life and a "maneuver" triggered by the interruption — the transition from daily activity to poetic composition and back. The interruption is a forced transition between automaton states, and the timing modes (uniform, Poisson, scheduled) parameterise the transition trigger in the same way that environmental perturbations trigger maneuver switches in robotic systems.

**Allen's Interval Algebra** (from the Notation session, July 12). The schedule defines temporal interval relationships: the response window $R$ means the contribution *during* the interval $[t_p, t_p + R]$; the availability window means interruptions *during* $W_p$; the inter-arrival constraint means successive interruptions are *separated by* at least $\Delta$. These are Allen relations applied to protocol timing.

**Autocurricula** (April 3 session). The prompt selection mechanism creates a *non-stationary environment* for each participant — the defining feature of autocurricula. Each contribution changes what subsequent participants will see, creating a self-generating sequence of challenges. Unlike the hide-and-seek example the SIG studied, Prufrock's autocurricula is aesthetic rather than strategic, but the structural mechanism is the same: agents' actions alter other agents' observation space.

**Fit quality**: The maneuver-automata and autocurricula mappings are productive analogies rather than strict isomorphisms. The Allen-interval mapping is tight. The schedule is where Prufrock's hybrid nature (protocol-imposed structure + human phenomenological response) is most visible.

### 1.4 The Lineage DAG

**Prufrock**: The parent relation $\prec$ traces cryptographic lineage — each contribution commits to specific ancestors via hash reference. When $k > 1$, the structure is a DAG. Chains (maximal paths) are the individually experienced sequences; the full DAG is the collective structure.

**SIG mapping**: The lineage DAG is a **directed graph** in the sense the SIG uses for protocol state spaces. In process calculi terms, it represents the *trace* of a multiparty session — the sequence of messages exchanged, with branching where multiple participants respond to the same prompt.

More precisely, it maps to the SIG's interest in **protocol composition and stacking** (from the Evolving Evolvability page and the PFW Integration Jigsaw). Each chain through the DAG is a composed sequence of atomic interactions; the DAG as a whole represents the space of all possible compositions. The form constraint $\mathcal{F}$ acts as a *grammar rule* on valid compositions — echoing the SIG's discussion of "behaviour grammars" in the big framing talk.

The DAG also connects to **protocol drift** (Sept 13 session, Protocols and Drift page). Each chain through the DAG can be seen as a particular drift trajectory from the seed. Comparing chains reveals how the same initial conditions diverge through different participants' situated responses — a concrete instance of the SIG's question about measuring drift.

**Fit quality**: Strong. The SIG's vocabulary for graphs, traces, and composition applies directly.

### 1.5 Form Constraints

**Prufrock**: $\mathcal{F} = (f_{\text{name}}, S, \rho, \mathcal{R}, \mathcal{W}, \mu, v)$ — named form, stanza structure, rhyme scheme, refrain rules, end-word rotation, meter, volta position.

**SIG mapping**: Form constraints map onto the SIG's concept of **protocol thickness** from the Design Principles session (Daston's thick/thin distinction). A free-form experiment ($\mathcal{F} = \emptyset$) is a *thin* protocol — minimal discretion, minimal judgement required. A sestina or ghazal trial is *thick* — the end-word rotation or refrain rules demand context-sensitive judgement, interpretation, and craft. The formalisation explicitly acknowledges this: form constraints are "advisory in simulation, validated in live experiments" with "human judgement applies to poetic form." This is a designed position on the thick/thin spectrum.

Form constraints also connect to **generative space** (from the Evolving Evolvability page). A protocol's generative space is defined by primitives, composition rules, constraints, and evaluation. In Prufrock:

- Primitives: contributions (response units)
- Composition rules: lineage DAG, schedule, prompt selection
- Constraints: form schema $\mathcal{F}$
- Evaluation: the advisory/validated distinction, plus the eventual human readership

The SIG's key question about generativity — "what determines the generativity of a protocol?" — becomes concretely testable in Prufrock by comparing the output space across experiments with different form constraints.

Form constraints also relate to the SIG's **nondimensionalisation** discussion (from the Nondimensionalization page). The SIG asked whether the ten dimensions of sufficiency could be cast as dimensionless quantities. The form constraint is a candidate for nondimensionalisation: the ratio of constrained positions to total positions in a poem gives a dimensionless measure of "formal tightness" that could be compared across experiments and even across non-poetic protocols.

**Fit quality**: The thick/thin and generative-space mappings are clean. The nondimensionalisation connection is speculative but potentially productive.

### 1.6 The Seed

**Prufrock**: Genesis contributions drawn from existing works, encoded with provenance attestation. The seed is authored by no participant — it is external to the cohort.

**SIG mapping**: The seed maps to the concept of **initial conditions** in dynamical-systems language, which the SIG uses frequently. More specifically, it is an *exogenous injection* in the autocurricula framework — the equivalent of a researcher introducing a new element into a multi-agent environment.

The seed also connects to the SIG's discussion of **protocol stewardship** (from the Atomic Protocol Questions). The seed is a stewardship act: it selects what lineage the protocol inherits, what cultural material enters the system. The provenance requirements (minimum age, rights status, language) are themselves a protocol for protocol initialisation — a meta-protocol concern the SIG has discussed under "stacking."

**Fit quality**: Moderate. The mappings are real but not deeply illuminating on their own.

### 1.7 Forfeit Handling

**Prufrock**: Forfeit is permanently recorded; absence is data. The schedule adapts (falling back to the most recent non-forfeited contribution) but the record does not pretend the forfeit didn't happen.

**SIG mapping**: This maps directly to the SIG's interest in **protocol failure modes** and **observability of non-events**. The Protocol Reader essay *Safe New World* (Stinson-Schroff) identified "safety as dynamic non-event" — the hardest thing to observe is when nothing happens. Prufrock's forfeit handling makes non-participation observable and permanent, which is a design decision the SIG would recognise as significant.

It also connects to the **ETTO principle** (Hollnagel) flagged in the Group 4 insights — the efficiency-thoroughness trade-off. Prufrock chooses thoroughness over efficiency: it would be simpler to silently skip forfeits, but the protocol insists on recording them. This is a concrete instance of the SIG's "Biased ETTO Principle" (Design Principle #2: Thoroughness > Efficiency).

**Fit quality**: Strong. The SIG has the exact vocabulary for this.

---

## 2. Shared Vocabulary: Alignment and Divergence

### Terms Prufrock uses that the SIG already defines

| Prufrock term | SIG definition | Alignment |
|---|---|---|
| Append-only ledger | Authenticated data structures, blockchain context | Aligned. Prufrock uses the structure for aesthetic rather than financial purposes, but the formal properties are identical. |
| Validity rules | Session types, contract enforcement | Aligned. Prufrock's five validity rules map to session-type preconditions. |
| Experiment configuration | Protocol parameterisation (Basket of Protocols) | Aligned. Prufrock's $\mathcal{E}$ is a point in the SIG's "protocol parameter space." |
| Response window | Temporal constraints (Allen intervals) | Aligned. |
| Self-exclusion invariant | Symmetry / impossibility constraints | Aligned. This is a structural impossibility result: you cannot be your own interlocutor. |
| Cohort | Agent population | Aligned, though "cohort" carries a longitudinal-study connotation absent from the SIG's usage. |

### Terms where Prufrock diverges from SIG usage

| Prufrock term | SIG expectation | Divergence |
|---|---|---|
| "Poem" | Not in SIG vocabulary | The SIG has no framework for the output of a protocol being an *aesthetic object* with its own evaluative criteria independent of protocol compliance. |
| "Interruption" | Message delivery | Prufrock's "interruption" is phenomenologically loaded — it implies the participant is doing something else and is *pulled away*. The SIG's message-delivery model is neutral about the recipient's prior state. |
| "Advisory" form constraints | Hard/soft constraint binary | The SIG tends to treat constraints as enforced or not. Prufrock's "advisory" — scored in simulation, flagged-but-not-rejected in live experiments — is a third category that sits between enforcement and suggestion. |
| "Negative space" | Not in SIG vocabulary | See Section 3.2 below. |

### Terms Prufrock introduces that could contribute to SIG vocabulary

| Term | Definition in Prufrock | SIG gap it could fill |
|---|---|---|
| Compression-fidelity trade (P7) | The protocol preserves certain observables (identity, time, location, lineage) while necessarily sacrificing others (mental state, context, alternatives considered). | The SIG discusses trade-offs extensively (ETTO, tension curves, nondimensionalisation) but has no term for the specific trade-off between what a protocol records and what it must discard. |
| Negative space | The unrecorded space — what the protocol deliberately does not capture — which is the space in which interpretation, meaning, and human judgement operate. | The SIG discusses observability but frames unobservability as a *limitation*. Prufrock frames it as a *feature* — a designed property. |
| Situated authentication | Authentication that binds not just to identity but to a specific moment and place (the dual timestamps + geolocation). | The SIG discusses authentication in blockchain/cryptographic contexts but without the phenomenological dimension. |

---

## 3. Novel Contributions to the FPT Conversation

### 3.1 Compression-Fidelity Trade as a Protocol Property

The SIG has discussed trade-offs between efficiency and thoroughness (ETTO), between legibility and defensibility (ten dimensions of sufficiency), and between ossification and evolvability. Prufrock's Property P7 names a different trade-off that may be more fundamental: every protocol compresses some aspect of the interaction it mediates, and the question is *what* it compresses and *what* it preserves.

This is not the same as observability. Observability asks "can you deduce internal state from outputs?" The compression-fidelity trade asks "which internal states did the protocol *design* itself to capture, and which did it *design* itself to ignore?" Every protocol answers this question, usually implicitly. Prufrock answers it explicitly, which makes it useful as a teaching case.

The SIG could use this as a general analytical tool: for any protocol in the Basket of Protocols, ask "what is the compression-fidelity trade?" For handwashing: the protocol compresses pathogen dynamics into a temporal rule (wash for N seconds) and discards the specific microbiome of the hands. For Ethereum: the protocol compresses economic intent into transactions and discards the social context of the exchange.

### 3.2 Negative Space as Design Category

The SIG has studied what protocols *do* — their rules, states, transitions, observables. Prufrock introduces a formal concept for what protocols *don't do* and argues this is equally important to their design.

In poetic terms, negative space is what makes a line meaningful — the fact that a sonnet has fourteen lines means everything not said is as much a part of the poem as everything said. The compression creates the space for the reader's interpretation. Prufrock argues this is a general protocol property: the unrecorded dimensions of a protocol interaction are the space in which participants exercise judgement, agency, and meaning-making.

This connects to the SIG's thick/thin distinction but goes further. A thick rule preserves space for judgement *within* the protocol; negative space identifies the judgement that happens *outside* the protocol's recording boundary. The forfeit-handling design is instructive: even Prufrock's negative space has edges — absence is recorded, but the *reasons* for absence are not.

This could be productive for the SIG's analysis of protocol drift: drift may be partly a function of what the protocol leaves in negative space. If a protocol's negative space is too large, participants fill it with uncoordinated practices that eventually diverge. If it's too small, the protocol over-constrains and becomes brittle.

### 3.3 Poetic Form as Protocol Constraint

The SIG has studied constraints from the perspective of enforcement (hard/soft, thick/thin, blockchain/institutional). Prufrock introduces a class of constraint with no enforcement mechanism in the traditional sense but enormous structuring power: the aesthetic constraint.

A sonnet's rhyme scheme or a ghazal's radif are not enforced by punishment, consensus, or cryptography. They are enforced by the participants' commitment to the form — and by the fact that violations are *visible* to subsequent participants. This is a mode of enforcement the SIG has not named: call it *aesthetic enforcement* or *visible-commitment enforcement*. It is closer to the stigmergic mechanism than to the actor-model mechanism: the constraint is mediated by the shared environment (the poem-in-progress) rather than by direct communication.

The SIG's "Floor > Ceiling" principle (Design Principle #9) is relevant here. Form constraints raise the floor of what constitutes a valid contribution without exhorting participants to achieve poetic excellence. The form provides structure that even a non-poet can work within; the ceiling is unlimited.

### 3.4 Human Authentication of Situated Experience

Most protocols the SIG studies authenticate *actions* (transactions, votes, messages). Prufrock authenticates *situated moments of human experience* — the fact that a specific person, in a specific place, at a specific time, was confronted with a poetic prompt and responded. The response window $R$ bounds how long the person had; the geolocation $g$ records where they were; the dual timestamps $(t_p, t_r)$ measure how long they took.

This is authentication at a level the SIG has not discussed. It is not authenticating that a transaction occurred; it is authenticating that a moment of attention and reflection occurred. In the context of generative AI and the collapse of trust in digital expression (which the Prufrock pitch frames as more urgent than the collapse of banking systems), this is a significant protocol-design move.

---

## 4. Open Questions for Protocol Theorists

These are framed as questions about protocol theory in general, using Prufrock as a concrete instance.

### Q1: Can a protocol's compression-fidelity trade be nondimensionalised?

The SIG has discussed nondimensionalisation as a technique for finding universal protocol properties independent of scale. If every protocol has a compression-fidelity trade, is there a dimensionless ratio (analogous to the Reynolds number) that characterises *how much* a protocol compresses? Prufrock's ratio of recorded fields (7 per contribution) to plausible fields of human experience at the moment of composition might be a starting point. What would the equivalent be for handwashing, or for Ethereum?

### Q2: What is the relationship between a protocol's negative space and its susceptibility to drift?

The SIG's Protocols and Drift strawman defines drift as "efficiency minus context." But context is partly what lives in a protocol's negative space — the dimensions of meaning that are not explicitly recorded. If a protocol records too little (large negative space), does drift become invisible because the protocol has no observables to drift *against*? If it records too much (small negative space), does it become brittle and break rather than drift? Is there an optimal ratio?

### Q3: Under what conditions does aesthetic enforcement produce coordination without consensus?

Prufrock's form constraints coordinate participant behaviour without any consensus mechanism — no voting, no majority rule, no mechanism design. The form itself is the coordination device. The SIG has studied correlated equilibria (Autocurricula session) as coordination mechanisms. Is aesthetic form a correlated equilibrium? If so, what is the "signal" — the form itself, the tradition behind it, or the participants' shared commitment to it?

### Q4: How does stigmergic coordination change when the environment is an aesthetic object?

The SIG's stigmergy session identified two types: quantitative (pheromone gradients) and qualitative (structural configurations cue different actions). A poem-in-progress is a qualitative stigmergic surface — but with a crucial difference: the "cues" are aesthetic rather than functional. A termite responds to the geometry of a half-built pillar; a poet responds to the meaning, rhythm, and emotional valence of a half-built poem. Does this difference affect the coordination dynamics, or is the structural mechanism the same regardless of the medium?

### Q5: Can a protocol's liveness property (P6) be extended to measure experiential coverage?

Prufrock's liveness guarantee says that contribution times converge to a uniform sample over availability windows. This is a statistical property about *when* contributions occur. A stronger property would characterise *what kind of experience* gets sampled — the diversity of locations, times of day, emotional states. Can the liveness concept be generalised from temporal coverage to experiential coverage? What would that look like formally?

---

## 5. Presentation Angles

### Angle 1: Prufrock as a Protocol Compression Laboratory

**Frame**: Every protocol compresses. Prufrock is a controlled experimental environment for studying what happens when compression is *the point* — where the protocol's output is defined by what it preserves and what it discards. Present the contribution tuple as a "compression specification" — seven fields that define exactly which aspects of a human moment survive protocolisation. Then generalise: every protocol in the Basket of Protocols has an implicit compression specification. Prufrock makes it explicit and therefore studiable.

**Why this works for the SIG**: It connects to nondimensionalisation, to the ETTO principle, to the ten dimensions of sufficiency, and to observability — all existing SIG interests. It positions Prufrock as a tool for studying a general protocol property, not as a poetry project.

**Risk**: The compression framing may feel too abstract to SIG members who want concrete formalisable problems. Pair with specific comparisons (Prufrock's compression spec vs. handwashing's compression spec vs. Ethereum's compression spec).

### Angle 2: Prufrock as a Case Study in Designed Negative Space

**Frame**: The SIG has studied what protocols do. Prufrock contributes a formal concept for what protocols *don't do* — and argues that the design of absence is as important as the design of presence. Walk through the formalisation showing what is recorded (7 fields) and what is not (mental state, alternatives considered, surrounding context, emotional valence), and argue that the unrecorded space is what makes the output meaningful rather than merely valid.

**Why this works for the SIG**: It provides a new analytical tool applicable across the Basket of Protocols. It connects to Protocol Drift (drift happens in negative space), to thick/thin rules (thick rules have more negative space within them), to Observability (observability has a designed complement). And it introduces a genuinely new concept: the SIG has not named this phenomenon.

**Risk**: "Negative space" may sound too literary for some SIG members. Ground it immediately in examples from protocols they already study. The argument must show that negative space is a *formal* property — specifiable, measurable, comparable across protocols — not a vague aesthetic intuition.

### Angle 3: Prufrock as a Stigmergic Autocurriculum

**Frame**: Combine the SIG's two most recent topical sessions (Stigmergy May 1, Autocurricula April 3). Prufrock is a protocol in which (a) the coordination medium is a shared environment modified by participant contributions (stigmergy), and (b) each contribution changes the challenge facing subsequent participants, creating a self-generating sequence of prompts with no external curriculum (autocurriculum). The output — a poem — is the emergent product of this stigmergic autocurriculum.

**Why this works for the SIG**: It demonstrates that stigmergy and autocurricula, usually discussed in the context of insects or multi-agent RL, apply to a human aesthetic practice. It tests whether the SIG's formalisms transfer across domains. And it provides a concrete system small enough to simulate and study — unlike climate protocols or blockchain governance, a Prufrock experiment with 14 participants over 14 days is tractable.

**Risk**: The connection might feel forced — "everything is stigmergy if you squint." Prevent this by being precise about where the mapping holds and where it breaks. The key difference from insect stigmergy is that Prufrock's agents are *cognitive* — they don't just respond to environmental cues, they interpret them. Flag this as a genuine open question (Q4 above) rather than pretending the mapping is tighter than it is.

---

## 6. Mapping Summary Table

| Prufrock Element | Primary SIG Framework | Secondary SIG Framework | Mapping Strength |
|---|---|---|---|
| Contribution tuple | Actor model (message) | Session types (typed message) | Strong |
| Spatiotemporal binding $(t_p, t_r, g)$ | Observability | Allen interval algebra | Novel (no direct SIG precedent) |
| Ledger $\mathcal{L}^*$ | Stigmergy (sematectonic surface) | Hardness / cryptographic cast | Strong |
| Parent relation $\prec$ / DAG | Process calculi (trace) | Protocol composition | Strong |
| Schedule / interruption | Maneuver automata (forced transition) | Allen interval algebra | Productive analogy |
| Prompt selection $\mathrm{Sel}$ | Autocurricula (non-stationary environment) | Correlated equilibrium | Productive analogy |
| Form constraint $\mathcal{F}$ | Thick/thin rules | Generative space constraints | Strong |
| Seed | Initial conditions / exogenous injection | Protocol stewardship | Moderate |
| Forfeit handling | Observable non-events | ETTO (thoroughness bias) | Strong |
| Compression-fidelity trade (P7) | — | Nondimensionalisation (candidate) | Novel |
| Negative space | — | Protocol drift (complement) | Novel |
| Self-exclusion (P5) | Symmetry / impossibility | — | Clean |
| Temporal monotonicity (P2) | Causal ordering | — | Clean |
| Non-equivocation (P4) | Byzantine fault tolerance | — | Clean |

---

## 7. Tactical Notes

**Know the room.** The SIG includes people from formal CS (Patrick Nast on process calculi), robotics/control theory (maneuver automata), social science (Fotis on ethnography, Amita on mechanism design), creative practice (Ben on music notation, Hao Guang on poetry), and generalist protocol thinkers (Venkat, Mike Travers). Robert has attended and contributed to SIG sessions, which provides standing. Pitch to the formal-CS contingent through the session-types and DAG structure; to the social-science contingent through thick/thin rules and negative space; to the generalists through compression-fidelity and the Basket of Protocols.

**What to avoid.** Do not lead with poetry. Lead with formal structure and let the domain emerge. The SIG's own framing talk uses handwashing — a mundane protocol — to demonstrate that formalisation applies to everyday behaviours. Prufrock should do the same: present the formal structure, show that it generalises, and then note that the domain happens to be poetry.

**What to emphasise.** The SIG has expressed frustration with a lack of crisp motivating examples (see the Atomic Protocol Questions README: "in the absence of a crisp motivating example, it can be difficult to see the benefit of a particular tool"). Prufrock is a crisp motivating example: it is small, fully specified, parameterised, and simulatable. It is a protocol that the SIG could actually implement and study, which distinguishes it from their usual examples (climate treaties, blockchain governance) that are too large to experiment with.

**Robert's unique position.** The transhuman-protocols thread (`../transhuman-protocols/README.md`) frames Robert's research as studying protocols for effective human-AI collaboration. Prufrock is a human-only protocol in an era of AI, which is itself a protocol-theory statement: it asks what happens when you design a protocol that cryptographically excludes AI from the generative process while potentially using AI infrastructure for coordination. This connects to the SIG's Protocolizing Agent Space session (April 17), where Robert contributed the point about cognitive sovereignty and drift management. Frame Prufrock as the complementary project: where that session asked how to protocolise AI space, Prufrock asks how to protocolise a *non-AI* space within a world increasingly dominated by AI.

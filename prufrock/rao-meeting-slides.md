# Meeting Prep — Venkatesh Rao, Protocol Institute
**Monday 11 May 2026 | 1:1 with Venkat**

---

## Meeting Shape

Three topics, each flowing into the next. The conversation should feel like a natural progression, not three separate pitches. Transition points are marked so you can steer or skip based on Venkat's energy.

| # | Topic | Time | Goal |
|---|---|---|---|
| 1 | Prufrock → Long Now application | ~20 min | Get feedback to improve the Lab 001.1 application |
| 2 | Prufrock → Protocol Institute | ~15 min | Explore PI support, FPT SIG presentation, symposium slot |
| 3 | Interspecies protocols / human-AI | ~15 min | Gauge interest; explore path to Long Now Lab 001.3 curriculum |
| — | Open / next steps | ~10 min | Concrete follow-ups, introductions |

**The throughline:** All three topics are aspects of the same question — how do we design protocols that authenticate and preserve human expression across time, across difference, and across species boundaries (including AI)? Prufrock is the concrete instance; the Long Now framing gives it temporal scale; the interspecies angle gives it conceptual reach.

---

## Framing Note

Venkat already knows Robert as "the unofficial poet of Protocol Institute" / "inaugural poet laureate" (PI General Assembly, 29 Apr 2026). He's seen the poetry protocols talk. He knows Robert's FPT SIG contributions, including the cognitive sovereignty point from the Protocolising Agent Space session (April 17). The task is not to introduce yourself — it's to show Venkat three concrete things he can help with, each connected to PI's mission.

---

# PART 1: PRUFROCK → LONG NOW

## 1.1 — Opening: Poetry as the Oldest Long Now

**Title:** The Oldest Long Now

- Poetry has bound the *long* (timeless themes) to the *now* (concrete individual moments) for four thousand years. It is the human timepiece that predates the clock.
- The Prufrock Protocol takes this intrinsic long-now structure and makes it *the* timepiece — sampling and recording subjective experience longitudinally in authenticated form.
- The longitudinal claim: poets hundreds of years from now respond to poems written today. The chain grows across centuries. The ledger is the record.

**Talking points:**
Open here because it's the frame Venkat hasn't heard. He knows Prufrock as a protocol; he hasn't heard it pitched as a *time-marking instrument* for Long Now. The long-now framing isn't a marketing angle — it's the project's actual claim: that poetry's long-now structure can be surfaced and protocolised to mark a new kind of time.

Connect to Long Now's existing inspirations from the callout: the 10,000-Year Clock marks time mechanically; Katie Paterson's Future Library marks it through sealed literary capsules; blockchains mark "sovereign time" independent of third-party interference. Prufrock marks time through *continuous sampling* of situated human consciousness — not sealed away but actively growing, each chain extending as new participants respond to what came before.

**References:** cf. concept.md (500-word application text); cf. rough-notes.txt ("Poetry is one of the longest of long nows"); cf. Long Now Labs launch post (longnow.org, 29 Apr 2026) — protocols as "hidden infrastructure of cooperation"; cf. pitch.md §"The Problem" — trust collapse in digital expression.

---

## 1.2 — The Protocol in 90 Seconds

**Title:** Five Invariants, One Sentence Each

- **Interrupts** — reaches into your life at a moment not of your choosing.
- **Confronts** — shows you someone else's authenticated moment.
- **Records** — captures your response with seven signed fields: content, parent hashes, author key, prompt time, response time, geolocation, signature.
- **Authenticates** — cryptographically binds content to identity, moment, place, and lineage.
- **Preserves lineage** — DAG of authenticated moments; tampering invalidates descendants.

**Talking points:**
Venkat has heard versions of this. Keep it to 90 seconds. The point here is to remind him of the formal structure so the Long Now framing doesn't sound like hand-waving. Emphasise: these five are *protocol constants* — they hold across every instantiation. The sonnet trial is one experiment; the protocol is the invariant structure beneath it.

The key line for Long Now: the lineage preservation means the chain *cannot be silently revised*. A poem started today and extended by poets in 2126 carries cryptographic proof of every ancestor. This is what makes Prufrock a long-now instrument rather than just a collaborative writing exercise.

**References:** cf. formalisation.md §2 (contribution tuple, validity rules); cf. pitch.md §"The Protocol".

---

## 1.3 — The Long Now Application: Deliverable and Pace Layers

**Title:** *Continual Proof: Volume I* — Artefacts at Four Speeds

- **Operational (live):** open-source mobile app + public web ledger — every line viewable, navigable across geographic, temporal, and dialectical lenses.
- **Per-line:** Bitcoin Ordinal inscription per signed line — "sovereign time" anchor named in the Long Now callout.
- **Annual:** *Continual Proof: Volume I* — hand-bound print codex (edition of 250), deposited at the Long Now Library and The Interval, dated in Long Now Zero (02028).
- **Decennial (v2):** Rosetta-class nickel-disk etching of each decade's spine for ten-thousand-year readability.

**Talking points:**
Walk through the pace-layer strategy (Brand's framework, which Long Now already uses). The protocol produces artefacts at fashion, commerce, and culture speeds simultaneously — the same ledger expressed as live web, annual codex, and millennial etching. This is not redundancy; it's pace-layer coherence.

The named deliverable — *Continual Proof* — comes from Stephen Dunn's "Different Hours." The title itself is the project's wager: continual proof you've been alive, cryptographically signed, across centuries.

The scoped v1 is concrete: 14 poets × 14 days × 14 poems × 2 cohorts, trial autumn 2027, codex Spring Equinox 02028. Institutional pairing: Long Now (custodian), Protocol Institute (protocol design), Poetry Society UK + Kundiman US (literary cohort), Long Bets (registered prediction at trial close).

**ASK:** Does this deliverable structure work for the review panel? Is the pace-layer framing the right register for Long Now? What would Venkat change?

**References:** cf. `memory/projects/prufrock-protocol.md` §"v1 deliverable" + §"Institutional pairing" (the deliverable spec content; the previous standalone `artefact-and-v1.md` was retired and absorbed here); cf. `memory/projects/long-now-lab-001-1.md` (timeline, application fields, review panel); cf. `to-review/prufrock/concept.md` (500-word application text — "Poetry is among the oldest long nows we have").

---

## 1.4 — Feedback on the Application

**Title:** What Would You Change?

Specific questions for Venkat:

1. **Framing:** The concept text leads with "poetry is the oldest long now" and ends with "continual proof someone, somewhere, was alive." Is this the right register for the review panel, or does it need more technical concreteness?

2. **Institutional pairing:** The application names Long Now, PI, Poetry Society UK, Kundiman US, and Long Bets. Is this the right set? Is PI's involvement a strength or a distraction in the application?

3. **The Long Bet:** Candidate prediction — *"By 02050, a Prufrock-protocol chain will be canonised in a major literary anthology of record."* Too audacious? Not audacious enough?

4. **Supporting media:** The application allows up to 10 files. Current plan: formalisation PDF, protocol diagram, video explainer (~2:30). What else would strengthen it? Would the poetry-blockchain-precedents review (7 prior projects analysed) help or clutter?

5. **Denise Hearn:** Venkat and Timber have been working with Denise on the Labs. Would it be useful for Robert to connect with her directly before the application deadline (June 5)?

**Talking points:**
This is the most important part of Part 1. Let Venkat react to the application as someone who helped design the Labs programme. His feedback here is worth more than any amount of solo iteration.

If he pushes back on the poetry framing, the fallback position is: the protocol is medium-agnostic; poetry is the first experiment. The five invariants hold for any medium. The Long Now application happens to use the sonnet trial because it's the most concrete and poetic expression of the long-now claim.

**References:** cf. long-now-lab-001-1.md (full application details, timeline, sibling labs); cf. application.pdf (Google Form fields).

---

## ▸ TRANSITION TO PART 2

**Pivot line:** *"The Long Now application is one expression of the protocol. The other is what it contributes to protocol theory itself — which is where PI comes in."*

If Part 1 went well, this transition is natural. If Venkat seems less interested in the Long Now angle, lead Part 2 with: *"Let me show you what the formalisation contributes to the SIG's vocabulary."*

---

# PART 2: PRUFROCK → PROTOCOL INSTITUTE

## 2.1 — Novel Contributions to Protocol Theory

**Title:** Three New Terms for the SIG

- **Compression-fidelity trade** — the relationship between what a protocol records and what it must discard. Every protocol has one; Prufrock makes it explicit. Seven fields recorded; everything else (mental state, alternatives considered, surrounding context) is the protocol's *negative space*. Candidate for nondimensionalisation.
- **Negative space as design category** — the designed complement of observability. What a protocol *doesn't do* is as important as what it does. Inverts the SIG's usual analytical frame. Hypothesis: a protocol's negative space may determine its susceptibility to drift — too large and practices diverge uncoordinated; too small and the protocol becomes brittle.
- **Aesthetic enforcement** — a class of constraint (sonnet rhyme scheme, ghazal radif, sestina end-word rotation) with no enforcement mechanism in the traditional sense but enormous structuring power. Enforced by visible commitment: violations are apparent to subsequent participants through the stigmergic surface. Coordination without consensus.

**Talking points:**
Frame these as contributions to the SIG's vocabulary, not as Prufrock-specific jargon. Test each with a non-Prufrock example Venkat will recognise:

Compression-fidelity: handwashing compresses pathogen dynamics into temporal rules; the fidelity loss is microbiome specificity. Ethereum compresses economic intent into transactions; the fidelity loss is social context. The SIG discusses trade-offs extensively (ETTO, tension curves, nondimensionalisation) but has no term for this specific trade-off.

Negative space: traffic protocols leave road-rage in negative space. Academic peer review leaves the reviewer's emotional state in negative space. The SIG has discussed observability (June 27 session) but frames unobservability as a *limitation*. Prufrock frames it as a *feature*.

Aesthetic enforcement: connects to the SIG's "Floor > Ceiling" principle (Design Principle #9) and to Daston's thick/thin distinction. Form constraints raise the floor without exhorting excellence. The question: does this generalise beyond aesthetic domains? Coding conventions? Academic citation norms?

**References:** cf. FPT positioning §§3.1–3.3 (full arguments for each); cf. formalisation.md §8, P7 (compression-fidelity as formal property); cf. Daston, *Rules* (FPT SIG, Design Principles session); cf. Hollnagel, ETTO Principle (FPT SIG, Group 4 insights); cf. Stinson-Schroff, "Safe New World" (Protocol Reader ch. 3) — safety as dynamic non-event; cf. Chambliss, "The Mundanity of Excellence" (FPT SIG, Design Principles); cf. poetry protocols talk slides 5, 9 (compression algorithm — Heaney/Beowulf, Gestalt — greater than sum of parts).

---

## 2.2 — SIG Framework Mappings

**Title:** Where Prufrock Connects to What the SIG Already Studies

- **Stigmergy (May 1 session):** The poem-ledger is a sematectonic stigmergic surface — coordination through the state of a constructed environment. Each contribution modifies the shared structure and cues subsequent contributions. But with a crucial difference: the cues are *aesthetic* rather than functional. Does this change the coordination dynamics?

- **Autocurricula (April 3 session):** Each contribution changes what subsequent participants will see — a self-generating sequence of prompts with no external curriculum. The output is the emergent product of a stigmergic autocurriculum.

- **Manoeuvre automata (Oct 17 session):** Participants alternate between a "trim state" (ordinary life) and a "manoeuvre" (poetic composition) triggered by the protocol's interruption. Timing modes parameterise the trigger.

- **Session types (Aug 8 session):** The contribution tuple maps to a typed message in a multiparty session. Form constraints function as session-type refinements — narrowing admissible messages at each position.

- **Protocol drift (Sept 13 session):** Each chain through the DAG is a particular drift trajectory from the seed. Comparing chains reveals how the same initial conditions diverge through different participants' situated responses.

**Talking points:**
Don't present all five — pick 2-3 based on what Venkat responds to. The stigmergy + autocurricula combination is the strongest (Angle 3 in the FPT positioning doc). The key selling point: Prufrock is *small enough to simulate and study*. Unlike climate treaties or blockchain governance, a 14-person, 14-day experiment is tractable. The SIG has expressed frustration with a lack of crisp motivating examples (cf. Atomic Protocol Questions README). Prufrock is one.

**References:** cf. FPT positioning §1 (full concept mapping, with mapping-strength ratings); cf. Theraulaz & Bonabeau, "A Brief History of Stigmergy" (FPT SIG, Stigmergy session); cf. Parunak, "A Survey of Environments and Mechanisms for Human-Human Stigmergy"; cf. Leibo et al., "Autocurricula and the Emergence of Innovation" (FPT SIG, Autocurricula session); cf. Frazzoli et al., "Maneuver-based motion planning" (FPT SIG, Manoeuvre Automata session); cf. Allen's Interval Algebra (FPT SIG, Notation session); cf. Stark, "Atoms, Institutions, Blockchains" (Protocol Reader ch. 7) — cryptographic hardness applied to aesthetic rather than financial commitments.

---

## 2.3 — What Robert Wants from PI

**Title:** Three Asks

1. **FPT SIG presentation slot** — Present Prufrock as a formal case study. 30-minute slot, interactive. Target: before the fall symposium so the formalisation is stress-tested by Patrick Nast (process calculi), James (robustness), Mike Travers (actor models) before a larger audience. This is the most important ask.

2. **Protocol Symposium (Fall 2026)** — Present at the second symposium. Frame: "A studiable, simulatable protocol for protocol theory" — Prufrock as the SIG's first protocol it can actually *run*.

3. **Cohort recruitment:** The v1 sonnet trial plans two cohorts — poets (via Poetry Society UK / Kundiman US) and protocol theorists / laypeople. Several SIG members are natural participants: Hao Guang Tse (poet), Ben (music notation), Patrick Nast (formal methods). Could PI help recruit the second cohort?

**Talking points:**
Don't present as demands. Frame as: "Here's where I think the natural leverage is — what do you think?"

If Venkat is enthusiastic, push for the SIG slot as the concrete next step. If he's cautious, suggest a smaller move: share the formalisation with Patrick Nast for informal feedback first, then decide on a SIG presentation.

**Fallback:** If Venkat sees Prufrock as interesting but not a PI priority, the minimum viable outcome is his feedback on the Long Now application (Part 1) and an introduction to Denise Hearn.

**References:** cf. FPT positioning §7 (tactical notes — know the room); cf. PI General Assembly transcript — upcoming Protocol Symposium fall 2026; cf. parameterisation spec §6.3 (free-form micro experiment as pilot format).

---

## ▸ TRANSITION TO PART 3

**Pivot line:** *"Prufrock is a human-only protocol — it cryptographically excludes AI from the generative process. But my broader research programme is about the opposite: how do we design protocols for humans and AI to collaborate? I've been thinking about this through an unexpected lens."*

If the conversation is running short, compress Part 3 into a 5-minute teaser and offer to follow up separately.

---

# PART 3: INTERSPECIES PROTOCOLS / HUMAN-AI

## 3.1 — The Research Programme

**Title:** Transposing Human Collaboration into Transhuman Protocols

- Robert's research statement (`transhuman-protocols/README.md`): effective human collaboration methodologies share design properties — data gathering, clarification, inspectability, accountability, shared context, standards for language and behaviour. These recur across traditions (GTD, agile, pair programming).
- The hypothesis: human collaboration paradigms can be *transposed* into transhuman protocols by deriving fundamental characteristics from concrete implementations and recasting them for human-AI use.
- The expansion: we may have more to learn from *humans with differences* than from studying "baseline" human collaboration.

**Talking points:**
This is the bridge from Prufrock (human-only, poetry, authentication) to the broader programme (human-AI, any domain, effectiveness). The connection: Prufrock studies what happens when you protocolise situated human expression. The interspecies angle asks what happens when you extend protocolised collaboration across cognitive boundaries — whether those boundaries are human-AI, neurotypical-neurodivergent, or cross-cultural.

Introduce the reframe gently: most human-AI collaboration research treats AI as a tool to be aligned or a mirror to be calibrated. What if we treated AI as a *new species* — with its own cognitive style, its own strengths and failure modes, requiring *interspecies* communication protocols rather than tool-use protocols?

**References:** cf. `transhuman-protocols/README.md` (full research statement); cf. FPT SIG, "Protocolizing Agent Space" session (April 17) — Robert's point about cognitive sovereignty and drift management; cf. Asparouhova, "Dangerous Protocols" (Protocol Reader ch. 9) — protocol-as-identity, Protocolisation 2.0.

---

## 3.2 — Humans with Differences as a Source Domain

**Title:** Neurodivergent Communication, Cross-Cultural Protocols, Interspecies

- **Neurodivergent communication:** Protocols designed for neurotypical-neurodivergent collaboration (explicit turn-taking, sensory accommodation, processing-time windows, concrete language) solve problems that are structurally identical to human-AI collaboration challenges. Robert works with these populations directly — this isn't abstract.
- **Cross-cultural protocols:** Communication across cultural boundaries (high-context/low-context, direct/indirect, different temporal norms) has generated rich protocol knowledge that the human-AI literature ignores. The "alignment" framing assumes a single target; cross-cultural protocols assume *irreducible difference* and design for interoperability anyway.
- **Interspecies communication:** The frontier — dolphin communication research, primate gesture studies, mycorrhizal signalling. These are protocols across cognitive boundaries so different that the usual assumptions about shared context break down entirely. If protocols can work here, they can work for AI.

**Talking points:**
The argument has three layers, each progressively more speculative. Lead with the neurodivergent layer — it's the most concrete and comes from Robert's direct experience. The cross-cultural layer extends it. The interspecies layer is the Long Now connection.

The key insight: in all three cases, the productive move is *not* to make the other party more like you (the "alignment" error). It's to design protocols that accommodate irreducible difference — that work *because* of the difference, not despite it. The SIG's thick/thin distinction (Daston) is relevant: neurodivergent protocols tend to be *thinner* (more explicit, less reliant on shared tacit knowledge) and this thinness is a feature, not a limitation. Human-AI protocols may need the same thinness.

Connect to the SIG's existing vocabulary: the ETTO principle (Hollnagel) applies — neurodivergent protocols choose thoroughness over efficiency in communication, which is exactly the trade-off human-AI protocols need to make. Goodhart's Law (Manheim & Garrabrant) applies — optimising for "human-likeness" in AI is a Goodhart failure; the metric (human-likeness) is not the goal (effective collaboration).

**References:** cf. `transhuman-protocols/README.md` — "wider contextual implications for individuals (cognitive load / sovereignty / debt)"; cf. Hollnagel, ETTO Principle (FPT SIG, Group 4 insights); cf. Manheim & Garrabrant, "Categorizing Variants of Goodhart's Law" (FPT SIG, Integration Jigsaw); cf. Daston, *Rules* — thick/thin distinction; cf. Walch, "The Protocol System Experience" (Protocol Reader ch. 4) — bistable perception, individual vs system view; cf. Kittel & Shorin, "Unprotocolized Knowledge" (Protocol Reader ch. 15) — "protocols are unreasonably sufficient and reasonably insufficient at the same time."

---

## 3.3 — Connection to Long Now Lab 001.3: Interspecies Protocols

**Title:** From Human-AI to Interspecies — The Long Now Thread

- Long Now Lab 001.3 is an open call for *interspecies protocols* — likely taking the form of a course, starting late 2026 or early 2027.
- Robert's human-AI research programme is a natural bridge: AI is the most accessible "other species" for protocol experimentation. The protocols designed for human-AI collaboration can inform — and be informed by — protocols for human-dolphin, human-fungal-network, or human-forest communication.
- The throughline from Prufrock: Prufrock authenticates *situated human expression*. The interspecies extension asks how to authenticate and preserve *situated cross-species expression* — whether the other species is biological or artificial.

**Talking points:**
This is the most speculative part of the conversation. Read Venkat's energy. If he's engaged, explore the connection between the three labs: Lab 001.1 (Book of Time — Prufrock), Lab 001.2 (Epistemic Cycles — adjacent), Lab 001.3 (Interspecies Protocols — Robert's broader programme). A researcher contributing to two of three labs in the inaugural series is a strong institutional signal.

If Venkat is less engaged, compress to the ask: "I'd like to explore whether my human-AI protocols work fits the interspecies call. Can you connect me with whoever is designing the 001.3 curriculum?"

The Long Now framing for interspecies-AI: Long Now thinks in 10,000-year timescales. In 10,000 years, the distinction between "artificial" and "biological" intelligence may be meaningless. Designing interspecies protocols that include AI is *already* long-term thinking about how diverse intelligences will coordinate.

**References:** cf. long-now-lab-001-1.md (sibling labs: 001.2 Epistemic Cycles, 001.3 Interspecies Protocols); cf. Long Now Labs launch post — "protocols shape how we... make decisions in relation to other species and new technologies"; cf. PI General Assembly transcript — Amber Hu on "automatically protocol negotiation between agents," Helena on "Trust Experience Design" and protocol futuring, Venkat on "AI exploding all over the place as a new substrate."

---

## 3.4 — What Robert Wants Here

**Title:** Gauging Interest, Not Pitching

1. **Venkat's read:** Does the "AI as interspecies" framing resonate with PI's direction? Or is it a stretch?

2. **Connections:** Who else in the PI/Long Now orbit is thinking about this? Amber Hu (automatically negotiating agent protocols, per the General Assembly)? Helena (protocol futuring at NYU Shanghai)? Mike Travers (actor models, "the more human side of protocols")?

3. **Path to 001.3:** If the interspecies work is interesting, what form should it take? A paper for Protocolized magazine? A SIG session? A direct application to the 001.3 call?

4. **PI support:** Could PI provide any of: a reading group, a publication venue (Protocolized), institutional affiliation, connection to the Long Now 001.3 curriculum designers?

**Talking points:**
Frame this as genuine exploration, not a pitch. Robert is early in thinking about the interspecies angle — he has the human-AI research statement and the neurodivergent experience but hasn't yet written the interspecies framing up. Venkat's reaction will determine whether to invest in developing it.

**Fallback:** If Venkat doesn't see the interspecies connection, the minimum viable outcome is: "Interesting direction, not for PI right now, but talk to [X person]." That's still valuable.

---

# ANTICIPATED QUESTIONS

### Q: "Why poetry for Long Now? Isn't this niche?"

**Response:** Poetry is the *least* niche framing for Long Now. It's the oldest continuous human cultural practice — older than any institution, older than writing itself (oral traditions). The 10,000-Year Clock marks mechanical time; Prufrock marks *experiential* time. Every Long Now inspiration in the callout (Clock, Future Library, Cosmic Calendar, Doomsday Clock) is a way of marking time. Prufrock adds another: marking time through situated moments of human consciousness, compressed into the form that has done this longest.

cf. concept.md; cf. rough-notes.txt ("poetry is one of the longest of long nows").

### Q: "How is this different from Katie Paterson's Future Library?"

**Response:** Future Library seals writing in a time capsule — 100 authors, one manuscript each, unsealed in 2114. It's beautiful but static: nothing happens between sealing and opening. Prufrock is *active* across its entire timeline — each chain grows as new participants respond to what came before. The protocol produces artefacts continuously, not at a single reveal. And it's authenticated: every node carries cryptographic proof of its lineage. Future Library trusts the institution; Prufrock trusts the mathematics.

cf. concept.md; cf. long-now-lab-001-1.md (Future Library listed as callout inspiration).

### Q: "How is Prufrock different from exquisite corpse?"

**Response:** Four structural differences: (1) randomised interruption at moments not of the participant's choosing (exquisite corpse is voluntary); (2) forced confrontation with another's *authenticated* expression (exquisite corpse shows partial or no context); (3) cryptographic authentication and hash-chained lineage (exquisite corpse has no verification); (4) permanent forfeit recording — absence is data (exquisite corpse ignores absence). These produce a different kind of artefact: not a parlour game but an authenticated record of distributed human experience over time.

cf. pitch.md §"An Enduring Artefact".

### Q: "What's the implementation status?"

**Response:** Formalisation complete. Parameterisation spec complete. Application concept drafted (500 words, in review). What's needed for v1: (a) client app for interruptions and signed responses, (b) ledger backend (any authenticated append-only data structure), (c) scheduling service. Scoped v1 targets trial autumn 2027, codex Spring Equinox 02028.

cf. formalisation.md §10; cf. `memory/projects/prufrock-protocol.md` §"v1 deliverable" (scoped v1).

### Q: "Can you really run a 14-person trial through PI?"

**Response:** The SIG has the right people. Hao Guang Tse is a poet. Ben works on music notation. Patrick Nast does formal methods. These are natural participants for the protocol-theorist cohort. The poet cohort comes from Poetry Society UK and Kundiman US — both prior partners from Transatlantic Poetry. The pilot could be smaller first: a 5-person, 5-day haiku-relay (cf. parameterisation spec §6.3) to test the mechanics before committing to the full sonnet trial.

cf. FPT positioning §7 (tactical notes — know the room); cf. parameterisation spec §6.3 (free-form micro experiment).

### Q: "Isn't 'AI as interspecies' just a metaphor?"

**Response:** It's a *productive* metaphor that generates different design moves than "AI as tool" or "AI as mirror." Tool-use protocols assume the tool has no preferences and serves the user. Mirror protocols assume the AI should reflect the user's own patterns back. Interspecies protocols assume *irreducible cognitive difference* and design for interoperability across that difference. The design moves are different: explicit signalling (not implicit inference), accommodation of different processing speeds (not synchronisation), mutual adaptation (not one-sided alignment). These are the same design moves that work for neurodivergent communication and cross-cultural coordination. Whether the metaphor is "just" a metaphor depends on whether it produces better protocols than the alternatives — and that's an empirical question.

cf. `transhuman-protocols/README.md`; cf. Kornfeld & Hewitt, "The Scientific Community Metaphor" (FPT SIG, Actor Models session) — agents organised on the model of a scientific community, proposals and confirmation without central authority. The metaphor generated productive computer science for decades.

### Q: "Where does Prufrock sit relative to PI's research programme?"

**Response:** Three positions. First, a *case study* for the FPT SIG — small, fully specified, parameterised, runnable. Second, a *Long Now application* that demonstrates PI's ability to produce concrete, fundable protocol designs (good for PI's institutional credibility). Third, a bridge between PI's protocol-theory work and Long Now's long-term-thinking mission — the kind of institutional partnership Venkat called for at the General Assembly ("we need the mid-career ones amongst you to help this little baby institution get off the ground").

cf. FPT positioning §5 (presentation angles); cf. PI General Assembly transcript — Venkat's call for institutional partnerships.

### Q: "Can the compression-fidelity concept actually be formalised?"

**Response:** It can be formalised as a ratio: recorded observables / total observables at the moment of contribution. The challenge is defining the denominator. One approach: define a canonical set of observable dimensions (identity, time, place, content, lineage, emotional state, context, prior thought, sensory environment, social context) and characterise each protocol by which it records and which it discards. The ratio is dimensionless and comparable across protocols. Whether this converges to something useful is empirical — but it's at least *askable*.

cf. FPT positioning §4, Q1; cf. FPT SIG, Nondimensionalisation page.

---

# MEETING OUTCOMES — SCORECARD

Track which outcomes you achieved:

| Outcome | Priority | Status |
|---|---|---|
| Feedback on Long Now application concept | Must-have | |
| Feedback on deliverable/pace-layer structure | Must-have | |
| Venkat's view on PI involvement in the application | Must-have | |
| Introduction to Denise Hearn | High | |
| FPT SIG presentation slot (agreed or pathway to) | High | |
| Protocol Symposium mention / slot | Medium | |
| Venkat's read on the interspecies/AI framing | Medium | |
| Connections to relevant PI/Long Now people for interspecies work | Medium | |
| Path to Long Now Lab 001.3 involvement | Stretch | |
| Cohort recruitment help for sonnet trial | Stretch | |

---

# CONVERSATION FLOW — IF/THEN

**If Venkat is most excited about the Long Now angle:**
Spend longer on Part 1. Drill into application feedback. Ask about Denise. Compress Part 2 to: "Here's what I'd present at the SIG" (2 minutes). Compress Part 3 to: "I'm also thinking about 001.3 — can we schedule a follow-up?"

**If Venkat is most excited about the FPT contributions:**
Move through Part 1 quickly (he'll already see the Long Now fit). Expand Part 2 — let him interrogate the formalisation, the vocabulary contributions, the open questions. The five questions from §4 of the FPT positioning doc are: (1) nondimensionalising compression-fidelity, (2) negative space and drift, (3) aesthetic enforcement as correlated equilibrium, (4) stigmergy with aesthetic environment, (5) extending liveness to experiential coverage. Pick 2-3 based on his reactions. Compress Part 3.

**If Venkat is most excited about the interspecies angle:**
This is the surprise scenario. If it happens, lean in. The interspecies framing connects PI to Long Now's Lab 001.3 in a way that gives PI institutional reach. Ask about the 001.3 curriculum design: who's leading it? What's the timeline? Is there a call for curriculum proposals? Could Robert's human-AI research become a module?

**If Venkat is politely interested but not enthusiastic about any angle:**
Focus on the minimum viable outcomes: feedback on the Long Now application, introduction to Denise Hearn, and one concrete next step (share the formalisation with Patrick Nast for informal review). Don't push.

**If Venkat brings up something unexpected:**
Follow his thread. The three-part structure is prep, not a script. If he wants to talk about PI's institutional strategy, or his "new nature" framing, or the Strange Rules Venice show, go with it and weave your points in naturally.

---

# QUICK REFERENCE: SOURCE DOCUMENTS

| Source | Path | Key content |
|---|---|---|
| Pitch | `prufrock/README.md` | Five invariants, compression argument, domain rationale (absorbed the previous `pitch.md`) |
| Formalisation | `prufrock/formalisation.md` | Full mathematical spec, 7 properties (P1–P7), experiment definitions |
| FPT Positioning | `prufrock/fpt-positioning.md` | Concept mapping to SIG, novel contributions, presentation angles |
| Parameterisation | `prufrock/mockup/spec/protocol-parameterisation.md` | Parameter space, experiment definitions for ghazal, sestina, haiku-relay |
| Long Now Lab 001.1 | `prufrock/memory/projects/long-now-lab-001-1.md` | Timeline, application fields, sibling labs, review panel |
| Application concept | `to-review/prufrock/concept.md` | 500-word Long Now application text |
| Artefact + v1 spec | `prufrock/memory/projects/prufrock-protocol.md` §"v1 deliverable" + §"Institutional pairing" | Named deliverable (Continual Proof: Volume I), pace layers, institutional pairing, scoped v1 |
| Protocol Reader distillation | `transhuman-protocols/protocol-reader/distillation.md` | 27-essay review, promotion shortlist |
| FPT SIG distillation | `transhuman-protocols/fptsig/distillation.md` | Reference catalogue scored against human-AI thesis |
| FPT SIG references | `transhuman-protocols/fptsig/references.md` | Thematic grouping of SIG sources |
| Research statement | `transhuman-protocols/README.md` | Broader programme: effective protocols for human-AI collaboration |
| Poetry protocols talk | `poetry-talk/poetry-protocols-notes.pdf` | 40-slide talk: compression, Gestalt, Fermi-Dyson, infinite game |
| PI General Assembly | `transhuman-protocols/pi/20260429 1600 Transcription.txt` | Venkat on "new nature," Timber on PI launch, member round-robin |
| Rough notes | `prufrock/rough-notes.txt` | Design evolution, thematic notes, domain ideas |

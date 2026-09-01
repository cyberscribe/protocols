---
title: "What is already substantiated about externalisation"
subtitle: "An evidence ledger for the human and AI sides of exec-fn-ai-org"
date: 2026-08-28
status: draft
see_also: external-protocols-model.md, external-protocols-review.md, knowledge-collapse-assumptions-evidence.md
---

# What is already substantiated about externalisation

> **The proposal this ledger produced:** `external-protocols-proposal-v2.md`.
>
> **Agent-facing register:** the operational short form of this document lives at
> `../../peakepro-diagnostics/cognition-assessment/settled-questions.md` — assume-and-cite rows,
> the open claims, and the citation traps. Amend this ledger first, then that file.

> **CLOSED 2026-08-31.** The audit is complete and the question it answers is settled. This file is
> now a reference, not a work item. See `settled-questions.md` §0 for what replaces it.

**Purpose: to stop modelling what is known.** Every claim below that carries a strong verdict is a claim we should *assume* in the simulator and *cite* in the paper, not re-derive. The value of the exercise is the residue — the short list at §5 of things nobody has shown, which is the actual contribution.

Two sides, because the diagram has two sides:

- **Human** — the GTD lineage for individuals (capture, next-action, context), the Kanban lineage for teams (visible board, WIP limits, pull).
- **AI** — cascading memory serving just-in-time context to an agent (the four store tiers and their loading pills).

The finding that matters most is in §4: **these two literatures have both studied *loading* and neither has studied *promotion*.**

---

## 1. Verdict at a glance

| # | Claim | Best evidence | Verdict | What it licenses |
|---|---|---|---|---|
| **E1** | External representation changes *task difficulty*, not merely memory demand | Zhang & Norman 1994, ToH isomorphs | **Strong** | Correspondence, not storage, is the right primitive |
| **E2** | Offloading improves performance on the offloaded task while access holds | Risko & Gilbert 2016; Gilbert et al. 2025 (Nat Rev Psych); 2025 meta-analysis | **Strong** | Stop simulating "does a store help" |
| **E3** | Offloading reduces encoding; losing access is *worse* than never offloading | Gilbert et al. 2025 | **Strong** | Cognitive debt exists at task level. Already ours to cite, not to prove |
| **E4** | The offloading decision tracks *confidence*, not ability; it is biased | Gilbert 2020; Chiu & Gilbert 2024 | **Strong** | The trust driver is metacognitive, not competence-based |
| **E5** | Committing a *plan* discharges load without discharging the task | Masicampo & Baumeister 2011 (6 studies); Gollwitzer & Sheeran 2006 (d≈0.65, 94 studies) | **Strong (meta) / Moderate (M&B)** | Externalisation-as-codification is a real, separate mechanism |
| **E6** | Scaffolds that help novices harm experts | Kalyuga, expertise reversal | **Moderate, contested** | Justifies the skill ladder / reviewer gating |
| **T1** | Transactive memory predicts team performance | Fausett et al. 2026, r=.44 (44 studies, 103 ES) | **Strong, with a measurement caveat** | Team-level externalisation pays. Do not use self-report to show it |
| **T2** | The *directory* ("who/what knows what") is the mechanism, not the repository | Ren & Argote 2011 | **Moderate–strong** | The store needs an index element in the diagram |
| **T3** | Protocols work when adopted as practice, not when mandated as artefact | Haynes 2009 vs Urbach 2014 | **Mixed — and the mixture is the finding** | Measure practice, never possession |
| **T4** | Kanban / WIP limits improve flow | Queueing theory (analytic); case studies (weak) | **Theory strong, evidence weak** | Cite the mechanism, never the brand |
| **A1** | More context is not better; performance degrades non-uniformly with length | Chroma 2025 (18 models); Liu et al. TACL 2024 | **Strong (see caveat)** | Loading is *not free on the AI side* |
| **A2** | Position within context governs retrieval — the middle is lost | Liu et al. TACL 2024 | **Strong** | Tier ordering is a real design variable |
| **A3** | A single irrelevant sentence materially degrades reasoning | Shi et al. ICML 2023 (GSM-IC) | **Strong** | One stale item in an ALWAYS tier is a live cost, not a rounding error |
| **A4** | A focused ~300-token input beats the full ~113k context on the same task | Chroma 2025, LongMemEval | **Strong (see caveat)** | Just-in-time context is established. Stop proving it |
| **A5** | *Plausible-but-wrong* distractors hurt more than noise; coherence compounds it | Chroma 2025 | **Moderate** | Empirical cousin of the sim's corroboration term |
| **L1** | Cognitive load shifts trust updating from process to outcome evidence | Chen et al. 2026 | **Strong** | The loop's first leg is given |
| **L2** | Substitutive AI use degrades unaided performance | Bastani 2025; Liu 2026; Wu 2026 | **Strong at task level** | The loop's second leg is given |
| **L5** | The act of *deciding what to promote* is capability-building cognition | — | **Unsubstantiated** | **Ours** |
| **L6** | Reading process evidence requires residual unaided capability | — | **Unsubstantiated** | **Ours** |
| **L7** | The task-level mechanism aggregates to months of professional practice | — | **Unsubstantiated** | **Ours** |

---

## 2. The human side

### 2.1 The one result the whole programme should be built on

**Zhang & Norman (1994).** Tower of Hanoi isomorphs, identical formal structure, rules moved one at a time from the head into the physical apparatus. Externalising rules did not make them *easier to remember* — it made them **impossible to violate**. Subjects made *zero* errors on externalised rules across all conditions, against multiple violations when the same rule was held internally.

This is the difference between a store and a representation, demonstrated thirty years ago, and it is the licence for the correspondence restart. An external protocol is not a memory aid with a better hit rate; it changes which errors are *available* to make. Our own visualisation principle — *show what the model makes impossible, not what it makes large* — turns out to be a restatement of the representational effect.

**What it costs us:** nothing. **What it saves us:** we never have to argue that externalisation helps. We argue about *which* externalisations change the possibility space and which merely store.

### 2.2 Offloading: benefits and costs are both established

The offloading literature (Risko & Gilbert's 2016 review; the 2025 *Nature Reviews Psychology* review; a 2025 meta-analysis in *Memory & Cognition*) has settled the shape:

- **Benefit** — better performance on the offloaded task, while access holds.
- **Cost 1** — reduced encoding of the offloaded content.
- **Cost 2** — **losing access leaves you worse off than if you had never offloaded.** Not merely back to baseline. Worse.
- **Cost 3** — partial offloading can interfere with recall of the *non*-offloaded items.

Cost 2 is cognitive debt, demonstrated, at task level, with no AI involved. We do not need to establish that externalisation creates dependency. We need to establish something the literature has not asked: whether a *particular discipline* of externalisation avoids it.

### 2.3 Offloading is driven by confidence, not competence

Gilbert and colleagues have shown across several designs that the decision to offload tracks metacognitive confidence rather than actual ability, and that people are systematically biased in that decision — a bias that moves with the *effort* of setting the reminder rather than with its value.

This is the trust-calibration story arriving from the memory literature instead of the human-factors literature. Two independent routes to the same structure, which is the same convergence we got when the gating rule appeared from the value side and the trust side simultaneously. Worth saying so in the paper.

### 2.4 GTD: the brand is unevidenced, the mechanism is not

There is no serious empirical evaluation of Getting Things Done as a package. Heylighen & Vidal (2008) is a theoretical reconstruction, not a test. **Do not cite GTD as evidence.**

But GTD's two load-bearing mechanisms are separately well-evidenced:

- **Capture-and-plan.** Masicampo & Baumeister (2011), six studies, ~600 participants: an unfulfilled goal impairs unrelated task performance and produces intrusive thoughts, and **making a specific plan eliminates the impairment without advancing the goal at all.** Mind-wandering fell from 65% to 33%; anagram performance rose from 6.6 to 9.6. The plan, not the progress, is what frees the mind. *(Caveat: Baumeister lab, pre-2011, in a literature with a poor replication record. Cite with the implementation-intention meta-analysis alongside it, not alone.)*
- **If-then structure.** Gollwitzer & Sheeran (2006): 94 studies, d ≈ 0.65, for specifying *when and where* over merely intending. This is one of the more robust findings in applied social psychology.

**Why this matters more than it looks.** These are not offloading results. Nothing is stored for later retrieval; the benefit arrives at the moment of *committing the form*. That is externalisation-as-codification, and it is the only place in the literature where an externalising act is shown to *reduce* load without substituting for the cognition. It is the closest existing support for our promotion claim — and it is an analogy, not a demonstration.

### 2.5 Teams: the directory, not the repository

Transactive memory is the strongest team-level result available: a 2026 meta-analysis (44 studies, 103 effect sizes) puts TMS against team outcomes at **r = .44**.

Two things come with it.

**The mechanism is the directory.** What predicts performance is *knowing who knows what* — the index — rather than the volume of what is held. Our diagram draws four content tiers and no index. On the human side, "shared tracking" is doing that work implicitly; on the AI side, nothing is. That is a gap in the picture, not just in the model.

**The measurement caveat is severe and immediately relevant.** Self-report measures of TMS give r = .77; observer ratings give r = .38; embedded behavioural metrics give r = .39. **Self-report roughly doubles the apparent effect.** The conference short-form is entirely self-report. That does not make it worthless — it makes it a measure of *perceived* externalisation, and the write-up must say so before a reviewer does.

### 2.6 Kanban and checklists: adoption is not the treatment

Kanban's core mechanism is queueing: limit work in progress and cycle time falls. Little's Law is a theorem, not a finding — it is true by construction, and citing it as evidence is a category error. The empirical Kanban literature is largely case studies.

The checklist literature is more useful precisely because it is *mixed*. Haynes et al. (2009) found large mortality reductions with the WHO surgical checklist; Urbach et al. (2014), studying mandated province-wide adoption in Ontario, found essentially nothing. The standard reading — that the checklist works when it changes team coordination and does nothing when it becomes paperwork — is exactly our thesis about protocols, already tested, in a high-stakes domain, at scale.

**This is the best available external validation of the programme's core intuition, and it should be at the front of the argument rather than absent from it.** It also dictates a study-design constraint: never measure whether someone *has* a protocol. Measure whether it changed what they did.

---

## 3. The AI side

The cascading memory model — four tiers, loaded by discipline pills into a session — has a literature that did not exist when the diagram was first drawn, and it is unusually favourable.

**More context is not better.** Chroma's 2025 evaluation across 18 models found performance degrading non-uniformly as input length grows, on tasks the models handle easily at short length. Liu et al. (TACL 2024) established the positional structure: retrieval is best at the beginning and end of the context, worst in the middle.

**Irrelevant material is actively costly, not merely inert.** Shi et al. (ICML 2023) showed that adding a single irrelevant sentence to an arithmetic problem substantially degrades accuracy. Chroma found that *plausible* distractors — topically related, wrong — hurt more than random noise, and that four compound worse than one.

**Focus beats volume, measured directly.** On LongMemEval, a focused input of ~300 tokens outperformed the full ~113k-token context containing the same answer.

Three consequences for the diagram, all of them corrections:

1. **"loading · automatic" must stop implying "free".** On the AI side, loading is priced in accuracy. An `ALWAYS` tier is not a convenience; it is a permanent tax on every session's reasoning, paid whether or not the item is relevant. That is the strongest empirical argument the diagram has for a *discipline* of loading rather than a discipline of storing, and the current label works against it.
2. **The pills are the mechanism, not the annotation.** `ALWAYS` / `AS-NEEDED` / `PER-PROJECT` is a just-in-time context policy. It is independently justified on the AI side by context rot and on the human side by GTD's context tags — whose entire function is likewise *not-loading*. This is the one element of the diagram supported by two unrelated literatures, and it is currently drawn as a label on a box.
3. **A stale `ALWAYS` item is the worst object in the system**, and now for two reasons rather than one: it is loaded unconditionally (our archive trap) *and* it is a plausible distractor (Shi; Chroma). The `cascade.py` finding that 118/256 standards were wrong even at 100% checking is a claim about the first. The literature supplies the second for free.

**Caveat on the Chroma work.** It is a vendor technical report from a company selling retrieval infrastructure, and therefore motivated to show that long context underperforms retrieval. It is not peer-reviewed. It is broad, transparent, and consistent with the peer-reviewed positional result — but flag it as industry evidence every time it is cited.

---

## 4. The gap: everybody has studied loading

Set the two literatures beside the diagram's three operations.

| operation | human evidence | AI evidence |
|---|---|---|
| **load** (store → session) | extensive — the whole offloading literature | extensive — context rot, position, distractors |
| **consult** (tracking → session) | moderate — TMS directory, checklists | partial — retrieval quality literature |
| **promote** (session → store) | **almost none** | **none** |

Every offloading experiment either hands the participant a store or permits writing into one, then measures what happens downstream. **The decision about what is worth keeping is never the treatment.** The nearest thing is the plan-making literature (§2.4), where committing the *form* of an intention produces the benefit — and that is an intention, not a codified generalisation, and the outcome is intrusive thoughts, not capability.

This is a better position than it looks. The Λ/Π split was adopted for internal reasons — to stop the model conflating relief with evidence. It turns out to be the seam along which the existing literature ends.

**So the contribution is exactly three claims:**

- **L5 — promotion is capability-building.** Deciding what from a session is worth keeping is effortful cognition that builds the thing offloading erodes. The generation effect, retrieval practice and self-explanation all make it plausible; none of them tests it. If L5 is false, the programme is a load-management proposition and not a judgment-preservation one.
- **L6 — process evidence requires residual capability to read.** A failing check informs only someone who knows what it means. This is what turns a cost model into a trap model, and nothing in the literature tests it.
- **L7 — it aggregates.** Ten-minute effects on logic puzzles, in students, with checkable answers, versus months of professional work on ill-specified problems with delayed or absent ground truth. Already named in the review as the distance the programme has to cover; the ledger confirms nobody else is covering it.

Everything else on the board is borrowed, and should be borrowed loudly.

---

## 5. What this changes now

**In the simulator.** Three families of behaviour can be fixed from literature rather than swept, which removes free parameters from a model that has too many:

- Loading helps the current task and degrades unaided capability. Do not sweep the sign; it is E2 + E3.
- AI-side loading is priced in accuracy, not effort. The current model treats loading as free on the AI side; A1/A3/A4 say it should carry an accuracy penalty rising with tier breadth. **This is a live model change and it strengthens the store term rather than weakening it** — worth checking whether it survives the `[0,1]` baseline that killed the 40.5% headline.
- Corroboration among wrong items is not an invented mechanic. A5 is its empirical cousin.

**In the study design.** The TMS measurement moderator (self-report r=.77 vs embedded r=.39) is the sharpest warning in this document for the Chile and Turtl waves. Self-report of externalisation practice will overstate the effect by roughly a factor of two. The three-item short form cannot fix that; the write-up can, by naming it.

**In the diagram.** Add an index/directory element (T2). Stop implying loading is free (A1). Promote the pills from label to mechanism (A1–A4). The demotion arrows added on 28 Aug were the right instinct — depreciation is the one exogenous process the literature agrees on across every field it appears in.

**In the argument.** Lead with checklists. Haynes-versus-Urbach is a large, high-stakes, real-world test of "the protocol works when it changes practice and does nothing when it becomes paperwork", and it is currently nowhere in our materials.

---

## 6. Sources

- Zhang & Norman (1994), *Representations in Distributed Cognitive Tasks*, Cognitive Science 18(1) — [wiley](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1801_3) · [pdf](https://pages.ucsd.edu/~scoulson/203/zhang.pdf)
- Risko & Gilbert (2016), *Cognitive Offloading*, Trends in Cognitive Sciences — [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S1364661316300985)
- Gilbert et al. (2025), *The benefits and potential costs of cognitive offloading for retrospective information*, Nature Reviews Psychology — [nature](https://www.nature.com/articles/s44159-025-00432-2)
- *Meta-analytic investigations of the effect of cognitive offloading on memory-based task performance and interindividual variability* (2025), Memory & Cognition — [springer](https://link.springer.com/article/10.3758/s13421-025-01743-8)
- Gilbert et al. (2020), *Optimal Use of Reminders: Metacognition, Effort, and Cognitive Offloading*, JEP:General — [pdf](https://samgilbert.net/pubs/Gilbert2020JEPG.pdf)
- Chiu & Gilbert (2024), *Influence of the physical effort of reminder-setting on strategic offloading of delayed intentions*, QJEP — [sage](https://journals.sagepub.com/doi/full/10.1177/17470218231199977)
- Masicampo & Baumeister (2011), *Consider It Done!*, JPSP — [pdf](https://users.wfu.edu/masicaej/MasicampoBaumeister2011JPSP.pdf)
- Gollwitzer & Sheeran (2006), *Implementation intentions and goal achievement: a meta-analysis* — [researchgate](https://www.researchgate.net/publication/37367696_Implementation_Intentions_and_Goal_Achievement_A_Meta-Analysis_of_Effects_and_Processes)
- Kalyuga (2009), *Expertise reversal effect and its instructional implications* — [springer](https://link.springer.com/article/10.1007/s11251-009-9102-0)
- Fausett et al. (2026), *Measurement Matters: A Meta-Analytic Examination of Transactive Memory Systems and Team Outcomes* — [sage](https://journals.sagepub.com/doi/abs/10.1177/10464964261434540)
- Ren & Argote (2011), *Transactive Memory Systems 1985–2010*, Academy of Management Annals — [aom](https://journals.aom.org/doi/10.5465/19416520.2011.590300)
- Urbach et al. (2014), *Introduction of Surgical Safety Checklists in Ontario, Canada*, NEJM — [nejm](https://www.nejm.org/doi/full/10.1056/NEJMsa1308261)
- Heylighen & Vidal (2008), *Getting Things Done: The Science behind Stress-Free Productivity* — [pdf](https://pespmc1.vub.ac.be/Papers/GTD-cognition.pdf)
- Liu et al. (2024), *Lost in the Middle: How Language Models Use Long Contexts*, TACL — [acl](https://aclanthology.org/2024.tacl-1.9/)
- Shi et al. (2023), *Large Language Models Can Be Easily Distracted by Irrelevant Context*, ICML — [arxiv](https://arxiv.org/abs/2302.00093)
- Chroma (2025), *Context Rot: How Increasing Input Tokens Impacts LLM Performance* — [trychroma](https://www.trychroma.com/research/context-rot) *(vendor technical report)*
- Lee et al. (2025), *The Impact of Generative AI on Critical Thinking*, CHI — [pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf)
- Dell'Acqua et al. (2025), *Navigating the Jagged Technological Frontier*, Organization Science — [informs](https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838)
- Parasuraman & Manzey (2010), *Complacency and Bias in Human Use of Automation*, Human Factors — [pubmed](https://pubmed.ncbi.nlm.nih.gov/21077562/)
- Aghajani et al. (2019), *Software Documentation Issues Unveiled*, ICSE — [acm](https://dl.acm.org/doi/10.1109/ICSE.2019.00122)

---

## 7. Appendix — what Heylighen & Vidal actually cite

Asked whether their primary sources give us something to build on. Short answer: **not as evidence, but one of them is a better formal frame than anything we have been using.**

### 7.1 The bibliography is a theory bibliography

Roughly 37 entries. Two do empirical work:

- **Miller (1956)**, the "magical number seven" — and this is the weakest brick in their argument. Cowan (2001) revised it to ~4, and the field has largely moved off fixed-slot accounts to interference and resource models. **Anything of ours that inherits "seven items" inherits a problem.**
- **Czerwinski, Horvitz & Wilhite (2004)**, a diary study of task switching and interruption.

Everything else is theory (Clark & Chalmers, Hutchins, Hollan/Hutchins/Kirsh, Gibson, Suchman, Clancey, Bickhard), formal/complexity work (Simon, Powers, Bonabeau, Grassé, Parunak, Susi & Ziemke), or management writing (Allen, Covey, Drucker) — plus a Wikipedia article.

**So: do not treat H&V's citations as an evidence base.** The paper is a theoretical reconstruction that says "here is a coherent cognitive-science story that would explain why GTD works if it does". That is a legitimate genre and it is not evidence.

### 7.2 The find: stigmergy

The most valuable entry is the lineage Grassé (1959) → Parunak (2006) → Heylighen's own later, much more developed *Stigmergy as a Universal Coordination Mechanism* (two-part paper; published version in **Cognitive Systems Research 38–39, 2016** — verify the volume before citing).

**Stigmergy:** *the trace of an action left on a medium stimulates the performance of a subsequent action.* That is the promotion → loading cycle, stated as a coordination primitive, thirty years of formal development behind it.

Four things it gives us that we do not currently have.

**(i) A principled criterion for the Human/AI boundary.** Heylighen's medium must be **both perceivable and controllable** — a beach is a stigmergic medium, the ocean is not. Apply it to the diagram and the boundary question Robert raised resolves itself: the store is a medium; project outcomes in the world are perceivable but not controllable, so they are *feedback*, not trace. That is a sharper cut than "which side of the line does this externalisation sit on", and it is not ours to invent.

**(ii) Our drift rate is an evaporation rate, and it already has a normative theory.** Heylighen argues decay is *not a priori negative*: traces are instructions, so outdated instructions mislead, and the **optimal decay rate depends on the speed at which the information becomes obsolete** — fast for ant food sources, slow for termite pillar locations.

This is a direct hit on `cascade.py`. Our `leverage = load_share / drift_rate` was reinventing it, and the tier structure stops being a design choice: **the tiers are a decay-rate-matched hierarchy, and that is why there are four of them rather than three or nine.** It also converts `drift` from an invented parameter into a principled one, which is exactly what the ledger was for.

**(iii) Its classification dimensions map onto distinctions we have been fudging.**

| Heylighen's dimension | our diagram |
|---|---|
| sematectonic vs marker-based | the work itself vs a note *about* the work — the thing we have never separated in the store |
| quantitative vs qualitative | strength-of-trace vs kind-of-trace |
| transient vs persistent | session vs store; **asynchronous stigmergy is precisely what a store is for** |
| broadcast vs narrowcast | shared vs individual context — already drawn, now named |
| individual vs collective | the same mechanism serves one agent coordinating with its later self; **no team is required for the model to bite** |

That last row matters for the venture: it says the individual case is not a degenerate version of the team case, it is the same mechanism.

**(iv) It exposes what is genuinely new on the AI side.** Classical stigmergy assumes traces are **non-rival** — Heylighen: an ant following a pheromone trace does not make it less useful to other ants, which is why free-riding does not undermine the commons.

**That assumption fails for an LLM context window.** Loading a trace consumes attention that the other traces need; context rot, distractor effects and the LongMemEval focused-vs-full result all say the same thing. So:

> **AI-side stigmergy is rival in attention. Classical stigmergy is not.**

I cannot find anyone who has said this. It is a real structural claim, it follows from putting two established literatures side by side, and it is the formal reason the loading *discipline* — the pills — is load-bearing rather than tidy. Worth a paper on its own.

### 7.3 One empirical anchor reachable from their bibliography

H&V cite Kirsh (1996, 2000) but not the empirical work behind it. **Kirsh & Maglio (1994)**, *On Distinguishing Epistemic from Pragmatic Action*: Tetris players rotate pieces physically at ~100 ms per 90°, against 800–1200 ms to rotate the same shape mentally — an **8–12× advantage** — and rotate more often than placement requires, with experts calibrating the epistemic check by cost-benefit.

Epistemic action: *a physical action taken to make mental computation easier, faster or more reliable.* Paired with Zhang & Norman, this is the second half of the strong claim — externalisation is not a workaround for a weak memory, it is a **cheaper computation**. Add it to §2.1.

### 7.4 One tension worth keeping

**Suchman (1990), *Plans and Situated Action*, cuts against GTD** and H&V do not notice. Suchman's argument is that plans are *resources for* action, not controllers *of* it. Our promotion claim should inherit that: what you promote is a resource that makes future situated action cheaper, not a script that future sessions execute. The archive trap is what happens when a store is treated as the second thing.

### 7.5 Sources added

- Heylighen, *Stigmergy as a Universal Coordination Mechanism* — [pdf](https://pespmc1.vub.ac.be/Papers/Stigmergy-Springer.pdf)
- Kirsh & Maglio (1994), *On Distinguishing Epistemic from Pragmatic Action*, Cognitive Science 18 — [pdf](https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf)
- Cowan (2001), *The magical number 4 in short-term memory* — [pdf](https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf)
- Grassé (1959), *La théorie de la Stigmergie*, Insectes Sociaux 6
- Parunak (2006), *A survey of environments and mechanisms for human-human stigmergy*
- Suchman (1990), *Plans and Situated Action*, CUP

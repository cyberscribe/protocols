---
title: "Externalisation as maintained correspondence"
subtitle: "Revised proposal — stigmergic architecture, two decay processes, and the operation nobody has studied"
supersedes: external-protocols.txt
see_also: external-protocols-model.md, externalisation-evidence-ledger.md, ../../peakepro-diagnostics/cognition-assessment/settled-questions.md
date: 2026-08-28
status: proposal
---

# Externalisation as maintained correspondence

**Thesis in one line.** *Loading is stigmergic; promotion is the only operation that maintains the
internal copy as a by-product of maintaining the external one.*

---

## 0. What changed

Three findings this week change the proposal rather than decorating it.

1. **The literature has only ever studied loading.** Every offloading experiment hands the participant
   a store or lets them write into one freely, then measures downstream. **The decision about what is
   worth keeping is never the treatment.** The loading/promotion split was adopted for internal reasons;
   it turns out to be the seam where the evidence base ends.
2. **Stigmergy is the right formal frame**, and it is not ours to invent — Grassé (1959) through
   Heylighen. It supplies a medium criterion, a decay theory, and a classification of trace types that
   maps onto distinctions we had been fudging.
3. **The two decay processes are of different type**, which is the load-bearing observation and the one
   that reorganises everything below.

---

## 1. The asymmetry

Knowledge in a head decays on its own. A written trace does not.

| | internal copy | external copy |
|---|---|---|
| decay of the **artefact** | autonomous — proceeds with time whether or not the world changes | **none**, for a digital medium |
| what actually fails | availability | **correspondence** — the trace is intact, the world moved |
| trigger | none; it is a property of the holder | exogenous, and in principle **detectable** |
| repair | rehearsal — recurring, expensive, does not scale | **one write**, which then holds indefinitely |

Hence the claim the whole proposal now rests on:

> **Externalisation converts an autonomous decay process into an exogenous one.**

That is not "storage with better retention". It is a change in the *type* of the problem. Autonomous
decay is unaddressable — there is no signal to act on and no schedule to keep; you can only rehearse.
Exogenous decay is addressable: the world changing is an event, events can be watched for, gated on and
scheduled against. **Everything a protocol can do, it can do only to the second kind.**

Heylighen supplies the normative half and we should take it: trace decay is *not a priori bad*, because
traces are instructions and stale instructions mislead. The optimal decay rate tracks the speed at
which the information goes obsolete. That is why the store has tiers, and why there are four of them —
**the tier hierarchy is decay-rate-matched, not a design preference.**

### 1.1 The same asymmetry explains cognitive debt

Run it the other way. Externalise, and the external copy keeps serving. The internal copy decays
underneath it, autonomously, and **nothing signals it**, because no task fails. The store answers; the
head empties; the error surfaces only when access is lost or when a judgment is required that the store
cannot make.

That is why debt is *counterfactual* — invisible by construction — and why it is measurable only by
withdrawal. It is not a moral failure or a laziness story. It is the arithmetic of two decay processes
where only one of them is instrumented.

**So the same asymmetry gives both halves of the thesis.** Externalisation is unambiguously good for
correspondence and it is the cause of debt. Any proposal that claims only one half is wrong.

---

## 2. The resolution: promotion is the only two-sided operation

Three operations, from the diagram:

| operation | direction | touches the external copy | touches the internal copy |
|---|---|---|---|
| **load** | store → session | reads it | **no** — no rehearsal, this is the free ride |
| **consult** | tracking → session | — | partially |
| **promote** | session → store | **writes it** | **yes** — reading, judging and re-encoding *is* rehearsal |

Promotion is the only operation that maintains both copies, and it does so **without a separate
practice discipline**, because the rehearsal is a by-product of the maintenance you were doing anyway.

Two consequences worth stating plainly:

- **This is why the discipline matters more than the tooling.** Tooling can automate loading, and should.
  Automating promotion removes precisely the part that pays.
- **It gives the programme a positive claim rather than a defensive one.** Not "protect yourself from
  the AI" but "here is the maintenance discipline a distributed cognitive system requires, and it
  happens to be the thing that keeps you sharp." Same mechanism, better story, and truer to the model.

---

## 3. The architecture, in Heylighen's terms

**Stigmergy:** the trace of an action left on a medium stimulates a subsequent action. That is
promotion → loading, stated as a coordination primitive with formal development behind it.

- **Medium = perceivable *and* controllable.** A beach is a medium; the ocean is not. This settles the
  boundary question: the store is a medium; project outcomes in the world are perceivable but not
  controllable, so they are **feedback, not trace**. Stop trying to draw them as the same kind of thing.
- **Asynchronous stigmergy** — persistent traces let agents coordinate without co-presence. That is
  precisely and only what a store is for.
- **Sematectonic vs marker-based** — the work itself vs a note *about* the work. We have never separated
  these in the store and they behave differently under drift.
- **Individual vs collective is the same mechanism.** A solitary wasp coordinating with its own later
  self is stigmergic. **The individual product and the team product are one model, not two.**

### 3.1 Where the classical theory breaks, and that is ours

Classical stigmergy assumes traces are **non-rival**: an ant following a pheromone trail does not make
it less useful to other ants, which is why free-riding does not undermine the commons.

**That fails for a context window.** Loading a trace consumes attention the other traces need — context
rot, distractor effects, and a focused ~300-token input beating the full ~113k context containing the
same answer.

> **AI-side stigmergy is rival in attention. Classical stigmergy is not.**

This is the formal reason a loading *discipline* is load-bearing rather than tidy, and I can find no one
who has stated it. It is also the shortest path to a publishable result we have.

---

## 4. What we are actually claiming

Fourteen claims are settled and should be borrowed loudly — see
`settled-questions.md` for the assume-and-cite register. The contribution is four things:

- **O1 — Promotion is capability-building.** Deciding what is worth keeping is effortful cognition that
  rehearses the internal copy. Plausible from the generation effect, retrieval practice and
  self-explanation; tested by none of them.
- **O2 — Process evidence needs residual capability to read.** A failing check informs only someone who
  knows what it means. This is what turns a cost model into a trap model.
- **O3 — It aggregates.** From ten-minute effects on logic puzzles to months of professional work with
  delayed or absent ground truth.
- **O4 — AI-side stigmergy is rival in attention.** §3.1.

Everything else is borrowed.

---

## 5. The experiment nobody has run

**Make promotion the treatment and hold the external artefact constant.** That is the whole design, and
the fact that it has not been run is §0.1.

| arm | store | who built it |
|---|---|---|
| **A — load only** | yes | someone else (a matched participant from B) |
| **B — promote** | yes | themselves, during the work |
| **C — control** | none | — |

- **Time-on-task matched** across arms. B spends part of its budget promoting; A gets the same total time
  with more of it on the task. This is the honest comparison and it makes the test harder for us.
- **External quality verified equal** between A and B by the adjudicator we already built — a fit +
  correctness judgment on the artefact, not an inspection of the practice. If A's store is worse than
  B's, the design is broken and we know before analysing.
- **Aided performance:** predict **A ≈ B** — no difference, or A slightly ahead on time.
- **Unaided probe, delayed:** predict **B > A**. That is O1, and it is the only place the arms differ.
- **A world-drift manipulation crossed with the above** tests §1 directly: in a *frozen* world the store
  should show no correspondence loss at all while internal loss proceeds normally; in a *drifting* world
  both degrade, by different mechanisms with different repair costs.

Why this is the right study: it isolates the internal effect by holding the external one constant,
it is preregisterable, it fails cleanly, and it is Prolific-scale rather than field-scale. The probe
contaminates — a delayed unaided probe *is* a dose of unaided practice — so single-probe, between-subjects.

---

## 6. Consequences for the simulation

The current model conflates the two decay processes into one drift rate. Split them:

- **`δ_K` autonomous** — proceeds on the clock, modulated only by rehearsal, and rehearsal arrives only
  through promotion.
- **`δ_X` exogenous** — fires on world-change events, repairable by one write, tier-matched.

This is not a parameter change, it is a structural one, and it should change results: under a frozen
world the store term should go to zero loss while capability still erodes, which the present model
cannot express. **Check whether the σ_A crossover survives the split.** Also: AI-side loading now carries
an accuracy cost rising with tier breadth and must stop being modelled as free.

The register at `settled-questions.md` §4 records the three behaviours that are now fixed from
literature and must not be swept as free parameters.

---

## 7. Where we go, in order

| # | Move | Effort | Why now |
|---|---|---|---|
| 1 | Rewrite the formal model to the three-state stigmergic form with the decay split | hours | Everything below depends on it; v3 is bigger than it needs to be and says less |
| 2 | Rebuild `cascade.py` on `δ_K` / `δ_X` and re-run the headlines | hours | The frozen-world case is a free falsifier we cannot currently express |
| 3 | Write **O4** as a standalone short paper | 1–2 days | Fastest publishable thing we have; two established literatures, one unstated consequence |
| 4 | Design + preregister the **promotion RCT** (§5) | days | It is the gap. Costed at Prolific scale before committing |
| 5 | Chile (5 Sep) and Turtl (28 Sep) ship as specced | — | Dated. Do not disturb — but bake in the self-report caveat |

Chile and Turtl remain self-report and will overstate by roughly 2× (TMS meta-analytic self-report
r=.77 vs embedded r=.39). That is survivable if named in the write-up, and fatal if discovered by a
reviewer.

---

## 8. What would kill this

**O1.** If promotion does not build capability — if the rehearsal in deciding-what-to-keep is too thin to
move an unaided probe — then the store still helps, the discipline still helps correspondence, and the
programme is a **load-management proposition rather than a judgment-preservation one.** That is a
smaller, still-viable product and a much weaker paper. §5 is designed to find that out cheaply and
early, which is the right order.

Two smaller risks, both manageable: the §1 asymmetry may already be stated somewhere in the
organisational-forgetting literature under different vocabulary (**check before claiming priority**);
and O3 remains an aggregation argument that no single study can close.

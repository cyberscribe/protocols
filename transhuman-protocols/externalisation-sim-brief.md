---
title: "The externalisation sim — what it is, and what it would show"
see_also: external-protocols-model.md, visualisation-design-principles.md, diagrams/exec-fn-ai-org_2026-08-26.svg
date: 2026-08-28
status: draft — decisions open
---

# The externalisation sim

Three parts: what the diagram actually claims, the sim in plain language, and the decisions still open with a recommendation on each.

---

## Part 1 — Re-reading the diagram

### What it is a picture of

`exec-fn-ai-org` is a picture of **one cognitive system with a seam down the middle**. Not two systems co-operating — one system whose parts happen to sit on either side of a boundary. That is the distributed-cognition claim proper: the unit of analysis is the whole assembly, and the assembly's properties are not the person's properties.

Three things in the drawing carry that claim, and one of them I under-read the first time.

**1. The colour overlay is the load-bearing element.** Six content types, each appearing in two places, same colour both times: *the same thing held twice, to be kept in sync.* That is not an annotation about tidiness. **A cognitive system is distributed exactly when a representation lives in more than one place and something maintains the correspondence.** So externalisation is not "writing things down" — it is *maintaining a correspondence across a boundary*, and the interesting question is always what happens when the maintenance lapses.

**2. The two arrows are the maintenance, and they are asymmetric by construction.** Loading is short, grey, automatic, and runs store → session. Promotion is drawn the long way round, in ink, human-involved, and runs session → store. One half of the coupling is free and machine-side; the other is expensive and can only be done by the person. That asymmetry is not a stylistic choice about arrow length — it is the whole mechanism, and it is why the system can hold its correspondence in one direction indefinitely while losing it in the other.

**3. The discipline pills say which half of the correspondence is guaranteed.** `ALWAYS` on working standards means that store is in every session's evidence base whether or not anyone has looked at it lately. The most-loaded store is the least-reviewed.

### What the diagram does not show — and this is the point

**There is no person in it.** The human side shows *apparatus* — shared context, individual context, three levels of tracking — and no cognizer. There is no box for what the person can still do, how loaded they are, or how much they believe the machine. The diagram draws the scaffolding of a distributed cognitive system and leaves the state of its human component entirely implicit.

That is why the sim is a complement rather than a second view of the same thing, and it is worth saying out loud to any room shown both, because a room shown both will assume they are two pictures of one object.

The honest joint claim across the pair is uncomfortable and correct: **the system in the diagram can be performing excellently while the person in it degrades.** That is `T^\* - P = (1-\alpha)(O - P)` in words — outcomes stay good, the basis for judging them does not.

Also absent, and now flagged rather than fixed: no demotion or expiry (addressed by running the cascade backwards); no representation of the sync *lapsing*, only of it existing; and the stacked loops show concurrency, which the model does not yet have.

---

## Part 2 — The sim, for someone who has not read any of the above

### The setup

Picture a workbench with a seam down the middle. On the machine's side are four filing cabinets. Every time work starts, the relevant contents of those cabinets are pulled into the job automatically, for free, without anyone deciding anything. On the person's side there is the person.

Once in a while — and only the person can do this — they stop, work out what actually mattered about the job just finished, and write it back into a cabinet. Not a transcript, not a summary: the criteria they used, the assumptions they made, why they decided what they decided, what they checked, what would make them change their mind.

Pulling out is free and constant. Writing back costs something and is optional. That is the entire mechanism.

### The question

Run that for months. **What happens to the person?**

Not to the output. The output is fine — that is what makes this hard.

### What gets watched

Each period, three yes/no readings:

| reading | plain question |
|---|---|
| **Writing back** | did they put anything judgment-bearing into a cabinet this period? |
| **Reasoning** | did they work any of it out themselves before asking? |
| **Calibrated** | does their confidence in the machine match what the evidence actually warrants? |

Three yes/no readings make eight combinations. That is the picture: **eight cells, with the ones the person actually visits lit up and the ones they never reach left empty.**

### What the picture would be claiming

That **you cannot stay calibrated while neither reasoning nor writing back.**

If that cell is empty, then good judgment about the machine is not a character trait and not a matter of being careful. It is a *by-product* of doing one of two specific things — and if you stop doing both, it goes, whether or not you notice it going. It also cannot be restored by resolving to be more careful, because carefulness is not one of the two things.

### The nasty part, which the picture should show as a movement

Better filing cabinets *free up time*. So a person with a good context store writes back **more** while reasoning **less** — the cabinets did the reasoning.

On the reading a manager would take — *are they keeping the documentation current?* — they look better than before. On the reading that matters, they are going the other way. The two readings move in opposite directions and only one of them is visible.

That is the sentence the whole programme is trying to land: **the harm is detected by the faculty the harm erodes.**

### How you would know it was wrong

If all eight cells get visited, there is no structural claim here and the story is only about degree. That result gets published too. The cells are not chosen so that one comes out empty — they are chosen because they are the three things the model says are happening, and then we look.

### Does it visualise the diagram?

Reasonably, and here is the honest fit:

| the diagram shows | the sim represents it as |
|---|---|
| loading — short, grey, automatic | free, every period, no decision |
| promotion — long, in ink, human-involved | the only choice in the model |
| the four stores | a stock that grows when written to and decays when not |
| "same thing held twice, kept in sync" | the correspondence being maintained, or not |
| the person | *everything the diagram leaves out* |

**Where it does not fit, and these are decisions, not oversights:** the diagram has four stores with different loading disciplines and the sim has one; the diagram shows several loops running at once and the sim runs one stream; the diagram's `ALWAYS` store has no review and the sim needs a way to represent a *wrong* store, not merely an empty one.

---

## Part 3 — Decisions still open, with a recommendation on each

### 3.1 Which engine this is

**Recommend: a new engine at `sim/externalisation/`, and archive `core/model-v2`, `core/model-v4` and `core/mvm2` in the same commit.**

`trust-trap/model.mjs` is canonical, digest-pinned, and the posture machine reads it unmodified behind 39 conformance checks — forking it in place breaks all of that. But a seventh engine arriving with nothing leaving is how the currency boundary in `00-CURRENT.md` stops meaning anything. Those three are already superseded in practice; retiring them keeps the count flat and makes the new one legible as *the* successor rather than another parallel attempt.

Declare explicitly: **the new engine reads the posture machine's *reading layer* and not trust-trap's state vector.** Reuse the quantiser, the deadband calibration, the ring, the conformance harness, the palette and the standalone build. Do not reuse the states.

### 3.2 Is the trust-trap loop integrated, or only related?

**Recommend: related, not integrated — and the reason matters more than the answer.**

The state vectors look close enough to merge and are not. Trust-trap's `S` (sovereignty) is *not* reasoning `R`; its `D` (debt) is *not* the complement of capability `K`. They are cousins, and conflating them would repeat an error already recorded in `sim_oscillator_conditions`: if sovereignty is driven by trust alone the plane collapses onto its anti-diagonal, `corr(T,S) = −1.00`, and two quadrants become unreachable.

**That warning applies directly to the new model, and it is the sharpest structural catch available here.** Promotion effort `H` and reasoning `R` are both written as decreasing in trust and load and increasing in observability. If that is all they have, they collapse against each other and the eight cells become four.

They need drivers the other lacks, and both are already to hand:
- **`R` gets `Λ`** — loading displaces reasoning and does not displace writing-back.
- **`H` gets `ρ`** — capacity/discipline, which is already sitting in the `θ_ρ ρ` term. `R` must *not* have it.

That asymmetry is not a modelling convenience. `sim_oscillator_conditions` already names discipline as "the only driver that is not a response to circumstance: trust answers results, capacity answers exhaustion, discipline answers nothing. **That is the term the venture teaches.**" So the term the business sells is exactly the term that keeps the state space from collapsing. Take that as confirmation, not as a coincidence to lean on.

### 3.3 Functional forms

**Recommend: inherit the tree's house forms wholesale. No new mathematics.**

| quantity | form | precedent |
|---|---|---|
| stocks — `K`, `X`, `L` | linear tracking with a restoring force, `x' = x + rate·(target − x)` | every engine in the tree |
| accumulation toward a ceiling | `x + η·f·(1 − x)` | DRIVE investment channels |
| evidence weight | noisy-OR | trust-trap `q = 1 − (1 − S(1−D))(1 − a_Q)` |
| outcome | bilinear, then capped | trust-trap `output = min(cap, B + h·H)` |
| the two behavioural readouts `H`, `R` | logistic only here | DRIVE's softmax family; `σ(·)` is already in the `H` equation |

One page, every choice carrying its citation from the existing tree. Sigmoids stay confined to the two places a bounded behavioural response is actually being modelled.

### 3.4 Parameter defaults

**Recommend: anchor the shared parameters to trust-trap's measured values; calibrate the new ones to target behaviour and report the surviving range.**

Shared and inherited: `τ = 28`, `η = 0.18`, debt/decay rates `0.02`, stock formation `0.10`. Those were what produced the cycle, and a successor model that cannot reproduce the cycle is not a successor.

New (`γ`, the `θ`s, the `β`s): set so the baseline run reproduces the six-state ring, then **sweep and report the range over which the occupancy result survives** — the figure's payload has to clear the 30%-variation bar from `visualisation-design-principles.md` §2, and if it does not, this is an instrument and not an exhibit. Same discipline as "never hand-pick a seed": declare the sign the result turns on, measure what fraction of the space reproduces it, report both numbers on the frame.

### 3.5 Bit thresholds — self or frozen

**Recommend: frozen, calibrated against the no-promotion baseline. This one is not close.**

Self-calibration reads each bit against its own run's median, so a person who never writes anything back still shows roughly half their periods as "writing back" — which destroys precisely the comparison the figure exists to make. `posture-machine/MODEL.md` already records a mechanism ranking that reverses sign between the two modes, with the affordability claim surviving in only one. Frozen against a declared baseline is the only mode in which arms are comparable.

### 3.6 Store granularity — one stock or four

**Recommend: one stock, but two-dimensional: `X = (mass, validity)`.**

The four stores differ by *loading discipline* — when they are pulled in — and the harm mechanism is about *validity*, not about which cabinet. Four stores multiply the state space without changing the topology claim.

But validity has to be there, because store-side debt is the genuinely novel finding: an `ALWAYS`-loaded standard that has quietly stopped being true is loaded into every session forever with no evidence attached and no review. Mass alone cannot represent a wrong store, only an empty one.

### 3.7 Concurrency

**Recommend: out of scope for v1, said loudly and in the file.**

The four-up's thesis was concurrency and it did not land. `sim_oscillator_conditions` already records why: *"every earlier attempt to show the trap loop failed because the model was carrying aids, slots, concurrency and temperament at the same time. Isolating the oscillator first is what worked."* Adding concurrency to a model that has not yet produced its structural result repeats the mistake with better notation.

### 3.8 Register

**Recommend: build the instrument. Do not build the figure. Decide on the exhibit afterwards.**

The four-up was a figure, and figures are where this line of work fails. Build the sliders-reach-the-failures instrument, run occupancy headless, and only then ask whether an exhibit exists. **If no cell is empty there is no exhibit, and that is a result rather than a setback.**

### 3.9 Effectiveness — product or sum

**Recommend: settle it as sum, in the ledger, this week — and build the figure so it does not depend on the answer.**

`00-CURRENT.md`'s argument is correct: the product form has a pole at `debt → 0` floored only by `D_base`, making one term a sixfold lever. Settling it is one edit to `theory-canonical.md` and it retroactively repairs the four-up. But a topological figure does not read a composite score at all, which is the better reason not to be blocked on it.

### 3.10 "Game theory"

**Recommend: not in this sim — and write it separately, because it is real.**

There is no game in the tree: `game-mechanics.md` is a race between non-interacting single agents, and the search for a fixed-policy optimum was closed on 2026-08-25 for a sound reason (*"a fixed-policy optimum is a fixed-point question, and the subject matter is a limit cycle"*). Making the agent an optimiser would reintroduce exactly that framing.

But `theory-under-simulation.md` §6 names the genuine formal parent — **costly state verification (Townsend 1979)** — with a stated novelty that nobody has written up: *in the standard formalism the verification technology is fixed; here, choosing not to verify degrades your ability to verify.* That is a paper. It is a different paper.

---

## Part 4 — Notation

`Π`/`π` is retired. It reads as the constant, as the product operator, and in economics as profit or a policy, and it was doing all three jobs at once.

**Rule adopted: single letters for states, whole words for functions.** The model is going to be code, and code is where the words belong anyway.

| was | now | why |
|---|---|---|
| `Π_t` promotion | **`W_t`** | what you *write back* |
| `π(·)` | `promote(·)` | |
| `λ(·)`, `p(·)`, `o(·)`, `ℓ(·)`, `r(·)`, `g(·)`, `m(·)` | `load(·)`, `evidence(·)`, `outcome(·)`, `burden(·)`, `reason(·)`, `grow(·)`, `probe(·)` | |
| `C_t` the store | **`X_t`** | matches trust-trap's externalisation stock — same object, and the alignment is free |
| bits `π/ρ/α` | **`W` / `R` / `C`** | writing-back · reasoning · calibrated. Mnemonic, no Greek, no collision with the allocation parameter `α` |

`Λ` stays — it is not a reserved symbol and it reads as an input.

⚠️ Two live collisions with trust-trap to declare in the header of the new engine, since both files will be open at once: its `H` is *human contribution* where ours is *promotion effort*, and its `R` is *reclaim* where ours is *reasoning*.

---

## Part 5 — Order of work

1. Settle 3.1 and 3.10 — decisions, not work.
2. Write forms and defaults into `external-protocols-model.md` as an `## Implementation` section, every choice citing its precedent.
3. Build headless. Run occupancy and the habitability test **before drawing anything.**
4. Only then specify the view, clause by clause against `VIEW-DECISIONS.md`.

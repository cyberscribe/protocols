---
title: "SPEC — four-buckets sim and visualiser"
date: 2026-08-28
status: ready-to-build
for: Claude Code
supersedes: diagrams/four-buckets_2026-08-28.html (prototype; keep for reference, do not extend)
see_also: NOTE-discipline-and-referencing.md, NOTE-poison-neutralisation-literature.md,
          ../../peakepro-diagnostics/cognition-assessment/settled-questions.md
---

# SPEC — four-buckets sim and visualiser

Build a **headless simulation first**, then a visualiser on top of it. The visualiser imports the
model; it must not reimplement any rule. The browser prototype at
`diagrams/four-buckets_2026-08-28.html` is a sketch that shipped three inert parameters before the
faults were found — **read §6 before writing a line of model code**, because those faults are the
acceptance tests.

---

## 1. Where it goes

```
peakepro-diagnostics/cognition-assessment/sim/buckets/
  model.py          the model. No I/O, no plotting, no globals.
  run.py            CLI: single run, batch, sweep. Writes CSV/JSON to out/.
  gates.py          the acceptance gates in §6, runnable as a suite.
  viz/index.html    the visualiser (§7). Loads out/grid.json; no model logic.
  out/              generated. Gitignored.
  README.md         findings, with the provenance table from §8.
```

Python for the model (matches `sim/correspondence/`), plain HTML+JS for the visualiser.

## 2. State

Four buckets. Every quantity is a count of items; poisoned items are tracked as a sub-count so that
a share is always derivable and never stored independently.

| symbol | bucket | behaviour |
|---|---|---|
| `Wh` | human working memory | **decays** every session |
| `Dh` | human durable | written by the human; does not decay |
| `Wa`, `Wa_p` | AI working memory | **replaced** every session |
| `Da`, `Da_p` | AI durable | promoted into; subject to clearance and curation |

`Wh` has no poison term. Poison is an AI-side phenomenon in this model; if that turns out to be
wrong it is a separate spec, not an addition here.

## 3. Parameters

Robert's five, plus two the literature audit requires and one his intractability point requires.

| name | range | meaning |
|---|---|---|
| `decay` | 0–0.5 | human working-memory loss per session |
| `poison` | 0–0.4 | probability that each new AI item is wrong at birth |
| `disc_h` | 0–1 | human discernment at promotion |
| `disc_a` | 0–1 | AI discernment at promotion |
| `discipline` | 0–1 | **decoupling of the ritual from felt need** |
| `rho` | 0–1 | **correlation between the two discernment gates** |
| `clearance` | 0–0.1 | per-session probability a poisoned durable item is corrected |
| `curation` | 0–0.1 | per-session share of durable items pruned |

Structural constants, exposed in config but not user-facing: `CAP_W=40`, `NEW=4`, `PROMO=3`,
`REF_MAX=12`, `LAG=0.12`, `BLIND=0.35`, `D_STAR=120`, `KAPPA=1.5`, `FIT_EXP=0.8`, `POISON_EXP=1.6`.

## 4. The cycle

One session, in order. Deterministic given a seed.

```
0  FEEL       need    = (1 - Wh/CAP_W) * (BLIND + (1-BLIND)*Wh/CAP_W)     # under-read when depleted
              felt   += LAG * (need - felt)
              ritual  = (1 - discipline)*felt + discipline

1  REFERENCE  Wh += min(Dh, REF_MAX) * ritual * tract(Dh)
              Wa, Wa_p := reload from Da (capped CAP_W - NEW), carrying Da's poison share

2  WORK       Wh += NEW
              Wa += NEW;  each new AI item is poisoned with probability `poison`

3  PROMOTE    catch = 1 - (1-disc_h)*(1-disc_a)**(1-rho)                  # see §5
              catch *= tract(Da)
              draw PROMO items from Wa at its own poison share; a bad one survives iff not caught
              Da grows below CAP_D, otherwise REPLACES at average composition

4  EXTERNALISE  Dh += Wh * EXT_MAX * ritual

5  MAINTAIN   clearance: each poisoned durable item corrected with prob `clearance`,
                         floored at RESIDUAL=0.15 of the current poisoned count (see §8)
              curation:  prune `curation` share of Dh and Da; if disc_h is high, prune
                         preferentially from poisoned/stale, else uniformly at random

6  DECAY      Wh *= (1 - decay)

   SCORE      fit         = (Wh/CAP_W) ** FIT_EXP
              correctness = (1 - Da_p/Da) ** POISON_EXP
              output      = fit * correctness
```

**Tractability** — Robert's point, and the one genuinely new mechanic:

```
tract(D) = 1 / (1 + (D / D_STAR) ** KAPPA)
```

Durable memory is nominally unbounded and practically intractable. A store past `D_STAR` costs
you: referencing yields less from it and discernment at the gate falls, because finding the
relevant item and spotting the bad one both get harder as the pile grows. **This is the term that
makes curation matter and gives store size an interior optimum.** It is the same object as context
rot on the AI side and the transactive-memory directory problem on the human side — cite both.

## 5. Two corrections the literature requires

Both make the model *less* favourable. Implement them; do not make them optional.

**Gate correlation.** `1-(1-h)(1-a)` assumes the two reviewers fail independently. They do not: the
human reads what the AI produced, so a plausible-but-wrong item is plausible to both. Use
`catch = 1 - (1-disc_h)*(1-disc_a)**(1-rho)`; at `rho=1` the second gate buys nothing. **Report the
rho at which "two gates beat one better gate" stops holding** — that is a headline, not a footnote.

**Partial clearance.** Poison is not an irreversible ratchet. Continued-influence meta-analysis
(32 studies, n=6,527) finds residual influence after correction is real but small. Clearance removes
poisoned items but never below a residual floor.

## 6. Acceptance gates — run these before reporting anything

`gates.py` must implement all of these and exit non-zero on failure.

**G1 · Sensitivity.** For each of the eight parameters, sweep its full range at 3 settings of every
other parameter, 20 seeds. **Every parameter must move at least one of {fit, correctness, output}
by ≥ 10 percentage points somewhere in the space.** A parameter that cannot move any outcome is a
bug, not a finding. *This gate exists because the prototype shipped `discipline` with a 4-point
spread and it went unnoticed.*

**G2 · No structural pinning.** Assert `Wh` is not equal to `CAP_W*(1-decay)` across ≥3 discipline
settings. *The prototype pinned there because inflow exceeded capacity and the cap silently did all
the work.*

**G3 · Fixed points, not ratchets.** With `clearance=0`, `curation=0`, poison share in `Da` must
converge to an interior value that depends on `poison` and `catch` — not to 1.0. Report the measured
fixed point against the analytic prediction. *The prototype ratcheted to 100% regardless of rate
because the store grew instead of replacing at capacity.*

**G4 · Corners behave.** Best corner ≥ 95% output; worst corner ≤ 35%; each single-axis corner
(decay only, poison only) degrades only its own half of the score and leaves the other ≥ 95%.

**G5 · Determinism.** Same seed and config → byte-identical output. Two seeds → different output.

**G6 · Tractability has an optimum.** Sweep `curation` at fixed everything else: output must be
non-monotonic, with a maximum at some `curation > 0`. If it is monotonic the tractability term is
not doing anything and `D_STAR`/`KAPPA` need re-siting. **This is the result Robert is asking for —
that an unbounded store is worse than a curated one — and G6 is the test of whether the model can
express it at all.**

**Report all six.** A gate that fails is the finding; do not tune until it passes and then report
only the pass.

## 7. The visualiser

**Mirror `diagrams/exec-fn-ai-org_2026-08-28-promotion.svg`.** Same composition, so the two read as
one family: human column left, AI column right, dashed divider between them that **stops where the
session begins**, session straddling the boundary at the bottom.

Collapse the taxonomy: **one durable bucket per side.** No content types, no tiers, no discipline
pills — that lives in `trace-space` and does not belong here.

```
   HUMAN                    ┊                    AI
   ┌───────────────┐        ┊        ┌───────────────┐
   │ working memory│        ┊        │ working memory│
   │   decays  ↘   │        ┊        │  overwritten  │
   └───────────────┘        ┊        └───────────────┘
        ↑ reference    ↓ externalise      ↑ load   ↓ promote
   ┌───────────────┐        ┊        ┌───────────────┐
   │    durable    │        ┊        │    durable    │
   │  tractability │        ┊        │ tractability  │
   └───────────────┘   ┌────┴────┐   └───────────────┘
                       │ session │
                       └─────────┘
```

Requirements:

- **Buckets show fill and composition** — poisoned fraction as a hatched band, not a second colour
  alone. Each bucket also shows its **tractability** as a separate small meter; a bucket can be full
  and useless and the picture must show that.
- **Session output score** prominent, with fit and correctness as separate meters beneath it.
  Output is their product; whichever is worse dominates.
- **Time series** of fit, correctness, output and poison share. One axis, all percentages.
- **Eight sliders**, grouped human / AI / shared.
- **Every rule from §4 printed on the page.** The prototype did this and it is the reason the faults
  were findable. Non-negotiable.
- **Loads precomputed `out/grid.json`** rather than running the model in JS. One implementation of
  the rules, in Python, or the two will drift.
- Theme-aware light and dark; no external assets beyond Google Fonts.

## 8. Provenance — what is anchored and what is invented

Put this table in the README and in the visualiser footer. **Nothing here is an effect size.**

| element | status |
|---|---|
| poison damage superlinear (`POISON_EXP`) | **anchored** — a single distractor does outsized damage (Shi et al., ICML 2023) |
| gate correlation `rho` | **anchored in form** — redundant inspection is not independent; value invented |
| partial clearance + residual floor | **anchored in form** — continued-influence meta-analysis; rate invented |
| tractability `tract(D)` | **anchored in form** — context rot; TMS directory. `D_STAR`, `KAPPA` invented |
| `BLIND` (need under-read when depleted) | **invented, and load-bearing.** Without it, lag alone washes out in steady state and discipline is inert. It was added *after* observing that inertness — flag it as the most contestable term in the model |
| `CAP_W`, `NEW`, `REF_MAX`, `PROMO` | **chosen for legibility**, selected by sweeping for a configuration where parameters visibly span |
| decay, poison, discernment rates | **user-set**, no empirical anchor |

## 9. Order of work

1. `model.py` + `gates.py`. Run G1–G6. **Report the gate results before building anything else.**
2. `run.py`, sweep grid, `out/grid.json`.
3. `viz/index.html`.
4. README with findings, the provenance table, and the measured answers to: the `rho` at which two
   gates stop beating one, the poison fixed point against prediction, and the optimal `curation`.

Do not proceed past step 1 if two or more gates fail — bring the failures back instead.

---

## 10. Amendments after the build review (2026-08-28)

Claude Code audited the spec before implementing and found four defects and one mis-description.
All accepted. **This section overrides §§3–8 where they conflict.**

### 10.1 Undefined constants — my omission

`EXT_MAX`, `CAP_D` and any bound on `Wh` are used in §4 and defined nowhere. Fixed:
`EXT_MAX = 0.05`, `CAP_D = 200`.

**`Wh` is bounded by saturating intake, not a hard cap.** Each unit of inflow lands with efficiency
`(1 - Wh/CAP_W)`. A hard cap is the obvious reading of §4 and it is what pinned G2 — `Wh` sat at
exactly `CAP_W(1-decay)` across the whole upper half of the discipline range, below decay ≈0.26,
which is two-thirds of the specced range. **This is the third time the same fault has appeared in
this model: inflow exceeding capacity, the cap silently doing all the work.** A saturating store is
the standard idiom and should have been the spec's from the start.

### 10.2 `RESIDUAL` shipped inert — my error, their reading is better

As worded, a 15% floor on the poisoned count could never bind against `clearance ≤ 0.1`. It was
exactly the fault class G1 exists to catch, written into the spec by the person who wrote G1.

Correct form: **15% of corrections do not take.** That is what continued influence actually says —
influence persists *after* correction — rather than a floor on how much may be cleared per session.

### 10.3 Curation needs a functional form

Odds-enrichment, not linear. The linear reading is degenerate: at `disc_h = 0.5` it removes ~10×
more poison than arrives, pins `Da_p` at zero, and makes `poison` inert.

### 10.4 `disc_h` was doing two jobs — **the one that matters**

`disc_h` gated promotion *and* set curation selectivity, and the two contaminated each other: a solo
reviewer at 0.7 beat a 0.5/0.5 pair at `rho = 0`, contradicting the catch algebra, because the solo
arm was also curating harder and winning on an unrelated channel.

`settled-questions.md` §3b warns against exactly this conflation — *"one variable standing for both is
an assumption, not an inference"* — and the spec then committed it internally. **Split them:**
`disc_h` gates promotion, a new `sel` (0–1) sets curation selectivity. The `rho` sweep must hold
`sel` fixed, and **the rho crossover must be re-derived after the split** — the reported numbers are
contaminated, independently of the config question.

### 10.5 `BLIND` — reclassified, and doing something other than advertised

Two corrections, both accepted.

**Better anchored than §8 said.** "Need under-read when depleted" is S5 plus the §3b edge-3 row
(Cherkaoui & Gilbert 2017: metacognitively impaired participants fail to scale reminders with
difficulty). Reclassify to **anchored in form, value invented** — the same status as `rho` and
`tract`.

**But it does something different from what was claimed.** At 0.35 the need curve is flat across the
lower half of its range, so `felt ≈ 0.36` is effectively constant and `ritual ≈ 0.36 + 0.64·discipline`.
That gives discipline its live span — but by making the signal a *constant* that discipline adds to,
not by overriding a *misleading* one. Those are different mechanisms and only the first was written
down.

**Required:** report `var(felt)` across every run. **Discipline may be described as "decoupling the
act from the feeling" only where `felt` actually varies.** Where it does not, it is an additive
offset and must be described as one. This is a reporting rule, not a tuning target — do not adjust
`BLIND` to make the nicer description true.

### 10.6 A standing methodological rule

One-at-a-time sensitivity reported 5 of 8 parameters inert at 0.017–0.069. They are not; poison only
accumulates where several conditions hold at once, and no OAT design visits that region. **OAT
sensitivity is unsafe for this model and for any model with interaction-gated effects.** The full
cross is the gate. Recorded because the weak reading looked entirely reasonable and was confidently
wrong.

### 10.7 Headline corrections to carry into the write-up

**The `rho` result undercuts a claim we had already made.** Two reviewers beat one better reviewer
only while their failures are near-independent, and the bar is low — `rho* = 2 − L(d_solo)/L(d)`,
`L(x) = −ln(1−x)`, giving 0.26 for a 0.5/0.5 pair against a 0.7 solo. Since the human is reading what
the AI produced, plausible `rho` is well above that. **"An argument for two reviewers rather than one
better one" was stated earlier in this programme and should be withdrawn or heavily qualified.**

**The curation optimum is the build's best result.** Peak output at `curation ≈ 0.065`, clearing both
endpoints by ~12× seed noise, and the mechanism is clean: `Dh` at the peak equals `REF_MAX`.

> **The optimum is the point where the durable store has been trimmed to exactly what one session
> can reference.** An unbounded store is worse than a curated one; over-curation is worse than both.

That is Robert's intractability claim, confirmed, with a mechanism rather than a shrug. Lead with it.

**Also report:** peak output is 0.543 at every `EXT_MAX` — only the curation rate that reaches it
moves. That invariance says `EXT_MAX` is not load-bearing for the headline, which is worth stating
explicitly since it was one of the undefined constants.

---

## 11. Amendments from the trace-channel notes (2026-08-21, read 2026-08-28)

### 11.1 New gate — G7 · Discipline must not be a corner solution

**In the model as specced, the ritual costs nothing.** Referencing and externalising consume no
budget that the work also needs, so more discipline is free and output is monotonic in it. That is a
corner solution, and it is the same defect the August artifact-inventory note diagnosed in the
previous engine — *"attention has three benefits and one weak cost, and no rival use. Nothing else
wants it."* `sim/correspondence/promotion_arms.py` had the contested budget and got a threshold out
of it; the four-buckets spec dropped it and nobody noticed.

**G7:** with the ritual drawing from the same per-session budget as the work, output must be
**non-monotonic in `discipline`**, with an interior maximum. If it is monotonic the model cannot
express the trade the whole theory is about and no result about discipline means anything.

Implement as: session yield `NEW` scales with `(1 - ritual · COST_RITUAL)`. `COST_RITUAL` is a new
constant; sweep it rather than picking it, as with `EXT_MAX`.

*G1 passing `discipline` at a 0.252 spread does not cover this. A parameter can span widely and
still corner — spread and interiority are different tests, and only the second one matters for a
prescription.*

### 11.2 The model has no channels 1 or 2 — a decision, not a defect

The trace-channel frame names three:

1. **you → model** — rich, and where all tooling investment goes
2. **model → you** — impoverished by construction; you receive a product, not a trace
3. **you-now → you-later** — the only symmetric channel, and the one debt runs on

**Four-buckets contains channel 3 and nothing else.** The human side and the AI side are two
parallel systems with no flow between them: nothing the human externalises reaches the AI store, and
nothing in the AI store reaches the human. That is not an approximation of channel 2 being thin — it
is channel 2 set to zero *and channel 1 absent altogether*.

Defensible as a scoping decision, since channel 3 is where debt lives and channel 3 is the claim.
But it must be **stated**, because a reader of the visualiser will assume the two columns interact.
Coupling them is a separate spec: it is the same "closing the loop" move flagged in
`settled-questions.md` §3b, and closing it produces bistability by construction unless the gain is
estimated rather than assumed. **Do not add it to this build.**

### 11.3 `BLIND` — better justified than §10.5 said

§10.5 anchored "need under-read when depleted" in metacognitive impairment. The trace-channel note
gives it a structural argument that is stronger and does not depend on any individual difference:

> **Channel 3 has no revelation event.** Channels 1 and 2 are tested constantly — the work either
> lands or it does not. The channel that decays silently is the one nobody is looking at, and it is
> the one you would need in order to look.

That is not a claim about impaired people; it is a claim about the architecture. Record it as the
primary justification for `BLIND`, with Cherkaoui & Gilbert as the individual-difference corroborant
rather than the anchor. Status stays **anchored in form, value invented**; the reporting rule in
§10.5 stands unchanged.

### 11.4 Two asymmetries, and they compound

Do not merge these — they are different claims with different sources.

| | asymmetry | source |
|---|---|---|
| **readability** | you can read what you left yourself; you cannot read the model's workings | the trace-channel frame |
| **rivalry** | classical stigmergic traces are non-rival; a context window's are rival in attention | `externalisation-evidence-ledger.md` §7.2, O4 |

SwarmWorld is the **symmetric, non-rival** case: shared world, every agent reads every trace. It is
therefore the right citation for making our asymmetry visible as a design fact rather than a
complaint — and it is **motivation and vocabulary, not evidence**, because nothing in it measures a
person. Two phrases worth taking verbatim: *"splits cognition from consequence"*, and evaluation
under unseen disturbances **after the agents are removed**, which is the delayed unaided transfer
test already operationalised on artifacts.

*Verified 2026-08-28: arXiv 2608.26081, Pal, Wang & Buehler, submitted 26 August 2026. The date is
genuinely the 26th. Affiliations were not on the abstract page — confirm separately before use.*

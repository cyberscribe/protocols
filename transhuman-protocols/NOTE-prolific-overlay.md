---
title: "What a Prolific wave could overlay on the sim"
date: 2026-08-28
---

# Prolific wave — what would interface with the sim

**The frame first, because it decides the design.** The posture machine became compelling when its oscillation was overlaid with real data — not because the model predicted the numbers, but because **a structure the model produced turned out to have a real analogue.** Same rule here: the data does not validate the sim. It tests whether the sim's *structural* claims have counterparts in people. A null is a result.

And the standing limit applies: Prolific gives you tasks, not careers. **You can test the mechanism at task level; you cannot test whether it aggregates.** That is the same ceiling every study in this literature sits under, and it should be stated rather than hoped past.

---

## Tier 1 — the two structural predictions, and they are cheap

### 1a. `corr(H, R)` with and without a witness — this is the study

The sim's most distinctive claim, arrived at three independent ways: **nothing endogenous separates writing-back from reasoning; only an exogenous witness does.** In the engine, `|corr(H,R)|` is 0.073–0.338 with an outside reviewer and collapses to 1.000 without one.

**Directly measurable.** Repeated tasks within person; per task record:

| model quantity | measurement |
|---|---|
| `R` | **solo share** — proportion of the task worked before first invoking AI (Wu's measure, instrumented in the task harness) |
| `H` | whether anything was recorded afterwards, and how much |

Randomise, within person and across blocks, whether a reviewer returns a verdict on the finished item.

> **Prediction: `corr(solo share, write-back)` is high in unreviewed blocks and falls in reviewed ones.**

That is a correlation structure, not an effect size — robust to almost every scaling assumption, and the sim is unusually specific about it.

### 1b. The `σ_A` mechanism — you control the reviewer, so you control the margin

Manipulate verdict accuracy directly. The sim's mechanism, which is what makes the crossover non-monotonic:

> **As the reviewer gets vaguer, write-back goes *up* and its judgment-bearingness goes *down*.**

Both are measurable — quantity by count, quality by rating the artefacts against the six-element rubric (criteria · assumptions · rationale · verification · failure conditions · revision triggers). That rubric score **is** `q_W`, operationalised.

**Two lines moving in opposite directions is the finding.** Whether total effectiveness crosses zero is a bonus; the crossing point depends on scaling the wave will not pin down.

---

## Tier 2 — the overlay, and the instrument already exists

`simulation-personas.md` already has **LOAD, DISS, SOV, DEBT** as scored 1–5 constructs from a 37-item bank with worked persona examples. That is the overlay apparatus, built.

**Put respondents on the load–debt plane and draw the flip locus across it.** Exactly the posture-machine move, on the panel that is already the stage's centrepiece: *here is where the sample sits, and here is the line the model says matters.*

### And the sharpest question in the whole wave costs two items

The model's darkest claim is that **self-review loses accuracy and independence at the same moment** — you lose the ability to notice the flip exactly when the flip happens.

So ask how much people self-review, and where they sit on (load, debt).

> **Prediction: self-review effort does *not* fall as respondents cross the model's line.**
>
> If it **falls**, people can see the line, and the model's darkest claim is wrong.
> If it **doesn't**, that is confirmation of the most important thing the model says.

Two items on an existing instrument, and both outcomes are publishable. This is the highest ratio of information to cost in the design.

---

## Tier 3 — later, and expensive

- **Delayed unaided probes** (`Δ = aided − unaided`, unaided block first) — the only route to `K` and to debt as a counterfactual rather than a self-report. Needs a return wave.
- **Store staleness injection** — supply the context store, degrade one element, measure detection. Tests store-side debt, which nothing in the literature touches.

---

## What this cannot do, said plainly

It cannot test aggregation, the archive trap over months, or the abolition claim — those need a longitudinal field engagement, which is the consulting work rather than a panel.

**What it can do is establish that the sim's structural claims have real analogues at task level** — which is precisely the standard the posture-machine overlay met, and the reason that overlay was worth having.

---

# Cost–benefit (priced 2026-08-28)

## Prolific's actual rates

| item | rate |
|---|---|
| platform fee — **academic / non-profit** | **33.3%** of participant rewards |
| platform fee — **corporate** | **42.8%** |
| recommended participant pay | **£9.00 / hr** |
| absolute minimum allowed | £6.00 / hr |
| VAT | charged and itemised separately; rate/base not published on the help pages — **assume 20% on the fee, confirm before budgeting** |

No subscription, no minimum spend, pay-as-you-go. **Which fee band applies is worth settling first** — it is a 9.5-point swing, and PI standing may qualify the work for the academic rate.

## A design change that pays for itself before any money is spent

Do **not** compute a per-person `corr(H,R)` and compare. Six or eight tasks per condition gives a correlation with an SE near 0.45 — noise.

**Run it as a multilevel slope × condition interaction**: solo share predicting write-back, tested against block condition. Same claim — *the reasoning-to-recording link is steep unwitnessed and flat witnessed* — but estimated from every observation rather than from per-person summaries. It cuts the required `n` by roughly half and is the difference between a study that can afford to run and one that cannot.

## The three tiers, priced

Assumes 55 min per participant for Tier 1 (8 tasks × 4 min, instructions, feedback screens, instrument, debrief) at £9/hr = **£8.25**; 10 min for Tier 2 = **£1.50**.

| | participants | rewards | + fee (acad / corp) | **≈ total inc. VAT on fee** |
|---|---|---|---|---|
| **Tier 2** — plane overlay + the two self-review items | 300 | £450 | £150 / £193 | **≈ £630 / £682** |
| **Tier 1 pilot** | 60 | £495 | £165 / £212 | **≈ £693 / £749** |
| **Tier 1 full** | 100 | £825 | £275 / £353 | **≈ £1,155 / £1,249** |
| **Tier 3** — return wave for unaided probes | 100 | ~£410 | — | **≈ £575 / £625** |

## The cost that is not on that table

**Tier 1 needs a task harness** — instrumented logging of time-to-first-AI-invocation, artefact capture, block randomisation, and a reviewer returning verdicts at controlled accuracy. That is a web app, not a survey. Two to four agent sessions plus review.

**And the real bottleneck is rating.** 100 participants × 8 tasks = **800 artefacts** to score against the six-element rubric. At a minute each that is ~13 hours of human rating. Mitigation: LLM-assisted rating with a double-rated calibration subset of ~100 — but the calibration subset is not optional, because `q_W` *is* the rubric score and an unvalidated rater makes the headline treatment unmeasured.

**Tier 2 needs no build at all.** The instrument exists in `simulation-personas.md`; the addition is two items in a survey tool.

## Recommendation

**Run Tier 2 first, on its own, for about £700.**

Not only because it is cheap and buildless. Because **it can invalidate the premise of the expensive study.** Its two-item question asks whether self-review effort falls as people cross the model's line. If it *does* fall — people can see the line — the model's darkest claim is wrong, and Tier 1's design should change before a harness is built for it.

That is correct sequencing, not just thrift: the cheap study is the one that can tell you the expensive one is pointed the wrong way.

## What the money buys

None of it validates the sim. What it buys is the difference between **a toy and a toy with a footing** — evidence that structures the model produces have real analogues at task level. That is the standard the posture-machine overlay met, and it is what makes the programme citable rather than illustrative.

At £700 for the first tranche, that is not a close call.

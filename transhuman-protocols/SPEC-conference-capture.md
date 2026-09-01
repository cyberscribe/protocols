---
title: "Spec — conference capture (Turtl ~70, Chile ~100)"
date: 2026-08-28
build_target: sim/externalisation/field/
---

# Conference capture

Two free waves, ~170 total, in person. This is not a Prolific design shrunk — the binding constraints are different and they change the instrument.

| constraint | consequence |
|---|---|
| **3–4 minutes on a phone**, not 10 at a desk | 37 items is impossible. Short form or nothing. |
| **no incentive** | participation has to be bought with something. See §3. |
| **Chile is Spanish** | hard requirement, and the two payload items must survive translation |
| **self-selected conference attendees** | non-random, AI-engaged, high-competence — **the hardest population for the model**, and say so |
| **two dates, two rooms** | ⚠️ **treat them as study + replication, not one pooled sample.** See §5 |

---

## 1. What we are actually asking

One question, from `NOTE-prolific-overlay.md` Tier 2, and it is the model's darkest claim:

> **Does self-review effort fall as people move into higher load and higher debt?**
>
> If it **falls** — people can see the line — the model is wrong about the thing that matters most.
> If it **doesn't**, that is confirmation, and it is the finding that would justify everything downstream.

Everything else in the instrument exists to place respondents on the plane so that question has an x-axis.

---

## 2. The instrument — short form

Target **12 items, ≈3 minutes.**

| block | items | source |
|---|---|---|
| LOAD | 3 | highest-loading items from the existing 37-item bank |
| DEBT | 3 | same |
| **self-review** | **3** | **new — the payload, over-specify these** |
| context | 3 | role · how often they use AI for real work · **does anyone else review their output** |

⚠️ **The short form must be calibrated against the long form or the plane positions mean nothing.**
Free fix, no extra recruitment: **run the full 37-item instrument on PI members** (who will give you ten minutes) with the short form embedded, and use the overlap to check the short form recovers long-form LOAD and DEBT scores. Do this **before** Turtl.

### The six items — verbatim from the frozen bank, chosen on the n=236 sweep

**All six lifted unchanged.** That matters more than which six (see §2b).

**LOAD** — the only three LOAD items answered by the full n=236 sample, three distinct facets, one reverse-keyed to catch straight-lining:

| id | facet | key | n | sd | text |
|---|---|---|---|---|---|
| `LOAD.dep1` | depletion | pos | 236 | 1.15 | *By the end of an AI-heavy session my judgement feels worn down.* |
| `LOAD.sup1` | supervision | pos | 236 | 1.11 | *Keeping track of what the AI has produced or changed leaves me mentally drained.* |
| `LOAD.rev1` | relief | **rev** | 236 | 0.98 | *I can hand work to AI and stay mentally fresh.* |

`LOAD.dep1` is the best item in the bank for this study — it is depletion degrading judgement, which is the mechanism itself.

**DEBT** — from the `sk` family (n=176), which is the **current** operationalisation after DEBT was re-pointed to capability erosion on 2026-07-21. The older `rp`/`dp`/`uw`/`rc` family (n=60) is superseded. **`DEBT.sk2` is excluded — it is the one item of fourteen that failed discrimination in the sweep.**

| id | facet | key | n | sd | text |
|---|---|---|---|---|---|
| `DEBT.sk5` | capability | pos | 176 | **1.25** | *There are things I now hand to the AI that I am no longer confident I could do well myself.* |
| `DEBT.sk4` | reversibility | **rev** | 176 | **1.23** | *If I stopped using AI tomorrow, I could return to my previous standard within a few weeks.* |
| `DEBT.sk3` | judgement | pos | 176 | 1.04 | *My judgement of what makes work good is getting less sharp.* |

sk5 and sk4 are the two highest-variance DEBT items in the bank. **sk3 is taken over the higher-variance `sk1` (sd 1.16) deliberately** — judgement erosion is what the plane's y-axis *means* in the model, and construct coverage beats 0.12 of sd. Swap sk3→sk1 if you would rather maximise spread.

### One free extra worth 13 items instead of 12

`DEBT.dp1` — *I reach for the AI before trying the problem myself* — **is solo share.** It is the model's `R`, the driver of everything, and the quantity Tier 1 was going to instrument with a task harness. It already exists, already fielded.

**Include it with the payload block, not scored into DEBT** (it belongs to the superseded family). Thirteen items still fits three minutes.

### 2b. The calibration is not a blocker — nest, don't reword

The long-form PI run cannot happen before 5 September. **It does not need to.** Because all six items are lifted **verbatim** from the frozen bank, any later long-form administration calibrates them retrospectively. Calibration is a job for October, not a dependency for next week.

⚠️ **This holds only if nothing is reworded.** Change a stem to fit a phone screen and the calibration is gone. If an item will not fit, cut it rather than edit it.

The Spanish version is a translated instrument whose measurement invariance is untested — **state that, do not paper over it.**

### The three self-review items — draft, and they carry the study

Each 1–5, and each must be unambiguous in Spanish:

1. *When I finish a piece of work, I go back over it myself before anyone else sees it.*
2. *When I check my own work, I usually find things worth changing.*  ← **perceived** accuracy
3. *Towards the end of a heavy day I check my own work as carefully as I do at the start.*  ← **the discriminator**

Item 3 is the one that matters. **The model predicts agreement stays flat across the plane** — people do not reduce self-review as they cross the line, because they cannot see it. Item 2 is the honesty check: if perceived accuracy holds while the model says actual accuracy has collapsed, that gap **is** the finding.

---

## 3. What the respondent gets, and why it is also the exhibit

**Give them their result on the next screen.** Where they sit on load and debt against everyone else in the room, and what the model says about self-review at that position.

**This is the recruitment mechanism and the demo at the same time.** They answer on a phone, they see themselves on the plane, and the plane is the panel you were going to show them anyway. **The instrument and the exhibit are one artefact.**

Put the **live aggregate on a screen at the stand.** People participate to watch themselves appear. That single decision probably doubles the response rate and costs nothing.

---

## 4. Build

Reuses the stage's plane panel and the house palette. Target: **static page, no server to babysit.**

| # | piece | notes |
|---|---|---|
| 1 | mobile form, 12 items, one screen per block | ~3 taps per block, progress bar, no back-navigation traps |
| 2 | consent screen | one paragraph, **no PII**, what it is for, who holds it |
| 3 | scoring + banding | already exists in the instrument |
| 4 | personal result screen | the plane, their dot, the cohort cloud |
| 5 | live aggregate view | same plane, all dots, for the stand screen |
| 6 | data capture | hosted form backend; **export must be trivial** — a CSV you can pull on the day |
| 7 | **es-CL translation + native-speaker review** | model translation is a first pass, **not the deliverable** |

**Linking without identifiers:** if you want to connect a respondent across waves or follow up, use a self-generated code (e.g. first two letters of mother's first name + day of birth) rather than anything identifying. Standard, cheap, and it keeps the consent short.

**Agentic time:** items 1–6 are one to two sessions. Item 7 needs a human pass and is the item most likely to slip — **start it first**, in parallel with the build.

---

## 5. Analysis — and the design decision worth the most

**Chile (5 Sept, ~100) is the study. Turtl (28 Sept, ~70) is the replication.** Chile comes first and is larger, which inverts the earlier assignment.

**Do not pool.** Twenty-three days between them is ample to lock the analysis in writing — so do it, and register it before Turtl.

At n≈70 the SE on a correlation is ≈0.12; at n≈100, ≈0.10; pooled at 170, ≈0.077. Pooling buys a little precision. **Splitting buys a replication in a different country, language and industry mix — worth far more**, and it costs nothing but the discipline of writing the analysis down before the second wave.

**If the date gap is too short to lock an analysis between them, say so and pool** — but that is the only reason to.

Primary: association between plane position and self-review item 3. Secondary: item 2 against position (the perception gap). Report the cohort as what it is — self-selected, AI-engaged, professional, non-random.

---

## 6. What I need from you

1. Sign-off on the six items, or the sk3→sk1 swap.
2. Whether `DEBT.dp1` goes in as the thirteenth.
3. Jose to do the **native-speaker pass** on the Spanish, not just to run the display — he is the right person and it is the item most likely to slip.

**Settled:** Chile 5 Sept, business-generalist, Spanish, ~100 · Turtl 28 Sept, ~70 · Jose can host the live aggregate, so build it as a URL he opens, no install.

---

## 8. Eight days — the critical path to 5 September

| by | what | blocks |
|---|---|---|
| **29 Aug** | six items signed off; English wording **frozen** | everything downstream |
| **30 Aug** | Spanish translation drafted | — |
| **31 Aug – 1 Sept** | **Jose's native-speaker pass** | printing/QR, final build |
| 30 Aug – 2 Sept | build: form · consent · scoring · result screen · aggregate view | — |
| **3 Sept** | test on real phones, both languages, both orientations | — |
| 4 Sept | QR codes, stand screen dry-run with Jose | — |
| **5 Sept** | Chile | |

**The translation is the critical path, not the build.** Freeze the English on the 29th even if the build is unfinished — the build can absorb slippage, a native-speaker review that starts on the 3rd cannot.

**Cut list if time runs short, in this order:** the live aggregate view (personal result alone still recruits) → the context block down to two items → `DEBT.dp1`. **Never cut the three payload items or the reverse-keyed pair** — those are the study.

---

## 7. The honest limit, stated up front

This tests one association in a self-selected professional sample at a single point in time. **It cannot test aggregation, the archive trap, or anything longitudinal.** What it can do is tell you whether the model's darkest claim has a real analogue in the population most likely to contradict it — for the cost of two conference stands you are attending anyway.

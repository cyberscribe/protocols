---
title: "Two debts — short-term and long-term, and the line between them is already in the model"
date: 2026-08-31
status: draft — input to the DRIVE practice strand, not further externalisation theory
see_also: ../../peakepro-diagnostics/cognition-assessment/settled-questions.md,
          ../../peakepro-diagnostics/cognition-assessment/sim/buckets/STUDY-PARAMETERS.md §4
---

# Two debts

**Short-term.** You let the AI decide the file structure and the naming conventions. Nothing is
lost — the structure is right there — but you have no index of it, so you pay a comprehension cost
the first time you need to find something. Reading it once discharges the debt.

**Long-term.** You use a calculator often enough that you lose arithmetic. Reading the calculator's
output restores nothing, because what you lost was never in the artefact. Only doing it unaided,
repeatedly, discharges this one.

## The line between them is `R`, and the model already draws it

`R` — `REHEARSE` in `model.py` — is the share of a lost item that re-reading the note restores.
`STUDY-PARAMETERS.md` §4 already states that **`R` is a property of the task, not of the person**,
and that tasks whose knowledge is tacit sit below `R*` by construction.

So the two debts are not two constructs. **They are the two sides of `R*`:**

| | short-term | long-term |
|---|---|---|
| `R` | high — the artefact carries what was lost | low — it does not |
| discharged by | **referencing**, once | **re-practice**, repeatedly |
| cost to discharge | bounded, one-off | unbounded, recurring |
| what it attaches to | an artefact you did not author | a faculty you stopped exercising |
| **has a revelation event** | **yes** — it announces itself the moment you go to find the file | **no** |

That last row is the important one, and it is the August trace-channel argument arriving from a new
direction: short-term debt is tested constantly, because you meet it whenever you use the thing.
Long-term debt is channel 3 going dark — nothing tests it, and the faculty you would need in order
to notice is the one that went.

**Which is why the vivid example is the wrong one to worry about.** Everyone can feel the file-
structure debt; nobody feels the arithmetic debt until they need arithmetic. The recoverable one is
the one that hurts, and the unrecoverable one is the one that is silent.

## The prescription that falls out, and it is not the obvious one

> **Externalise the high-`R`. Practise the low-`R`. Externalisation is the wrong tool for
> arithmetic.**

This is a real constraint on the programme's own advice, and it cuts against the simple version of
the thesis. More externalisation does not help a low-`R` faculty at all — it cannot, because the
knowledge does not fit in the artefact — and time spent writing it down is time not spent
practising. For low-`R` material the ritual is *doing it yourself on purpose*, not writing it down.

## Two consequences worth checking rather than assuming

**The practice bank almost certainly conflates them.** A practice addressing short-term debt
(indexes, naming schemes, decision records — things that make a store referenceable) and one
addressing long-term debt (deliberate unaided reps) are not the same product and do not compete for
the same slot. **Classify by which debt a practice discharges, alongside which term of the
effectiveness equation it moves.** That is a second axis on the registry and it is cheap to add.

**The instrument may conflate them too.** If the DEBT construct scores one quantity, and the two
debts have different remedies and different detectability, then two people with the same DEBT score
need opposite advice. That is checkable against the existing item bank — do the DEBT items load on
one factor or two? — and it is a better use of the wave-2 data than another posture cut.

## The fork, RESOLVED 2026-08-31 — and my proposal here was wrong

This section originally proposed reporting both readings and saying what each measures. **That is
refuted.** `sim/buckets/debt.py`, `DEBT-READINGS.md`:

| R | carried (1–5) | incurred (1–5) |
|---|---|---|
| 0.1 | 3.513 | 1.372 |
| 0.8 | 2.390 | 1.652 |
| **high − low** | **−0.955** | **+0.239** |

Both separate the regimes, **with opposite signs**, at 4.3× the within-regime spacing and with
discipline pinned at 1 so R is the only difference. `incurred` is not insensitive to the regime — it
is a strong, near-monotone, **backwards** indicator of it. High R keeps more in working memory, decay
loss scales with what is held, so *the recoverable regime creates more debt per session while being
in less debt.*

At fixed decay they are not two constructs at all: `incurred_raw = decay · CAP_W · (1 − carried_raw)`,
exact to 8.9e-16. One quantity, read backwards. They only become two when decay varies across a
field, and there `incurred` confounds how much is lost with how fast — over a 12-arm R × decay field,
Spearman(carried, R) = −0.615 against Spearman(incurred, R) = **+0.909**. Of the six most indebted by
`carried`, five are low-R; by `incurred`, one.

**Choose `carried`.** `incurred` is not broken — it measures gross churn — but it is not debt in the
instrument's sense and must not rank anyone.

### The scope of that, stated precisely

It resolves the fork **for this engine**, and it names the condition rather than the instance:

> The inversion arises whenever debt is **depletion of a stock** and loss is **proportional to the
> stock**. The diagnostic is whether `incurred` is a *flow out of* the stock or an *addition to* it.

`score.mjs`'s `incurred` is `delta × (1−a)` — an additive insult accumulating *into* `D`, not a flow
out of it — so there the two readings should be **positively** related and this result does not
transfer. Running the same check in that engine is cheap and is what closes
`settled-questions.md` §0 in full. It also matters more than it looks: `score.mjs` is where the
effectiveness equation lives, so it is the engine any practice ranking would actually run in.

### The warning for the practice registry — carry this into the DRIVE strand

> **A practice that raises `incurred` is not thereby harmful, and the best ones will tend to raise
> it.** Any registry field resembling "debt created per session" would systematically penalise
> exactly the practices worth recommending.

That field is an obvious one to add. Do not add it. Classify on **artefact rehearsal value (`R`)**
directly — a property of what the practice produces — not inferred from any debt score.

And `carried` is the right reading but not a pure one (−0.615, not −1): comparing people who differ
in forgetting rate needs `decay` controlled separately.


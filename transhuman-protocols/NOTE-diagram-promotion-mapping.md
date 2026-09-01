---
title: "Mapping the promotion simulation into exec-fn-ai-org"
date: 2026-08-28
status: draft
see_also: external-protocols-proposal-v2.md, ../../peakepro-diagnostics/cognition-assessment/sim/correspondence/promotion_arms.py
---

# Mapping the promotion simulation into the diagram

Variant built: `diagrams/exec-fn-ai-org_2026-08-28-promotion.svg`
(`python3 build-exec-fn-ai-org.py <out.svg> naa promotion` — nothing overwritten, base unchanged).

---

## 1. What the base drawing asserts, and where it is wrong

The base diagram draws **every crossing as a transfer**: something moves from one place to another,
and the only asymmetry recorded is that loading is short/grey/automatic while promotion takes the long
way round and is human-involved.

The simulation says two of those crossings have a **side effect on the person**, and the two side
effects have **opposite signs**. Neither is drawn.

| operation | what the diagram draws | what the sim says it also does |
|---|---|---|
| **load** | store → loop, automatic | **suppresses the occasion to reconstruct.** Looking it up means not working it out, and working it out is the only full rehearsal. Loading is *not* neutral for the person |
| **promote** | loop → store, human-involved | **refreshes** the store entry, **extends** its coverage, **rehearses** the person on what was written, and **costs** budget that would have gone to work |

So the base drawing shows one of five effects. The variant adds the two that carry the sign.

---

## 2. The notation: arrow produces, bar inhibits

Both new paths terminate on **the same box, from different edges**, because both act on the same
quantity with opposite signs. Splitting them across two targets would lose exactly the claim.

- **Top route, dashed, bar end** — loading suppresses. Dashed because the effect is *indirect*: loading
  does not remove anything from the person, it removes the occasion that would have refreshed them.
- **Bottom route, solid, arrow end** — promotion rehearses. Solid and full weight, because it is the
  contribution.

The bar/arrow pair is the systems-biology convention and it needs **no gloss text to read**, which is
what makes it usable here.

The two long routes also mirror each other around the drawing, which is a truth about the model and
not a composition trick: **both effects arrive at the person by the long way round.** Neither is
something the tooling does for you.

---

## 3. The finding: the diagram has no head

Both effects act on **the person's own copy of what they know**, and *the diagram does not contain
that object*. Every box in the human column is an externalisation — shared context and individual
context are stores; the tracking rows are artefacts. `Individual context` is the nearest thing
available and it is **not the same thing**: it is a personal store, which decays by correspondence
only, whereas the quantity the two new arrows act on decays autonomously.

The variant lands both arrows there as a placeholder. That is a known compromise, not a rounding.

This is the same absence the correspondence work already noted from the other direction — *"the
diagram contains no person; it draws the apparatus and leaves the cognizer implicit."* Leaving the
cognizer implicit was defensible while every arrow was a transfer between artefacts. It stops being
defensible the moment two arrows have the person as their **target**.

Three options, in increasing cost:

1. **Leave it.** Both arrows point into the human column and stop; the cognizer is the unlabelled
   thing they converge on. Elegant, and probably too subtle to survive a slide.
2. **Split `Individual context`** into the store and the head — two boxes, the store keeping its
   colour-keyed content dots, the head carrying nothing but the two arrows. Cheap, honest, and it
   makes the six-colour sync overlay sharper by contrast: the head is the one place with no
   colour key, because nothing in it is guaranteed to correspond.
3. **Draw the two decay processes explicitly** — store-side as discrete events (the demotion arrows
   already added on 28 Aug), head-side as a continuous fade. *Different visual grammar for different
   process type*, which is the whole §1 asymmetry of the proposal, drawn.

**Recommendation: option 2 now, option 3 when the model rewrite lands.** Option 2 is a twenty-minute
change and it removes a placeholder that will otherwise get quoted as if it were the claim.

---

## 4. Two quantities the drawing still cannot express

**Coverage.** The sim's sharpest result is that a store which covers *everything* removes every
occasion to work anything out — unaided retention falls to 0% as coverage goes to 1. The pills encode
*load policy* (`ALWAYS` / `AS-NEEDED` / `PER PROJECT`); coverage is a different quantity and is
unencoded. It could ride on the 4.5px accent bar as a **fill level**, which would make the dangerous
object visible as a combination of two encodings already present: `ALWAYS` **and** a full bar.
Deferred, because it needs a real number per store and the diagram is a representation, not a chart.

**The world.** Exogenous decay fires when the world moves, and the world is not in the picture. Per
the medium criterion — perceivable *and* controllable — project outcomes are **feedback, not trace**,
so they must not be drawn as another store. A band spanning both columns, feeding the demotion arrows,
is the shape; it is not drawn yet.

---

## 5. What each sim parameter is, in diagram terms

| sim | diagram |
|---|---|
| `store`, `COVERAGE` / `MAX_COV` | the four AI-side stores; the cap is per-tier scope |
| pill discipline | which stores load unconditionally — `ALWAYS` is the tier with no gate |
| `COST_STORE` vs `COST_WORK` | the loading arrow against its absence — the ratio *is* the store's whole value |
| `PROMOS` (budget) | the promotion arrow's cost, currently drawn as free |
| `rehearsal_gain` | **the new bottom arrow.** Nothing else in the drawing |
| `DECAY_K` (autonomous) | nothing — see §3 |
| `p_world` (exogenous) | nothing — see §4 |
| cascade project → general → standards | already drawn, and correct |

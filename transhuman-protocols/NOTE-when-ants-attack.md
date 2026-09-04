---
title: "When Ants Attack — what a 2001 security paper says our store is missing"
date: 2026-08-31
status: acted on — all three classes now in sim/buckets (2026-09-04)
source: Zhong & Evans, *When Ants Attack: Security Issues for Stigmergic Systems*, University of Virginia CS, 2001
see_also: NOTE-poison-neutralisation-literature.md, ../../peakepro-diagnostics/cognition-assessment/settled-questions.md §3c
---

# When Ants Attack

**Verify before citing:** retrieved as a UVA CS department paper, 2001, venue not stated on the PDF.
It may be a technical report rather than a published paper. Same rail as the SwarmWorld and Townsend
citations.

It is about attacks on **AntNet**, an ant-colony routing algorithm. It is an analogy for our work,
not evidence about human–AI cognition, and it is twenty-five years old. Cite it for vocabulary and
for the one structural property in §3, not for anything about people.

---

## 1. Three attack classes, and we model only the first

> **Superseded in part, 2026-09-04.** All three are now in the model. The table below is the
> reading as it stood; §5 records what was built and where this note was wrong. The heading is
> kept because the count it names — *we model only the first* — turned out to be wrong twice
> over, and in opposite directions.

| attack | AntNet | our analogue |
|---|---|---|
| **fabrication** — inject bogus traces, or replay real ones, to promote an inferior route | ✅ | `p_poison` — a bad item written at birth |
| **dropping** — selectively discard good traces to discredit a good path | ✅ | **none** |
| **tampering** — alter the trip-time a trace carries | ✅ | **none** |

**Dropping** is curation gone wrong in a specific way. Our curation uses odds-enrichment and assumes
selectivity correlates with quality; dropping is the regime where **pruning is worse than random**
because it preferentially removes what is good. We have never run that case, and the model is
perfectly capable of it — invert the enrichment and see.

**Tampering is the one that should worry us more, and it has no home in the model at all.** It
corrupts not the content but *the metadata about the content's reliability*. In our terms: not a
poisoned item, but a corrupted signal about how much to trust an item. That attacks the **discernment
channel** rather than the store, and every defence we have modelled — both gates, clearance, curation
— runs *through* discernment. A model whose only failure mode is bad content cannot represent an
attack on its own quality signal.

## 2. The vulnerability, stated in their words

> nodes "completely trust information in all backward ants they receive"

That is our AI side exactly: working memory is **replaced** each cycle from the durable store with no
re-evaluation of what comes back. We modelled that as a mechanic. They name it as the vulnerability.

## 3. The property we do not have, and it is the finding

The paper's recovery claim:

> "once the critical region has grown to include the external node, it must continue to create the
> network congestion otherwise the routing information will quickly recover to the original best path"

**In AntNet, poison requires continuous maintenance. Stop attacking and the system heals itself.**

Our store does not do this. Poison persists until explicitly corrected (`clearance`) or pruned
(`curation`), both of which cost attention. AntNet's trace strength has to be *continuously
re-earned*, so anything not re-earned fades — a bad write dies on its own.

*(The paper does not attribute recovery to evaporation, and does not discuss decay as a defence at
all. That reinforcement-and-decay is the mechanism behind the recovery is my inference, not their
claim. Do not cite them for it.)*

**Two immune systems, and we implemented the expensive one.** Ours costs attention per item. Theirs
costs nothing, because the dynamics do it. That was a modelling choice and we never examined it.

### The idea it suggests, and why it is only half right

**Usage-weighted retention** — an item's persistence depends on being *referenced*. Anything not used
fades. Poison that never gets read dies unattended, and the archive trap solves itself without a
prune.

It is not in the model, the diagram, or the practice bank, and it is close to but not the same as
CTX-17: *fix one thing when you open it* is repair-on-touch; this is **fade-without-touch**. They are
complements.

**But it breaks precisely where it would hurt most.** Rarely-used and critically-important is the
`ALWAYS` tier — working standards, low traffic, high consequence. Usage-weighted retention would
delete them first. Heylighen's rule stands and this does not overturn it: **optimal decay tracks
obsolescence speed, not usage frequency.**

So the honest form is tier-dependent — usage-weighted for the volatile tiers, obsolescence-weighted
for the durable ones. Which is the tier structure arriving for a third time, from a third direction.

## 4. What to do with it

1. **Run the dropping case.** Invert curation's enrichment so pruning removes good items
   preferentially. One parameter, and it tests whether our curation optimum survives a curator who is
   wrong rather than merely imperfect. Cheap.
2. **Record tampering as an unmodelled failure mode**, not as a to-do. Representing an attack on the
   discernment signal means giving discernment its own state, which is a bigger model, and the
   honest move is to name the gap rather than fill it.
3. **Do not add usage-weighted retention to the buckets model.** It is a good idea and it is
   tier-dependent, and the buckets model has one store per side by design. It belongs to whatever
   comes after, if anything does.

---

## 5. What was actually built, and where §1 and §4 were wrong

Done 2026-09-04 in `sim/buckets`. §4.3 stands; §4.1 and §4.2 did not survive contact.

**§1 was wrong to map fabrication onto `p_poison`.** They are different attacks with different
defences. A poisoned item is born in AI working memory and has to survive the promotion gate, so
discernment is worth something against it. A fabricated trace is written into the durable store
from outside and never meets the gate — so review skill, reviewer overlap and attention are worth
*exactly nothing*, and only clearance and pruning ever touch it. Now a separate parameter,
`fabricate`, and the point of it is which defences go dead rather than how much damage it does.

**§1 was right that dropping was already in the model.** `sel` widened to `[-1, 1]` with the odds
enrichment made reciprocal, so `sel = -1` is a curator who never once removes a poisoned item. No
new mechanism. Of the three classes this is the one the model represented natively, and nobody had
run it.

**§4.2 was wrong, and the reason it was wrong is the finding.** The recommendation was to name
tampering as a gap rather than fill it, on the grounds that it needs a quality claim held
separately from the true quality. The first half of that was right and the conclusion was not.

The gate, as it stood, could only ever reject a poisoned item: `catch` was applied to items already
drawn as poisoned, and a good item could not be wrongly caught. So a tamper term could only scale
the poison-rejection rate, which is exactly what lowering `disc_h`/`disc_a` does, and adding it
would have been a second dial for one effect. That much was checked before building anything.

What was missing was **the false-positive path**, and it is not a modelling technicality. It is the
human asleep at the wheel. A reviewer who has ceded cognitive sovereignty is not reading the work,
they are reading its label — and a reader of labels is wrong in *both* directions the moment the
labels are corrupted: waving through what claims to be clean, and binning good work that claims to
be dirty. Nothing else in the model can discard a good item. Only inattention can.

So tampering is two parameters, not one. `tamper` is the share of quality claims corrupted away
from the truth; `sovereignty` is the share of promotion decisions taken on the content rather than
on the claim. And the interaction, rather than either dial, is the result:

| | `tamper = 0` | `tamper = 1` |
|---|---|---|
| **`sovereignty = 1`** | 795 | 795 — *identical, to the digit* |
| **`sovereignty = 0`** | 800 — *better than reading the work* | 36 |

(Accumulated score over 1500 sessions at the visualiser's opening settings.)

**Ceding sovereignty is not a weak defence. Until somebody lies to you it is a better one than
vigilance**, because an uncorrupted claim is a perfect signal and review is not. Then it goes to
nothing. And while it goes to nothing the catch rate the gate reports does not fall — at the
visualiser's opening settings it *rises*, 32% to 47%, because binning good work slows the store's
growth and store size is a term in the catch rate. The gate's own health indicator improves as the
gate stops working. A defence that is superior right up until it is worthless, reported by an
instrument that reads high while it fails.

That is a better sentence about the trust trap than the one this note set out to write, and it came
from taking the paper's third attack seriously instead of filing it as out of scope.

**Still true, and still the gap:** the model has no path from a contaminated AI store into human
working memory. `Wh` carries no poison term. An attacker can take the whole right-hand side apart
and the left-hand side stays clean, because there is no channel by which it could not. The attacks
do not touch that limit, and §3's recovery property — poison that must be continuously re-earned
or fade — is still not in the model either.

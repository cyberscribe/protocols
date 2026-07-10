# DRIVE ↔ assessment mapping — evaluation and recommendations

*2026-07-08. Evaluates the cognition assessment's advice layer (per-posture, sim-lever-ranked "Start
here" engine; practices registry) against the DRIVE loop (`methodology.md`). Question: how does the
custom feedback we deliver from the model's drivers map to the intent of the five phases — and where
doesn't it?*

---

## 1. The headline: near-isomorphism, and why

DRIVE and the assessment's inner loop are the same object at two registers. The dynamics model's
inner loop is *intention → four mechanisms (context, outcome phrasing, tooling, assumptions) →
measure/diagnose → intervene → next iteration*. DRIVE is that loop as practitioner phases:

| DRIVE phase | Model/sim counterpart | Practice families & levers |
|---|---|---|
| **Decide** | Sovereignty axis; ownership behaviour `d` (own the decision, define "done", override) | SOV-1/3/4, INT-1, GOV; lever `d` |
| **Request** | The four controllable mechanisms of §5 — context, outcome phrasing, tool availability, assumptions — **one-for-one** | CTX, INT, TOOL, ASM |
| **Inspect** | Anti-anthropomorphism discipline; habituation-interrupts (`k_H` drift = Inspect decaying) | ASM-3 pre-mortem, adversarial review, "assume it's wrong once"; lever `habituation` |
| **Validate** | Calibration: trust tracking *true* reliability (`k_T`), base-rate over vivid miss (`β`, `p_err`); confirms against the done-criteria set in Decide | TRUST-1/2/3/5, REV, TOOL-4, GOV-5; levers `k_T`, `β` |
| **Evolve** | The master lever: `μ` (systematise the win), `δ` (keep scaffolding current), `retrieval` (keep your hand in); the `μ·ℓ > δ` bifurcation | SYS-1, DEBT-2/4, CTX-1/3/5, REV-2/3, DEBT-1/3; levers `mu`, `delta`, `retrieval` |

This is not retrofitting — both derive from the same thesis (trust your practice/system, not the
model). Two loop-closures worth naming explicitly in copy: **Validate is only possible because Decide
defined "done"** (the phases are coupled, not just sequential), and **Evolve is the sim's stability
condition stated as behaviour** — "no update, no learning, no method" *is* `μ·ℓ > δ` in method form.
The metacognitive self-regulation / "learning loop" fifth construct is, precisely, *a measure of
whether the respondent runs Evolve*.

## 2. Postures as phase failures

Each posture is a specific DRIVE phase gone missing or hypertrophied — this is the cleanest
consulting story the mapping yields, and none of the posture copy currently says it:

| Posture | DRIVE diagnosis |
|---|---|
| **Overreliance** | Inspect has gone quiet (fluent output accepted on trust; comfort drift); Validate right-sized to zero |
| **Compliance** | Decide abdicated (mandated use, no ownership) and Evolve absent (transactional, no accretion) |
| **Hypervigilance** | Validate hypertrophied and un-right-sized — re-deriving everything at every stakes level; Evolve missing (checks don't compound into a system, hence the load) |
| **Partnership** | Loop running; next frontier (F5) = running DRIVE at team scale, teaching it |

The Inspect/Validate split earns its place here: the Hypervigilance fix is literally "let Inspect
cover what you're currently Validating" (right-size the check to stakes = `k_T` lever), and the
Overreliance fix is "reinstate Inspect before trust". A model with a single "check" phase couldn't
express either prescription.

## 3. Where the mapping strains — three honest gaps

**3.1 Inspect is under-provisioned in the practice bank.** The bank carries Inspect only as
Tier-3/habituation items, which the ranker suppresses for everyone except Overreliance. In DRIVE,
Inspect is universal — every loop passes through it as the cheap filter before the costlier
Validate. Missing: a named "tells" practice (fluency ≠ accuracy; fabricated-citation checks;
suspicious specificity; over-smooth confidence) and possibly an item probing the skill ("I can often
spot a wrong answer before checking it against anything"). This is the one place the sim's
sensitivity ranking and DRIVE's intent genuinely disagree — the sweep says habituation is
low-leverage globally, DRIVE says Inspect is a per-loop invariant. Resolution: Inspect belongs in
the *method* (taught, universal) even where it's not the highest-leverage *lever* (ranked); don't
let the ranker's economics delete a phase of the practice.

**3.2 Decide is under-measured in the instrument.** Sovereignty measures whether you *own*
decisions, not how *well* you decide — prioritisation quality ("what's worth doing, to what
standard") isn't probed at all. Acceptable for the free diagnostic; but DRIVE's D is the GTD-lineage
half of the offering, so the curriculum must carry what the instrument doesn't measure. Name the
scope rather than imply coverage.

**3.3 Concurrency has no DRIVE home.** The CON family (explicit handoffs, WIP limits, the
working-memory scratchcard) and delegation itself sit *between* Request and Inspect. Recommended
framing over a sixth letter: **DRIVE runs per delegation; orchestration is running many DRIVE loops
well** — a meta-skill above the loop, which is also the honest description of agentic co-working in
2026. Keeps the acronym, names the layer.

## 4. Recommendations (cheap → structural)

1. **Add a `drive_phase` column to `registry.csv`** (D/R/I/V/E; some practices dual-tag). The
   sim_lever→phase map in §1 makes this mechanical. It becomes the join key between assessment
   advice, curriculum, and whitepaper — same role `sim_lever` plays for the sim agent.
2. **Render "Start here" grouped by DRIVE phase, phase names visible.** The free report then teaches
   the method's vocabulary before the client buys anything — the congruence requirement (free =
   position + direction, paid = traversal) satisfied on the page itself. The personalised
   composition stays; only the presentation ordering changes.
3. **One line per posture naming the broken phase** (per §2 table) in the posture fragments —
   folds into the copy-deck pass already in flight.
4. **Add the Inspect practice(s)** to the bank (tells checklist), exempt from tier-suppression the
   way the Overreliance habituation guarantee already works.
5. **Scope note on Decide** in the offering one-pager: instrument measures loop-health (R-I-V-E +
   ownership); decision *quality* is curriculum-carried (GTD lineage — the differentiator, not a
   bug).
6. **Orchestration framing** ("many DRIVE loops") into `methodology.md` when next touched.

## 5. Trade-off read (Authentic / Principled / Effective)

Adopting DRIVE as the assessment's presentation vocabulary scores high on all three — Authentic
(same underlying loop, not veneer), Principled (each phase anchors to an existing literature: D →
SDT autonomy + GTD; R → context/CLT; I → fluency-miscalibration; V → Lee & See calibration; E →
SRL/Bjork), Effective (one vocabulary across funnel: blog → assessment → workshop → coaching). The
residual risk is forcing fit: CON has no phase, Decide is thinly measured. Both are named above
rather than absorbed — the mapping should advertise its two seams, which is itself the DRIVE-ish
move.

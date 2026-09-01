---
title: "Review dossier — externalised protocols, 2026-08-28"
purpose: independent review; written to be attacked, not to persuade
date: 2026-08-28
---

# Review dossier — 2026-08-28

Everything produced in one session, with its provenance, its errors, and its soft spots. **Read §3 and §4 first if you have limited time — that is where this is weakest.**

---

## 1. The artefacts, in reading order

All under `~/workspace/projects/protocols/transhuman-protocols/`.

| # | file | what it is |
|---|---|---|
| 0 | `external-protocols.txt` | Robert's original research statement — the input |
| 1 | `external-protocols-review.md` | citation audit + feasibility. **§2 superseded** by #2 |
| 2 | `external-protocols-model.md` | the formal model, v3. §10 is the v2→v3 changelog |
| 3 | `external-protocols-study-design.md` | the empirical design review |
| 4 | `visualisation-design-principles.md` | why the posture machine works and the four-up doesn't |
| 5 | `externalisation-sim-brief.md` | diagram re-read, layman walkthrough, ten decisions |
| 6 | `SPEC-externalisation-sim.md` | the build handover. **§0 and §5 are the ones to check** |
| — | `diagrams/exec-fn-ai-org_2026-08-28-demotion.{svg,png}` | proposed one-line diagram change (cascade arrows double-headed) |

Related, not produced here: `peakepro-diagnostics/cognition-assessment/sim/` — six engines, the posture machine, the four-up.

### The three claims worth reviewing

1. **`T^\* − P = (1−α)(O − P)`** — miscalibration is the outcome–process gap times the load-driven weight on outcome, and it requires no irrationality because `O > P` is what substitutive AI honestly produces. (#2 §2)
2. **Preservation is promotion, not loading** — loading is locally optimal and globally harmful *only through displacement of reasoning*; promotion preserves both the evidence and the capability needed to detect the harm. (#2 §3–4)
3. **Show what the model makes impossible, not what it makes large** — the design rule separating the posture machine's success from the four-up's failure. (#4)

---

## 2. Claim ledger — verified

Checked by me directly, against the source, this session.

| claim | source | how checked |
|---|---|---|
| Chen et al. 2026, *Human Factors*, `10.1177/00187208261477486` — "two trust updating pathways" is the **paper's own** framing; process updating attenuated under load | journal page | fetched |
| Bastani et al., PNAS 2025 `10.1073/pnas.2422633122` — ~1,000 students, grades 9–11, Turkey, Fall 2023, **preregistered**; GPT Base +48% practice / **−17% unaided exam**; GPT Tutor +127% / n.s. | author PDF | fetched |
| Liu et al. `arXiv:2604.04721v4` — 1,222 participants, effects after ~10 min | arXiv abs | fetched |
| Wu et al. `arXiv:2608.23543`, HCOMP 2026 | arXiv abs | fetched |
| **Wu's actual result**: solo share predicts latent-ability gain; AI usage does not after controlling initial ability (`α_usage` posterior mean **0.0004**); authors say the coefficient "should be interpreted as associational rather than causal" | arXiv HTML, results section | fetched, quoted |
| Klein & Klein `10.3389/frai.2025.1719019` — defines *cognitive sovereignty* and *Sovereignty Trap*; PMC12738859 resolves to it | Frontiers + PubMed | fetched |
| Meng `arXiv:2606.15078` — *cognitive debt*, "stock of unverified reasoning obligations"; **does not** use the sovereignty terms | arXiv | fetched |
| product-vs-sum is an open inconsistency; `00-CURRENT.md` sides with sum on the pole at `debt → 0` | `00-CURRENT.md:44–46`, `theory-under-simulation.md:142` | grepped |
| "Correctness spans 0.040 in total… Two bands is what this term can honestly carry" | `fourup-core.js:244,247` | grepped |
| the DRIVE score "is 3.7× gameable" | `sim/README.md:84` | grepped |
| `SEED = 1163` | `fourup-core.js:54` | grepped |

---

## 3. Claim ledger — NOT verified. Attack here first.

| # | claim | status | what it would break |
|---|---|---|---|
| **U1** | **The PNAS correction** `10.1073/pnas.2518204122` (PMC12403119, Aug 2025) — contents unknown, 403 on every route tried | **unread** | Bastani's numbers, which are quoted throughout. **Read this before anything goes public.** |
| **U2** | **Chen's coefficients are conditional mixed-model slopes that cannot be summed to test conservation** — accepted from third-party feedback; I never read Chen's results section | **second-hand** | the strict simplex `w_p + w_o = 1`, which drops two parameters from the model |
| **U3** | Chen's authors interpret the finding as *reconfiguration* rather than global impairment | **abstract-level only** | same — this is the entire warrant for the simplex |
| **U4** | Linearised stability boundary `k < 2 sin(π/(2(2τ+1))) ≈ π/2τ` | **stated from memory, hedged, never computed** | the "tolerable gain falls as 1/τ" result and the proposed figure |
| **U5** | **Everything about the sim tree except the four items in §2** — trust-trap's parameter values, the posture machine's eight states and two empty seats, `v-habitability` results, `VIEW-DECISIONS` clauses, `NOISE_NULL` 3.38/4.03 | **two subagents read ~40 files; I spot-checked four facts** | the design-principles diagnosis (#4) and most of the spec's inherited parameters |
| **U6** | Liu et al. is still a preprint | no journal ref shown, but absence is not proof | a minor characterisation in #1 |

**U5 is the big one.** The four-up post-mortem is the analytical centrepiece of #4 and #5, and it rests on a summary of a summary. The four load-bearing facts held under spot-check, which is encouraging and is not the same as the whole account holding.

---

## 4. Assumed, not derived — the soft joints

| # | assumption | where | why it matters |
|---|---|---|---|
| **A1** | **`P` is the calibration target** — trust tracking process evidence is what "calibrated" means | #2 §2 | the identity's whole interpretation. Flagged in the file as an assumption. If `O` were an unbiased estimator of reliability there would be no thesis |
| **A2** | **Promotion contributes to capability** (`H` in `grow(R,H)`) | #2 §4, #6 §3 | **explicitly our hypothesis, not Wu's** — Wu measures `R`. Do not let this acquire a citation by proximity |
| **A3** | The predicted empty cell `(¬W, ¬R, C)` | #5, #6 | a *prediction*. The spec's rail says if all eight cells are visited that is the result. Check the spec actually holds that line |
| **A4** | The colour overlay in `exec-fn-ai-org` means "correspondence maintenance across a boundary" | #5 Part 1 | **my reading of Robert's diagram**, and a lot is built on it. Confirm with the author |
| **A5** | `H` and `R` are separably identifiable given `Λ` and `ρ` as non-shared drivers | #5 §3.2, #6 C2 | if false, eight cells collapse to four and the figure does not exist. **C2 tests it; it is untested today** |

---

## 5. Errors I made this session, and where they were caught

Included as signal about where else to look, not as ceremony.

| error | caught by | fixed |
|---|---|---|
| Wrote `∂g/∂Λ < 0` and **cited Wu for it**. Wu supports displacement, not loading-holding-reasoning-constant | third-party critique; I then verified it against the paper and confirmed | v3: separate `R` state |
| Defined the calibrated bit as `\|T − P\|` — **undefined** in exactly the cell the figure interrogates | me, at spec-writing time | `\|T − B\|` against model truth |
| Framed the `π` objection as *overloading* | Robert — π is a **constant, therefore reserved, therefore never a variable**. Category error, not a style issue | notation rule; also caught `σ(·)` by the same test |
| Called `Z` "the tool-to-practitioner axis", conflating what the harness makes observable with who does the intervening | third-party critique | `Z` is tool-side, `H` practitioner-side |
| Said the simulator for this model did not exist, before surveying | the survey — six engines, a full visualiser ecosystem | rewrote the gap analysis |

**Pattern worth a reviewer's attention: four of five are overclaiming — asserting support that the source or the structure does not give.** Look for more of that.

---

## 6. Live disagreements, unsettled

- **`Z` scalar or vector `(Z^tool, Z^practice)`.** Third-party says vector; I pushed back that `Z^practice` duplicates `H` and would be collinear. **Not settled.** Decide before the protocol is written.
- **Effectiveness: product or sum.** `00-CURRENT.md` sides with sum; `theory-canonical.md` still argues product; DRIVE still computes it. **The edit has not been made.**
- **`Π → K`.** See A2.
- **Whether the trust-trap loop should stay separate.** Recommended related-not-integrated; the state vectors are close enough that a reviewer might reasonably disagree.

---

## 7. What would falsify what

**The model** — study 1 (#3): if load-only preserves unaided judgment as well as promotion, the headline fails. If promotion helps only while AI remains available, it produced better loading, not preserved judgment. Any "loading has no effect" claim needs a predefined equivalence bound.

**The sim** (#6 §5): C1–C3 are the gate. C2 failing means the state space collapsed. C3 finding all eight cells occupied means there is no structural claim and no exhibit — and that gets reported.

**The framing**: every cited study is short-horizon, task-level, on students or paid participants, with the AI as solution-provider on checkable problems. The thesis is about professionals on ill-specified problems over months. **The claim that a task-level mechanism aggregates is the contribution and it is untested by anyone.** A reviewer should press hardest here.

---

## 8. Outstanding actions

- [ ] Read PNAS correction `10.1073/pnas.2518204122` (U1)
- [ ] Read Chen's results section directly (U2, U3)
- [ ] Compute the stability boundary numerically rather than quoting it (U4)
- [ ] Spot-check more of the sim-tree account, or re-derive #4's diagnosis from primary files (U5)
- [ ] Confirm A4 with the diagram's author
- [ ] Settle `Z` scalar-or-vector
- [ ] Make the product→sum edit in `theory-canonical.md`
- [ ] Split the Klein & Klein / Meng bullet in `external-protocols.txt`
- [x] Fix the DRIVE stage-name drift. Settled 2026-08-31: **Decide · Request · Iterate · Validate · Evolve**
      (Inspect was retired in favour of Iterate). Only "Define" remains as drift wherever it appears;
      the deck slide is corrected.

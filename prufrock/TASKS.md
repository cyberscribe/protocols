# Tasks

> Path to a polished Long Now Lab 001.1 (Book of Time) submission. Deadline **2026-06-05**.
> Three lanes: **[H]** Human (Robert) · **[C]** Cowork (me) · **[K]** Code. Items on the critical path are marked **[CRIT]**.
>
> **Convention:** all docs in `to-review/` are staged for Robert's human review. Cowork should not treat them as final or auto-edit them once parked there — only update on Robert's instruction or to apply his returned feedback.

## Critical Path

```
[C] update artefact-and-v1 for shared-seed mechanic
        ↓
[H] review pass: concept · previous-work · ln-situating · artefact-and-v1
[H] review formalisation                                ─┐
[H] review protocol-diagram                              │  parallel
[H] pick seed sonnet (public-domain volta couplet)      ─┘
        ↓
[C] apply review feedback across all docs
        ↓
[C] draft full video script (from inline shot list)
        ↓
[H] review video script
        ↓
[H] record piece-to-camera takes
        ↓
[C] edit video (B-roll, cuts, captions)
        ↓
[H] approve final cut
        ↓
[K] render PDFs (formalisation, artefact-and-v1, ln-situating)
[K] render diagram to PNG + PDF
[K] package submission bundle
        ↓
[H] final read-through · fill Google Form · submit
```

Cycle time is dominated by the video (script → review → record → edit → approve) and by Robert's review windows. Estimated critical-path duration: 2.5–3.5 weeks if review cycles stay tight.

---

## Active

### Cowork

- [ ] **[CRIT] Update `to-review/artefact-and-v1.md`** for the shared-seed mechanic
  - Current draft references the old participant-seeded model (2 seeds + 12 responses per poet); needs alignment with §9.1's shared-corpus seed + 1-nominal-line + 13-rotated-lines design
- [ ] **[CRIT] Apply Robert's review feedback** across to-review/ docs, formalisation, and diagram
  - Hold open until Robert's review pass returns
- [ ] **[CRIT] Draft full video script** from the inline shot list — recorded-take prose with timing, cues, B-roll markers
- [ ] **[CRIT] Edit video** once Robert's takes arrive — B-roll cuts, lower-thirds, captions, ~2:30 final
- [ ] Compose **Affiliations & Community** text (~3 sentences) once Robert names the channels he wants cited
- [ ] Compose **Google Form paste-in** text for each field (concept, previous work, affiliations, how-did-you-hear)
- [ ] Verify all hyperlinks in `previous-work.md` resolve (TAPoetry archive, film-poems page, Poet Tips, talk handouts)
- [ ] Draft a one-page **submission bundle README** — file names + reading order for the reviewer

### Human (Robert)

- [ ] **[CRIT] Review pass on `to-review/`** — concept, previous-work, ln-situating, artefact-and-v1
  - Inline edits welcome; comment back any structural concerns
- [ ] **[CRIT] Review `formalisation.md`** for technical correctness
  - Particular attention to §1.1 prompt-anonymity invariant, §4.2 dialectic framing, §6.1 form-constraint extensions, §9.1 shared-seed Sonnet Trial
- [ ] **[CRIT] Review `protocol-diagram.svg`** for visual clarity
  - Open in browser; check that the seed-fan-out and Latin-square authorship pattern read at a glance
- [ ] **[CRIT] Pick seed sonnet** — a public-domain source poem whose volta (lines 12–13) becomes the shared seed pair
  - Constraints: ≥100 years old, English, sonnet form
- [ ] **[CRIT] Review video script** (after cowork drafts it)
- [ ] **[CRIT] Record piece-to-camera takes** per the shot list (6 short beats; landscape 16:9; phone fine)
- [ ] **[CRIT] Approve final video cut**
- [ ] **[CRIT] Final read-through** of all submission materials
- [ ] **[CRIT] Fill Google Form** and submit
- [ ] Decide whether `poetry-blockchain-precedents.md` is included as supporting media (form allows ≤10 files)
- [ ] Confirm preferred LinkedIn / personal-site URLs

### Code

- [ ] **[CRIT] Render `formalisation.md` → `formalisation.pdf`** with proper LaTeX math (pandoc + xelatex/lualatex; Greek letters, $\Theta$, $\phi$, $\mathcal{L}^*$, etc. must render cleanly)
- [ ] **[CRIT] Render `protocol-diagram.svg` → PNG and PDF** at submission-grade resolution
- [ ] **[CRIT] Render `to-review/artefact-and-v1.md` → PDF** (after Robert's review applied)
- [ ] **[CRIT] Render `to-review/ln-situating.md` → PDF** (or fold into another document)
- [ ] **[CRIT] Package final submission bundle** — folder of named files (or zip) respecting form's 10-file / 10-GB-per-file limits
- [ ] **Word-count validator** for `to-review/concept.md` — script (`wc -w` with title/epigraph excluded) confirming body ≤ 500
- [ ] **Latin-square validator** for §9.1 — generate a 13-row Latin rectangle on 14 poems with no fixed points; output the assignment matrix as a table; sanity-check that the dispersion design is realisable
- [ ] Optional: **reference simulation** — small Python notebook running one cohort end-to-end, verifying authorship-dispersion arithmetic and rendering the resulting matrix as a chart. Could be embedded as an appendix in `artefact-and-v1.md`

## Waiting On

*(items move here when handed to Robert or external dependency)*

## Someday

- [ ] **V2 / Volume II** experiment configuration — different form (ghazal trial, tanka cycle) or non-textual response medium (audio, image)
- [ ] **Decennial Rosetta-class nickel-disk** etching design conversation with Long Now (post-acceptance)
- [ ] **Participant cohort recruitment plan** — Year 1 cohort assembly through Poetry Society / Kundiman / FPT SIG
- [ ] **Long Bet** text and stake amount for the post-trial registry entry (e.g. "By 02050, a Prufrock-protocol chain will be canonised in a major literary anthology of record")
- [ ] **Open-source mobile app** scoping spec (post-acceptance build)
- [ ] **Bitcoin Ordinal inscription** mechanism — per-line on-chain anchor, signed at commit time

## Done

- [x] ~~Draft 500-word concept~~ (2026-05-09)
- [x] ~~Draft Previous Work paragraph (with Poet Tips addition)~~ (2026-05-09)
- [x] ~~Long Now positioning paragraph~~ (2026-05-09)
- [x] ~~Mathematical formalisation~~ (2026-05-09)
- [x] ~~Generalise formalisation: response medium, form-constraint extensions, prompt anonymity invariant, PromptType variable, dialectic framing~~ (2026-05-09)
- [x] ~~Correct §9.1 Sonnet Trial to shared-seed model + Latin-square dispersion~~ (2026-05-09)
- [x] ~~Replace π → φ and Π → Θ for notational hygiene~~ (2026-05-09)
- [x] ~~Protocol diagram (initial chosen-rotation version)~~ (2026-05-09)
- [x] ~~Redraw protocol diagram for shared-seed model~~ (2026-05-09)
- [x] ~~Outline video shot list (inline)~~ (2026-05-09)
- [x] ~~Productivity scaffolding (TASKS.md, CLAUDE.md, dashboard.html)~~ (2026-05-09)
- [x] ~~Integrate central frame: poetry-as-long-now + regression-to-mean vs specificity-to-the-timeless~~ across concept, ln-situating, CLAUDE.md, project memory (2026-05-09)

# Project: The Prufrock Protocol

A protocol for marking time through cryptographically-signed responses to random interruptions, framed by poetic form. Pitch in development for Long Now Lab 001.1 (*Book of Time*). Deadline: **2026-06-05**.

## Central frame (load-bearing)

Poetry is among the oldest long nows we have: for four thousand years it has bound the *long* — timeless themes — to the *now* — concrete individual moments — in a single act. Poetry is the human timepiece that predates the clock. The Prufrock Protocol takes this intrinsic long-now structure and makes it the timepiece itself.

Where generative AI compresses human concerns toward the statistical mean — averaging into anonymous probability-weighted text — the protocol works in the opposite direction. It expands what is compressed in humanity in aggregate into specific, signed, dated, located instances of individual consciousness expressing itself, giving specificity to the timeless. Marvin Bell's *infinite game of using words to transcend words* is the design language at the heart of this work.

This is the central frame for every artefact: README, concept, ln-situating paragraph, video script, deck slide. The frame should be legible in each — drift toward "just a counter-AI argument" or "just a clever distributed poetry protocol" is drift away from the project's spirit.

## One-line claim

In an era when generative AI averages human concerns toward the statistical mean, The Prufrock Protocol expands the aggregate back into specific signed moments of individual consciousness — using the long-now form of poetry as a timepiece for a new kind of time, at once unique and timeless.

## Design history

The mechanic has evolved through three iterations:

1. **Single-spine cascade (initial draft).** One chosen poet writes line 1; everyone responds to that one line; one chosen poet's response becomes the spine for the next day. Authorship concentrated. Rotation was a permutation.
2. **Adjacent-pair single-author seeding.** Each poet seeds their own poem with 2 lines on days 1–2; days 3–14 use combinatorial rotation showing each poet a different (poem, tail-pair) prompt. Authorship dispersed but each poet still "owns" their nominal seed.
3. **Shared-seed dispersed model (current, v1 sonnet trial).** A *single* public-domain volta couplet seeds *every* poem in the cohort. Day 1: every poet writes line 1 of their nominal poem in response to the same shared pair. Days 2–14: Latin-square rotation; each poet writes one line in each of the 13 non-nominal poems exactly once. Authorship maximally dispersed; each poem is 1 nominal line + 13 rotated lines.

Each iteration was a refinement — same dialectic (situated experience meets disruption produces synthesis), same cryptographic backbone, same time-marking goal.

## Key files

- `README.md` — long-form essay (voice reference; do not alter). Absorbed the previous `pitch.md`.
- `formalisation.md` — protocol formal specification, parameterised over experiment configurations. Sonnet trial in §9.1.
- `protocol-diagram.svg` — dispersed-authorship diagram (5×5 illustrative slice).
- `../to-review/prufrock/concept.md` — 500-word concept for the Long Now form.
- `application/previous-work.md` — credentials paragraph.
- `memory/ln-situating.md` — paragraph situating Prufrock against existing Long Now work.
- `poetry-blockchain-precedents.md` — comparative review of 7 prior poetry-on-blockchain projects.

(The previous `to-review/artefact-and-v1.md` spec has been absorbed: the deliverable content lives below in *v1 deliverable* and *Institutional pairing*; the file itself was retired.)

## v1 deliverable

***Continual Proof: Volume I*** — a hand-bound print codex (edition of 250) containing the first season's 14 sonnets, dated in Long Now Zero, deposited canonically at the Long Now Foundation Library and at The Interval. Anchored at four pace layers:

- **Operational (live):** open-source mobile app + public web ledger
- **Per-line:** Bitcoin Ordinal inscription per signed line
- **Annual:** the print codex
- **Decennial (aspirational v2):** Rosetta-class nickel-disk etching of each decade's spine

## Open decisions

- **Which public-domain sonnet supplies the volta couplet (the shared seed)?** Constraints: ≥100 years old, English, sonnet form. Awaiting Robert's pick.
- **Cohort composition for Year 1.** Two cohorts proposed: poets (recruited via Poetry Society UK and Kundiman US, prior partners) and laypeople / protocol theorists (recruited via the FPT SIG).
- **Long Bet text.** Candidate prediction: *"By 02050, a Prufrock-protocol chain will be canonised in a major literary anthology of record."*
- **Whether `poetry-blockchain-precedents.md` ships as supporting media** in the Long Now form (10-file limit).
- **Affiliations & community channels** to cite in the form.

## Institutional pairing

- **Long Now Foundation** — canonical host, custodian of the codex and decennial nickel-disk artefact.
- **Protocols Institute** — protocol design and validation.
- **Poetry Society (UK)** + **Kundiman (US)** — literary cohort recruiters; both prior Transatlantic Poetry partners.
- **Long Bets** — registered prediction at trial close.

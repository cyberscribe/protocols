# Gwern Branwen — work relevant to poetry protocols

Working notes. Cross-referenced against Gwern's site (gwern.net) where I'm
confident; flagged as `[verify]` where I'm working from memory.

## Who he is, briefly

Independent researcher, long-running personal site at **gwern.net**. Writes
across statistics, AI, cryptography, self-experimentation, anime, darknet
market archives, longevity, decision theory. The site itself is the artifact
— continuously revised, dense link economy, popups for citations, decade-plus
maintenance discipline.

The reason he matters for *protocol theory* (independent of poetry) is that
his site is one of the cleanest extant examples of a sustained personal
research protocol made legible. The methodology is the message.

## Most relevant for "poetry protocols"

### GPT-3 Creative Fiction (gwern.net/gpt-3)
May 2020. Foundational practical document on eliciting poetry, fiction, and
stylistic pastiche from large language models. Established many of the
prompt-engineering conventions that became standard practice. Includes
extensive raw poetry samples — Dr. Seuss pastiche, Allen Ginsberg pastiche,
formal-verse experiments.

Protocol-theoretic angle: the essay is implicitly an argument that prompts
*are* protocols — structured conditions under which a desired generative
behavior becomes elicitable. The craft is protocol design.

### GPT-2 poetry fine-tuning
Earlier work (2019). Fine-tuned GPT-2 on a poetry corpus (Project Gutenberg
poetry collection, plus other sources). Documented at
gwern.net/gpt-2 and gwern.net/gpt-2-preference-learning. `[verify
exact pages]`

Relevance: pre-RLHF demonstration of training-as-protocol — what does it mean
to "teach" a model the protocol of being a poet?

### "RNN Metadata for Mimicking Author Style" (2019)
Adding metadata tokens (author, year, genre) so the model conditions on
identity. A protocol-design choice that prefigures the system-prompt era.
`[verify title]`

### "The Scaling Hypothesis" (gwern.net/scaling-hypothesis)
Not directly poetry, but the central modern statement of the claim that
"scaling is a protocol" — capability follows from a small set of training
choices applied at sufficient magnitude. Relevant to any argument about why
poetic protocols in LLMs work the way they do.

## Most relevant for the Long Now / time-marking lab

### "Long Content" (gwern.net/about, gwern.net/long-content)
Essay-and-practice on writing that's intended to remain useful and revised
over decades, not days. Argues for "long site" as a counter-protocol to the
churn of social-media-paced content. Direct kinship with Long Now's framing.
Worth citing in any application to the time-marking sub-lab.

### Site revision logs
Every essay carries its revision history. This is a working artifact of
*epistemic time* — a protocol for marking how a thought changed. Robert
could probably write 800 words on this alone for the Protocolize magazine.

## Adjacent work worth knowing

- **"It Looks Like You're Trying to Take Over the World"** — fiction.
  Short story rendering AI takeover from inside a model's perspective. Sits
  near the PI fiction SIG's territory.
- **"This Waifu Does Not Exist"** — generative-image protocol experiment.
- **Self-experimentation pages** — sleep, nootropics, dual n-back. Personal
  protocols documented as research artifacts. The methodological honesty
  (negative results, abandoned experiments) is itself a protocol worth
  modeling.
- **Darknet markets archive** — archival protocol at scale; relevant to
  the PI memory SIG.

## Where Robert's and Gwern's work meet (per the PI GA transcript)

Timber referred to "the poetry protocols between Guern [sic] and Robert"
as a body of work the PI leadership has learned from. Worth noting that
this framing already places the work as joint — not parallel. A short
piece authored or co-authored with Gwern, framed for Protocolize, would
land on already-warm ground.

## Suggested integration angles for the talk / PI work

1. **Prompts as protocols.** Use Gwern's GPT-3 essay as the canonical
   example of a body of practice that's already protocol-theoretic in
   substance but not in name.
2. **Long Content as counter-protocol.** Pair this with Long Now's framing
   for the time-marking lab.
3. **Site-as-protocol.** Gwern's site is the most legible example of a
   personal research protocol I can think of; potentially a case study
   for the formal protocol theory SIG.
4. **Revision logs as poetic protocol.** A more speculative angle —
   the revision log as a poem of attention over time.

## Citations to verify before using publicly

- Exact URLs and titles for the GPT-2 fine-tuning and metadata work
- Date and venue of any Gwern poetry that's been formally published vs.
  site-only
- Whether Gwern has written explicitly on "protocol" as a term, or whether
  it's a frame Robert is bringing to the work

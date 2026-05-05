# Feeds brief — Protocols for effective human-AI collaboration

*Last updated: 2026-05-05*
*Purpose: dual-use document. Reads as a topic statement for Robert. Functions as the scorer prompt for the recurring RSS-relevance task.*

---

## Core thesis

How should humans and AI systems coordinate to do high-quality knowledge work together, and what conventions, formats, and ceremonies make that work durable, ergonomic, and resistant to known failure modes?

The synthesis Robert brings to this is unusual:

- GTD (Getting Things Done) — capture, clarify, organise, reflect, engage; trusted-system thinking; horizons of focus. Certified franchisee, decades of practice.
- Kanban / Theory of Constraints — flow, WIP limits, pull systems, explicit policies, continuous improvement.
- Agile / Scrum — iterative delivery, ceremony design, retrospectives, team coordination.
- Engineering team effectiveness consulting — sociotechnical patterns, comms hygiene, decision-making, DORA-flavoured metrics.
- Deep technical familiarity with software, systems, and AI — capability, alignment, ergonomics; hands-on with current agentic tooling.
- Poet Laureate of the Protocol Institute — door-opener at PI specifically. Carries weight there but is not the research thesis.

The pitch positioning: cross-disciplinary synthesis is rare in AI-collaboration discourse, which skews toward pure theory or vibes-driven adoption. Few people have actually run engineering teams, taught GTD professionally, *and* know AI internals at depth. The gap is real and pitchable.

---

## Domains in scope

1. **Human-AI collaboration patterns.** Agentic workflows, copilots, supervised agents, MCP, prompt protocols, guidance documents, context management, eval-driven development, the practitioner literature on actually shipping work with AI.

2. **Protocol theory.** Protocol Institute output, Venkat Rao protocol writing, Long Now Foundation, coordination/governance protocols, ceremony design, plurality-adjacent work.

3. **Productivity-system thinking under AI.** GTD evolution, Kanban / TOC, second-brain / PKM with AI augmentation, knowledge-worker effectiveness research.

4. **Team and engineering effectiveness.** Agile / Scrum / Lean evolution under AI tooling, DORA / Accelerate, team topologies, retrospectives and ceremony design as it intersects with AI.

5. **AI tooling for knowledge and code work.** Claude Code, Cursor, agent frameworks, MCP ecosystem, eval methodology, prompt engineering as a discipline.

6. **Failure modes and critique.** Sycophancy, automation bias, deskilling, context-window pathologies, the Lindsey-et-al interpretability line on affect and reward hacking, AI-induced sloppy thinking, model drift.

---

## Source list

The verified source set lives in `feeds-config.json` — 28 sources, mix of RSS and page-diff modes. Each entry carries `id`, `name`, `mode`, `url`, `tier`, `tags`, and optional `notes` for page-diff selectors. Five sources dropped on 2026-05-05 after consistent zero-yield: ribbonfarm and bret-victor (both archival, no new posts), linus-lee (static homepage, no extractable post structure), apollo-research (JS-rendered SPA, no extractable post links), radicalxchange (URL redirected, no extractor matches).

The list spans:

- **Anthropic technical surfaces** — Transformer Circuits (interpretability), alignment.anthropic.com, anthropic.com/news.
- **Practitioner / engineering effectiveness** — Simon Willison, Charity Majors, Will Larson, Pragmatic Engineer, Ethan Mollick, Lenny Rachitsky.
- **Protocol theory and cognition critique** — Venkat Rao (Contraptions), Convivial Society (Sacasas), Kneeling Bus (Drew Austin), DataChutney.
- **Knowledge work, tools-for-thought, design** — Maggie Appleton, Andy Matuschak, Cal Newport, John Maeda (How to Speak Machine), Tom Critchlow.
- **Epistemics, research methodology, cognition science** — Henrik Karlsson, Adam Mastroianni, Erik Hoel, Robin Hanson, Slime Mold Time Mold.
- **Institutional / state-of-field** — Stanford HAI, Long Now Foundation.
- **Alignment / evals** — METR.
- **Coordination / protocols / plurality** — Vitalik.
- **Long-tail tech-philosophy** — Kevin Kelly (Technium).

Tier (`high` / `medium` / `low`) reflects expected signal density for the thesis. All sources get scored by the recurring task; tier is informational ranking, not a behavioural switch in v1.

Sources without RSS (Transformer Circuits, anthropic.com/news, alignment.anthropic.com, Stanford HAI, Long Now, DataChutney, METR, Technium) run in `page-diff` mode — see `CONVENTIONS.md` for the multi-mode design rationale.

Prune entries by editing `feeds-config.json` directly. Adding a source is the same operation in reverse — append a new entry with a unique `id`.

---

## Relevance criteria (scorer guidance)

The brief is a contract. Apply each criterion strictly. Items not clearly meeting any criterion are rejected — over-permissive scoring fills `read-and-review/` with noise that's worse than empty.

### Score `high` when the item:

1. **Articulates a protocol, pattern, or practice** for human-AI work that someone else could read, learn from, and adopt or critique. The *protocol-or-practice test*: would the reader finish with a transferable insight about *how* humans and AI should work together? "I built X with Claude Code" alone is not high. "Here's the workflow pattern I evolved while building X — here's what I'd change next time" is.

2. **Documents a failure mode or pathology** in human-AI collaboration with enough mechanism to learn from — sycophancy, automation bias, deskilling, context-window drift, cognitive surrender, model affect bleeding into output, alignment misses with practical impact.

3. **Provides citable scaffolding for the PI pitch** — a frame, a study, an institutional position, an empirical result Robert could stand on or argue against in writing about human-AI collaboration protocols.

4. **Surfaces what PI is publishing or discussing** directly. Useful for pitching into live conversations.

### Score `medium` when the item:

5. **Engages substantively with adjacent practitioner territory** — engineering effectiveness, knowledge work, productivity systems — and applies under AI conditions even when not explicitly about human-AI collaboration. Charity Majors on observability, Larson on engineering org design, Pragmatic Engineer on tooling shifts: medium when AI-relevant, otherwise low.

6. **Critiques the cultural / cognitive impact of AI on human work, attention, language, or agency** with substance and specificity. Sacasas, Drew Austin, datachutney's cognitive-surrender material land here. Score medium for analytical critique with mechanism; drop to low if it is general lament without analytic content.

### Score `low` when the item:

7. Touches the topic but lacks transferable substance — an AI-assisted demo with no workflow or pattern extracted, a side-project showcase, an opinion piece without specifics.

### Score `reject` when the item:

- Is generic AI hype, model release announcement, or capability benchmark with no practice content.
- Is "Top 10 prompts" or similar low-density listicle output.
- Is tooling release notes without ergonomics or workflow analysis.
- Is crypto / tokenomics / governance content unconnected to coordination protocols Robert would actually use.
- Is from a `tier: high` source but is genuinely off-thesis (cooking, parenting, hobbies, personal life).
- Is a re-share of older content the source has covered before.

### Poetry-protocols carryover

The poetry-protocols frame from earlier work stays as a narrow lens, applied only when an item explicitly intersects human-AI collaboration. Mnemosyne / Bell / Gwern do not earn an item a high score by association. The exception: a piece that directly applies poetic / ritual / mnemonic frames to human-AI workflow design — rare, valuable, scores high.

### Application discipline

- The source's `tier` from `feeds-config.json` is a prior, not a guarantee. A `tier: high` source can publish low-relevance items; a `tier: low` source can occasionally publish gold. Score the *item*, not the *source*.
- **The protocol-or-practice test applies only to criterion 1.** Criteria 5 and 6 are explicitly looser — substantive engagement under AI conditions is sufficient for `medium` without the extracted-pattern test. Over-applying criterion 1's strictness to the whole brief produces under-scoring and false rejects.
- When unsure between adjacent scores, default to the higher one for criteria 5–6 (where the bar is substance under AI conditions). Default to the lower one for criterion 1 (where the bar is transferable practice). Never default to `reject` for content that addresses AI's impact on practice, cognition, or coordination.
- The `reason` field names *which criterion* matched, not a summary of the article. "high — criterion 2: documents the model-affect-bleeding-into-output pathology with mechanism" is good. "high — discusses interesting AI work" is bad.

### Personal stack signal

Robert works in the OpenClaw workspace using Claude Code, MCP, and adjacent agentic-coding tools (Pi by Mario Zechner — the foundation OpenClaw is built on — Aider, Cursor, Claude Agent SDK) in his daily practice. Items that substantively engage with these specific tools — design choices, ergonomics, workflows, failure modes, eval results — have direct relevance regardless of the source's tier. Default such items to at least `medium`; `high` if they articulate a transferable pattern or document a real failure mode.

Personal-stack-relevant signals: OpenClaw, Pi (Zechner's agent), Claude Code, MCP ecosystem and tooling, Anthropic technical work, agentic-coding eval results, multi-agent orchestration patterns, Cursor / Aider / Continue ergonomics analysis.

### Worked examples

Concrete calibration. When uncertain, pattern-match these:

| Item type | Score | Why |
|---|---|---|
| Venkat (Contraptions / Ribbonfarm) on protocol theory, world-machines, or coordination | `high` or `medium` | criterion 3 — citable scaffolding for PI; criterion 2 if it identifies failure modes; criterion 6 if it addresses cognitive impact |
| Pragmatic Engineer / Charity Majors / Will Larson on AI infrastructure, agentic engineering, eval practice | `medium` | criterion 5 — adjacent practitioner territory under AI conditions. Does NOT require a protocol-or-practice extraction. |
| Sacasas (Convivial Society) on attention / language / agency / cognition under tech | `medium` | criterion 6 — analytic critique with mechanism. Drop to `low` only if pure lament without analytical content. |
| Mollick on interface ergonomics, agent design, prompting practice | `medium` | criterion 5; `high` if a transferable workflow pattern is articulated |
| Willison demonstrating "I built X with Claude Code" without pattern extracted | `low` or `reject` | criterion 7 — touches topic without transferable substance |
| Any source on a model release announcement, capability benchmark, or "Top N prompts" listicle | `reject` | low practice density |
| Posts substantively engaging OpenClaw, Pi, Claude Code, MCP, Cursor, Aider | `medium` minimum, often `high` | personal-stack signal — direct daily-practice relevance |
| Karlsson / Hoel / Mastroianni / Hanson on epistemics or methodology under AI | `medium` | criterion 5 or 6 if substantive |
| Anthropic technical research (Transformer Circuits, alignment) | `high` | criterion 2 (failure-mode mechanism) and criterion 3 (citable scaffolding) |
| A `tier: high` source publishing a personal-life or hobby post unrelated to thesis | `reject` | source-tier is a prior, not a guarantee |

---

## Output expectations

Each scored item lands as its own file in `00-protocols/read-and-review/` per the convention in `CONVENTIONS.md`. Filename: `YYYY-MM-DD-source-slug.md`. Frontmatter carries title, url, source, published date, collected date, `status: read-and-review`, tier, relevance reason, tags. Body carries a one-line LLM summary (≤30 words), the clipped article body, and an empty `## Notes` section for Robert to populate after reading.

The recurring task does not generate a separate digest file — the directory listing of `read-and-review/` *is* the digest. If a session-time skim is wanted, generate it on demand in chat from the directory contents.

Items surface as *potential captures* per the workspace GTD convention (§4.2 / §9). They are not auto-pushed to OmniFocus.

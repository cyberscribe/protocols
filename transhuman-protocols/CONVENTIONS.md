# transhuman-protocols — thread conventions

*Last updated: 2026-05-10*

Conventions specific to the *Effective Protocols for Human-AI Collaboration* research thread. Workspace-wide conventions live in the root `CONVENTIONS.md`.

---

## Directory layout (this thread)

| Path | Purpose |
|---|---|
| `STATEMENT.md` | Research statement (the load-bearing thesis for this thread). |
| `feeds/` | RSS / page-diff / search surveillance pipeline. Holds `config.json`, `brief.md`, `feeds.opml`, plus pipeline state (`.feeds-state.json`, `.feeds-runs.log`). |
| `read-and-review/` | Inbox for newly gathered articles awaiting reading. *(gitignored)* |
| `read/` | Articles after reading. Retained for back-reference from the corpus. *(gitignored)* |
| `research/` | Daily read-and-review digests scoring evidence against the A/B pillar grid (see scheduled task `review-read-and-review-from-protocols-research`). |
| `resources/` | Distilled lookup material — curated cross-references (e.g. `gwern-notes.md`). Not raw research; this is the post-distillation layer. |
| `pi/` | Protocols Institute general-assembly transcripts and PI-facing artefacts. |
| `fptsig/` | Formal Protocol Theory SIG materials — distillation, references, urls-with-context, plus a local Roam graph dump (`fptsig/roam/`, gitignored). |
| `protocol-reader/` | The Protocol Reader anthology distillation and citation list. |
| `considerations.{canvas,opml,mindnode}` | Brainstorm / mind-map artefacts mapping the broader theme tree. |
| `sources.md` | Lightweight pointer file. |

---

## Read-and-review workflow

The research stream flows: **capture → read → distil → corpus**.

### 1. Capture

Articles enter via the recurring surveillance task or manual save.

The recurring task is a **multi-mode surveillance pipeline**, not just an RSS reader. Several of Robert's highest-signal sources (Anthropic Transformer Circuits, Stanford HAI, DataChutney) don't publish RSS at all — RSS-only would systematically miss exactly the curated research surfaces and irregular institutional drops he most wants to surface. The task supports three poll modes per source:

- **`rss`** — fetch RSS / Atom feed, dedup by GUID. Standard blogs, Substacks, WordPress.
- **`page-diff`** — fetch HTML index page, diff against last-seen content snapshot, surface new entries. For static research surfaces with no feed (e.g. transformer-circuits.pub).
- **`search`** — periodic search-API call against configured topic queries, surface new hits. For institutions that publish reports irregularly without feed surfaces (e.g. Stanford HAI).

All three modes write the same per-item file shape into `read-and-review/`. The mode is a per-source config field in `feeds/config.json`. Manual saves use the same file shape — drop a file in `read-and-review/` matching the convention below.

### 2. Read

When Robert reads an item, the file moves from `read-and-review/` to `read/`. Frontmatter changes:

- `status: read-and-review` → `status: read`
- `read_date:` set to the read date
- Notes added inline under a `## Notes` section.

### 3. Distil

When an item is referenced in corpus writing:

- The corpus file links to the source as a standard markdown link to `read/YYYY-MM-DD-source-slug.md`.
- The source file's `distilled_into:` frontmatter list gets the corpus path appended.

This gives two-way traceability: corpus → source by link, source → corpus by frontmatter. `grep` over `distilled_into:` surfaces orphans (read but never used) and lets any source show every place it has fed into.

---

## Per-item file convention

Filename: `YYYY-MM-DD-source-slug.md` where the date is the collection date and source-slug is a short kebab-case identifier (e.g. `simon-willison-context-windows`).

Frontmatter:

```yaml
---
title: "Article title"
url: https://example.com/article
source: simon-willison
published: 2026-05-03         # ISO date if known, else null
collected: 2026-05-04         # date the file was created
status: read-and-review       # or: read
tier: high                    # high | medium | low (per feeds/brief.md scorer)
reason: "Direct on-topic — agentic workflow patterns"
read_date: null               # ISO date when moved to read/
distilled_into: []            # list of corpus-file paths citing this item
tags: [agentic, context-management]
---
```

Body (in order):

1. `# {title}` heading.
2. One-line source attribution: `> Source: [{source}]({url}) — published {published}`.
3. `## Summary` — short LLM summary (≤30 words by default).
4. `## Article body` — clipped content from the source. Full text where licensable, excerpt with link otherwise.
5. `## Notes` — added by Robert after reading. Quotes, arguments, links to corpus drafts that distil this.

A blank `_TEMPLATE.md` lives in `read-and-review/` so new items can be cloned cleanly.

---

## What does NOT belong in this flow

- **Distilled lookup material** (cross-reference compilations, glossaries, "everything Gwern said about X") goes in `resources/`, not `read/`.
- **Working drafts of corpus writing** go wherever the corpus lives — not here.
- **Generic AI / productivity links Robert won't return to** — drop them or note them in the appropriate session, don't pollute `read-and-review/`.

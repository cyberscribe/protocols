# 00-protocols — workspace conventions

*Last updated: 2026-05-04*

This document records the file layout and working conventions for the `00-protocols` workspace. Future sessions and scheduled tasks should read it before adding files.

---

## Directory layout

| Path | Purpose |
|---|---|
| `poetry-talk/` | Materials and assets for the poetry-protocols talk that opened the door at the Protocol Institute. |
| `pi/` | Protocol Institute general assembly transcripts and PI-facing artefacts. |
| `resources/` | Distilled lookup material — curated cross-references (e.g. `gwern-notes.md`). Not raw research; this is the post-distillation layer. |
| `read-and-review/` | Inbox for newly gathered articles (RSS pulls or manual saves) awaiting reading. |
| `read/` | Articles after reading. Retained for back-reference from the main corpus. |
| `feeds-brief.md` | Topic brief and scorer prompt for the recurring RSS-relevance task. |

The main corpus (PI pitch drafts, longer-form writing) does not yet have a fixed home in this folder. When it lands, this section gets updated.

---

## Read-and-review workflow

The research stream flows: capture → read → distil → corpus.

### 1. Capture

Articles enter via the recurring surveillance task or manual save.

The recurring task is a **multi-mode surveillance pipeline**, not just an RSS reader. Discovery during the 2026-05-04 source-confirmation pass found that several of Robert's highest-signal sources (Anthropic Transformer Circuits, Stanford HAI, DataChutney) don't publish RSS at all — building RSS-only would systematically miss exactly the curated research surfaces and irregular institutional drops he most wants to surface. The task supports three poll modes per source:

- **`rss`** — fetch RSS / Atom feed, dedup by GUID. Standard blogs, Substacks, WordPress.
- **`page-diff`** — fetch HTML index page, diff against last-seen content snapshot, surface new entries. For static research surfaces with no feed (e.g. transformer-circuits.pub).
- **`search`** — periodic search-API call against configured topic queries, surface new hits. For institutions that publish reports irregularly without feed surfaces (e.g. Stanford HAI).

All three modes write the same per-item file shape into `read-and-review/`. The mode is a per-source config field in `feeds-config.json`. Manual saves use the same file shape — drop a file in `read-and-review/` matching the convention below.

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
tier: high                    # high | medium | low (per feeds-brief.md scorer)
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

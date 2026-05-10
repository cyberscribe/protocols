# 00-protocols — workspace conventions

*Last updated: 2026-05-10*

This repository holds materials under the umbrella of *humane protocols for the transhuman age*. Three peer research threads sit under that umbrella, plus supporting material. Future sessions and scheduled tasks should read this before adding files. Thread-specific conventions live inside each thread's own folder where applicable.

---

## Top-level layout

| Path | Purpose |
|---|---|
| `README.md` | Public landing page (served via GitHub Pages). |
| `poetry-talk/` | Materials and assets for *The Infinite Game of Poetry* (talk, July 2025) — one of the three threads. Opened the door at the Protocols Institute. |
| `prufrock/` | *The Prufrock Protocol* — pitch in development for The Long Now Foundation Lab 001.1 (Book of Time). Deadline 2026-06-05. |
| `transhuman-protocols/` | *Protocols for Effective Human-AI Collaboration* — the broad research thread on transposing human collaboration paradigms into transhuman protocols. Holds the read pipeline, daily research digests, distillations, and adjacent reference material. See `transhuman-protocols/CONVENTIONS.md` for thread-specific read-flow conventions. |
| `blogs/` | Robert's ongoing writing — drafts (`drafts/`) and published posts (`published/`). Sits at root as a peer of the threads but is **not a research project**: it's an ongoing writing practice. Not promoted in the public README. Cross-thread blog-format material (e.g. talk-derived essays) lands here rather than in any thread's `to-review/`. |
| `to-review/` | Single workspace-wide review queue. Subfolders are by thread (e.g. `to-review/prufrock/`). |

The three threads are peers, not nested — Prufrock is **not** a subset of the human-AI collaboration thread, and vice versa. They are distinct projects sharing the same umbrella. `.obsidian/` and `.git/` are housekeeping.

---

## `to-review/` semantics

Documents parked under `to-review/` are awaiting Robert's human review. **Cowork must not auto-edit them once parked** — only update on Robert's explicit instruction or to apply his returned feedback. Treat them as paused, not final. New review-ready drafts go under the appropriate thread subfolder (e.g. `to-review/prufrock/`); create new subfolders as new threads acquire review queues.

---

## Naming and dating

- File names: `kebab-case.md` (lowercase, hyphenated).
- Dated files: `YYYY-MM-DD-slug.md` (ISO date prefix). For Long Now-adjacent contexts the project text uses 02026-style five-digit dating, but filenames stay four-digit ISO.
- Workspace dates in prose: ISO `YYYY-MM-DD`. Convert relative dates ("Thursday") to absolute when persisting.

---

## Voice and formatting

- Concise, declarative, trusted-advisor register.
- British spellings (synthesised, centralised) for project text; American where it matches an external venue's house style.
- Bias toward prose; lists and bullets only when content suits. No decorative bolding.
- No emojis unless functional. Never in code comments.

---

## GitHub Pages

The repository is exposed as a GitHub Pages site whose surface is **`README.md` only**. No other files are served. Treat the README as the single public entry point; link out from there to whatever the public surface should grow to include.

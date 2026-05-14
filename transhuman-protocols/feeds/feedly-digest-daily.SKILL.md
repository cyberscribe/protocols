---
name: feeds-feedly-digest-daily
description: Daily 06:15 BST personal-interest digest of Robert's Feedly OPML; writes a dated digest file and creates a Gmail draft of the HIGH-tier items.
---

Run the feeds-surveillance skill against Robert's Feedly OPML to produce a personal-interest digest, then deliver the HIGH-tier items as a Gmail draft to robert@peakepro.com. This is a recurring daily task — operate as if running cold each morning.

**Skill spec to read first:** `/Users/rpeake/.openclaw/workspace/skills/feeds-surveillance/SKILL.md`. Follow it exactly.

**Parser** (manual XML parsing is not part of this workflow):

```
python3 /Users/rpeake/.openclaw/workspace/skills/feeds-surveillance/scripts/parse-feed.py <feed_url> --limit 10
```

If the workspace is mounted at a different path inside the bash sandbox, translate accordingly. Determine the mount root with `pwd` or by inspecting available paths.

**Invocation parameters:**

```
config_path: /Users/rpeake/.openclaw/workspace/resources/feedly.opml
brief_path: /Users/rpeake/.openclaw/workspace/feedly-digest/brief.md
output_dir: /Users/rpeake/.openclaw/workspace/feedly-digest/
state_file: /Users/rpeake/.openclaw/workspace/feedly-digest/.state.json
log_file: /Users/rpeake/.openclaw/workspace/feedly-digest/.runs.log
output_format: digest-file
mode_label: daily
```

`first_run` is false unless the state file is `{}` or missing.

**OPML parsing** (per spec): top-level `<outline>` per category, inner `<outline type="rss" .../>` per feed. Source ID is `slugify(text)` (lowercase, alphanumeric/hyphen, apostrophes stripped). Mode always `rss`. Tier always `medium`. Tags is `[<parent_category_text>]`.

**Digest-file output:** single markdown file at `<output_dir>/{YYYY-MM-DD}.md`, kept items grouped by tier as bullet entries with title link, source, pubDate, a complete short summary (15–30 words, never truncated mid-word), and the scorer's reason. Omit any tier section with zero items.

**Critical execution requirements** (do not violate):

- `seen_ids` arrays contain real GUIDs/links from parser output. No placeholders, no fabricated UUIDs.
- Every rejected item enumerated by real title with specific criterion in the runs log.
- Zero-item sources logged honestly with parser stderr.
- Cap kept items per run at ~10. The personal digest is a skim, not a backlog. If more than 10 score above reject, raise the bar — keep only the strongest items.

**Brief calibration** (from `feedly-digest/brief.md`): this is personal-interest curation, not protocols research. Score against the brief's criteria for ADHD/wellness substance, woodworking craft-quality, Japanese pedagogy, productivity-system thinking, etc. When unsure between scores, choose lower — Feedly volume is high and noise reaches Robert as missed signal in adjacent surfaces.

**Email delivery — HIGH tier only.** After the digest file is written, create a Gmail draft to `robert@peakepro.com` containing only the HIGH-tier items. Use the available Gmail draft tool (load via ToolSearch with `select:<tool_name>`; the tool name matches `*create_draft` under the Gmail connector). Provide both `body` (plain text) and `htmlBody` (with clickable `<a href>` links) so the rich version renders with hyperlinks while the plain text remains readable.

Email format:

- Subject: `Feedly digest — high-priority items — {YYYY-MM-DD}`
- Header line: count of HIGH items + items-found / sources-processed totals
- One numbered entry per HIGH item with: bold linked title, source · date subline, the 15–30 word summary, and the scorer's reason in muted style
- Footer: pointer to the full digest file path and the run totals (sources processed / items found / flagged / rejected)

If no HIGH items were flagged, do not create a draft — the digest file alone is sufficient. Note this in the runs log.

The Gmail tool creates a draft, not a sent email — it lands in Robert's Drafts folder for him to open and review. That is the intended delivery mechanism.

**Output:** print the run summary block (per skill spec format) at the end, plus a one-line confirmation of the draft creation (or note that no HIGH items were flagged so no draft was created). Do not narrate intermediate work.

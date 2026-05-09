# Spec: Prufrock Protocol Visualisation SPA

## 1. Purpose

A local-first single-page application that renders the output of the simulation engine (`simulation.md`) as an explorable, screen-recordable demo. Target: a compelling 5-minute narrated walkthrough demonstrating the Prufrock Protocol's output, the lineage of lines, and the contrast between cohorts.

The SPA loads a single JSON file (the simulation output) and requires no backend.

## 2. Design principles

- **Demo-first**: every view should look good mid-scroll in a screen recording
- **No login, no setup**: open `index.html`, drop in JSON, explore
- **Narration-friendly**: transitions are smooth, states are URL-addressable (hash routing) so a presenter can bookmark key moments
- **Data-dense but not cluttered**: show the richness of the protocol without overwhelming

## 3. Tech stack

Chosen for maximum AI-agent buildability:

- **Vanilla HTML/CSS/JS** — no build step, no framework overhead
- **D3.js** — lineage graphs, timeline, geographic projections
- **Leaflet** or **D3-geo** — map view with participant locations
- **CSS custom properties** — theming, dark/light mode
- Single `index.html` with inlined or co-located JS/CSS modules (ES modules, no bundler)
- Load simulation JSON via `<input type="file">` or `fetch` from a local path

No React, no Vite, no npm. The SPA should work by opening the HTML file in a browser.

## 4. Views

The SPA has six primary views, navigable via a persistent top bar. Each view has a cohort toggle (Poets / Laypeople / Both) and a day slider (1–14) that filters/animates across all views.

---

### 4.1 Timeline View (default/home)

**What it shows**: The 14-day experiment as a horizontal timeline — one row per collaborative poem.

- X-axis: days 1–14
- Y-axis: poems (rows, 14 per cohort), labelled "Poem 01" through "Poem 14"
- Each cell: the line contributed to that poem on that day, colour-coded by the contributing author
- Colour-coded by:
  - Author (unique colour per poet; legend shown)
  - Forfeits (greyed/crossed out)
- Selecting a poet highlights their authorial trail — the diagonal stripe of cells where they contributed — as the "spine" across all poems
- Click a cell → expands to show: line text, author name, prompt lines received, moment context (time, location, weather), response latency

**Animation**: slide the day slider and watch the poems fill in column by column. Selecting a poet causes their cells to light up across all rows, revealing their distributed authorship in a single glance.

---

### 4.2 Lineage View

**What it shows**: The structure of each collaborative poem as a linear chain, with authorship colour-coded per node.

Each poem is a single vertical chain: seed (2 lines) → Line 1 → Line 2 → … → Line 14. Every node has exactly 2 parents — the two lines immediately preceding it in the same poem. This is not a branching tree; the lineage within a poem is always linear. The branching is authorial: each node is coloured by who wrote it.

- **Default**: show one poem at a time (selector or scroll through all 14)
- **Poem chain layout** (top-down, D3 tree or custom SVG):
  - Seed node (gold, "William Shakespeare — 1609") at root
  - Lines 1–14 as nodes, top to bottom
  - Each node coloured by author, labelled with author initials
  - Node size proportional to line word-count
  - Hover a node → shows full line text, author name, prompt pair received (the two preceding lines), timestamp, location
  - Click a node → highlights that author's full trail across all poems in a side panel
- **Multi-poem overview**: all 14 poem chains rendered as side-by-side thin columns (mini-view), colour-coded by author; reveals the Latin square pattern visually — each row (day) is a permutation of all 14 author colours
- Toggle: show one cohort or overlay both cohorts as parallel columns

**Key demo moment**: select a poet and watch their cells light up — one per poem, one per day — revealing a diagonal stripe across the multi-poem overview. Then switch to a single poem and read it top to bottom, watching the authorial colours change line by line. "No one owns this poem. Fourteen voices built it."

---

### 4.3 Map View

**What it shows**: Geographic distribution of contributions over time.

- World map (Leaflet tiles or D3 natural-earth projection)
- Participant home locations as persistent markers (sized by total contributions)
- As the day slider advances, lines "pulse" from their origin location
- Lines connecting prompt-source location → response location (the geographic journey of the line's parentage)
- Seed poem location marked distinctly (e.g. London for Shakespeare)

**Layers** (toggleable):
- Participant locations only
- Lines of lineage (arcs between locations showing parent→child geography)
- Heatmap of contribution density

**Key demo moment**: animate through all 14 days and watch the lines criss-cross the globe — a visual metaphor for the protocol's distributed authorship.

---

### 4.4 Poem View

**What it shows**: The finished collaborative poems, readable as poetry.

- Select a poem (by number, 1–14) → see its complete 14-line text
- Each line attributed inline: author name (or initials) and author cohort colour appear at the right margin, unobtrusive but readable
- Each line annotated (on hover) with:
  - Author name, location, day written
  - The two prompt lines they received (the line above and the one above that)
  - Response latency
  - Moment context (weather, situational note)
- **Side-by-side mode**: compare the same-numbered poem from the poet cohort vs the layperson cohort — built from the same seed, structured identically, but with completely different contributors and voices
- **Full-cohort mode**: all 14 poems in a scrollable grid, lines aligned by day; authorship shown as colour swatches — reveals the Latin square pattern as a quilted colour grid

**Typography**: clean serif font (e.g. Crimson Text, EB Garamond via Google Fonts), generous line height. Poems should look like poems, not data.

**Key demo moment**: side-by-side Poem 01 from poet cohort vs Poem 01 from layperson cohort — same seed, same lineage structure, 14 different voices each. "The protocol doesn't prescribe craft. It prescribes attention."

---

### 4.5 Participant View

**What it shows**: Deep dive into a single participant — their authorial trail across all 14 poems.

- Profile card (name, location, cohort — biography hidden by default, revealable)
- **Authorial trail**: their 14 contributed lines, one per poem, shown in the order they were written (Day 1 → Day 14). Each line is labelled with which poem it belongs to and what the two prompt lines were. This is the closest thing to "their poem" — a sequence of 14 lines written across 14 different poems over 14 days
- Contribution timeline (14 points on a mini-timeline showing when each interruption landed and when they responded)
- Response latency chart (bar chart, 14 bars — one per contribution)
- Map showing their location and the locations of the 14 prompts they received (from the authors of the preceding lines in each assigned poem)
- **Voice consistency**: their 14 contributed lines shown together as a reading, to assess whether a recognisable voice emerges across unrelated poems
- Link-out: click any line to jump to the full poem it belongs to in Poem View

---

### 4.6 Concerns View

**What it shows**: Each poem — the seed and every collaborative result — is mapped by AI analysis onto a set of universal human concerns. This view makes the thematic inheritance (and occasional divergence) visible across the 14 poems spawned from the seed.

**AI-mapping pipeline**: After each poem is complete (and for the seed text at ingestion time), the simulation engine calls an LLM to assign proportional weights across the nine concern categories. Weights sum to 1.0 per poem and are stored in the simulation JSON alongside the poem text and lineage data. The seed poem's distribution anchors the chart at the left; every heir poem is then compared against it.

**Concern taxonomy** (controlled vocabulary, AI-assigned per poem):

1. Mortality / impermanence
2. Time / aging
3. Love / longing
4. Memory / preservation
5. Wonder / awe
6. Solitude / alienation
7. Domestic life / routine
8. Grief / loss
9. Identity / selfhood

**Two sub-views**:

**Theme river** (default): stacked ribbon chart. X-axis: Seed → Poems 01–14 → projected future (faded). Y-axis: stacked concern proportions. Each concern is a coloured ribbon whose width at each column reflects that poem's AI-assigned weight. The seed anchors the distribution; most heir poems inherit its dominant concerns (Mortality, Time, Love, Memory) and the ribbon landscape stays relatively stable. Occasionally a poem — particularly one where layperson voices accumulate — diverges markedly: the Domestic life or Solitude ribbon swells while Mortality contracts. The right edge fades to imply continuation into the future. This makes the key dynamic visible at a glance: the seed spawns mostly similar-themed poems, but not always.

**Theme network**: bipartite graph. Left column: 14 poem nodes. Right column: 9 concern nodes. Edges connect each poem to the concerns it carries (threshold: weight > 5%); edge thickness and opacity scale with weight. Most poems share the same dense cluster of edges to Mortality, Time, Love, and Memory on the right. A divergent poem's edges pull toward Solitude and Domestic life — its connection pattern visually distinguishes it as an outlier. This view shows inter-poem thematic relationships by revealing which poems share concern profiles (connecting to the same right-hand nodes) and which stand apart.

**Key demo moment**: In the river view, point to the divergent poem's column — the ribbon landscape shifts noticeably. "The protocol didn't prescribe what to write — but the accumulated voices introduced concerns the seed never carried." Switch to the network view: the outlier poem's edges land on different nodes from all other poems.

**Post-experiment idea — theme-based cohort self-selection**: In future open-call editions, participants could browse the concern taxonomy and self-select into a cohort aligned with a theme they feel drawn to (e.g. "Grief / loss", "Domestic life"). This would make concern-divergence intentional and explorable by design, rather than emergent. The Concerns view would then show distinct thematic rivers per self-selected cohort. This is a high-level post-experiment idea not in scope for the current protocol.

---

## 5. Global controls

### Cohort toggle
- Poets / Laypeople / Both
- Affects all views simultaneously
- "Both" uses distinct colour palettes per cohort

### Day slider
- Range: 0 (seed only) → 14
- Animatable: play/pause button auto-advances at ~2 sec/day
- Affects all views: timeline fills, lineage tree grows, map pulses, poems reveal line by line

### Search
- Full-text search across all lines
- Highlights matching lines in whatever view is active

### Seed info
- Persistent small panel (collapsible) showing the historical seed poem, its two prompt lines, author, date, and location

## 6. Data flow

```
simulation JSON
  → parse + validate against expected schema
  → build in-memory indexes:
      - by participant
      - by day
      - by lineage (parent→child)
      - by location
  → render active view
  → URL hash tracks: view + cohort + day + selected participant
```

No data transformation at build time. All indexing happens on JSON load in the browser.

## 7. Visual design

### Colour palette

- Poet cohort: warm tones (amber, terracotta, wine)
- Layperson cohort: cool tones (slate, teal, indigo)
- Seed/historical: gold/antique
- Spine (chosen line): high contrast highlight (white or bright yellow stroke)
- Forfeit: grey, dashed border
- Background: off-white (light mode) / near-black (dark mode)

### Typography

- Headings: sans-serif (e.g. Inter)
- Poem text: serif (e.g. Crimson Text)
- UI/data: monospace for timestamps, sans for labels

### Transitions

- All state changes animate (300ms ease)
- Day slider transitions crossfade content
- Lineage tree nodes enter with a subtle scale-up
- Map arcs draw progressively

## 8. Responsiveness

Desktop-first (this is for screen recording), but the layout should not break at 1024px. Target viewport: 1440×900.

## 9. File structure

```
prufrock-vis/
  index.html              # entry point, all views
  css/
    main.css              # layout, variables, themes
    timeline.css
    lineage.css
    map.css
    poem.css
    participant.css
  js/
    app.js                # router, state, data loading
    data.js               # JSON parsing, indexing
    timeline.js           # timeline view
    lineage.js            # D3 tree view
    map.js                # Leaflet/D3-geo map view
    poem.js               # poem reader view
    participant.js        # participant deep-dive
    concerns.js           # concerns river/chord view
    controls.js           # cohort toggle, day slider, search
  lib/
    d3.min.js             # vendored, no CDN dependency
    leaflet/              # vendored if using Leaflet
  data/
    sim-output.json       # default data file (or loaded via file picker)
```

No build step. Open `index.html` in a browser.

## 10. Screen recording script (suggested 5-min flow)

1. **0:00–0:30** — Open on seed panel. Show Shakespeare's Sonnet 18, highlight lines 11–12. "These two lines — written in 1609 — are the seed. 28 people around the world will each receive a pair of lines from a poem in progress. Their job: write the next line."
2. **0:30–1:30** — Timeline view. Animate day slider 1→14. Watch the grid fill column by column. Select one poet — watch their authorial trail light up as a diagonal stripe across all 14 poems. "Each poet contributes to every poem exactly once. No one owns any poem. Fourteen voices build each one."
3. **1:30–2:30** — Lineage view. Show one poem's chain growing top to bottom. Point to the shifting author colours. Switch to multi-poem overview — the Latin square pattern appears as a colour quilt. "The same structural constraint, 14 times over. Maximum diversity, by design."
4. **2:30–3:30** — Map view. Animate. Watch contribution arcs cross continents as each day's prompts travel from the location of one line to the location of the poet writing the next. "Accra hands to Osaka. Osaka hands to Detroit. Detroit hands to Lisbon. The poem is a record of attention travelling the world."
5. **3:30–4:30** — Poem view. Side-by-side Poem 01 from poet cohort vs Poem 01 from layperson cohort. Read the same-numbered lines from each. "Same seed. Same structural position. Different hands. Different voices. The protocol doesn't prescribe craft. It prescribes attention."
6. **4:30–5:15** — Concerns view. Show the river: mortality and love flowing from Shakespeare 1609 into 2026 responses. Point to where a layperson in São Paulo introduced "solitude" — a concern Shakespeare didn't carry. "The concerns are timeless. The protocol makes that visible. Poets hundreds of years from now will respond to lines written today — and these same concerns will still be there."
7. **5:15–5:30** — Pull back to lineage view, multi-poem overview, both cohorts. "Two communities, one seed, 28 collaborative poems, 392 contributed lines, 14 days. Every line is someone's real moment — or will be, when we run this for real."

## 11. Acceptance criteria

1. Loads simulation JSON and renders all six views without errors
2. Cohort toggle and day slider affect all views consistently
3. Timeline view rows are poems (not participants); selecting a poet highlights their authorial trail across all poem rows
4. Lineage view renders each poem as a linear chain (not a branching tree); every node has exactly 2 parents; nodes are colour-coded by author
5. Multi-poem lineage overview reveals the Latin square authorship pattern visually
6. Map view shows real geographic coordinates; arcs connect the locations of sequential line authors within each poem
7. Poem view renders collaborative poems with per-line author attribution; side-by-side comparison is between two poems (one per cohort), not two participants
8. Participant view shows a poet's authorial trail (14 contributions across 14 different poems) rather than a single-author poem
9. Day slider animation runs smoothly at 2 sec/day with no jank
10. URL hash routing allows bookmarking specific states (view, cohort, day, selected poem, selected poet)
11. Works by opening index.html locally — no server, no build step
12. Screen recording at 1440×900 produces a clean, presentable demo
13. Concerns view renders both the theme river and the theme network from AI-assigned concern weights in simulation data; the seed poem's distribution is visually distinct from heir poems; divergent poems are legible at a glance
14. Clicking a concern in either concerns sub-view filters across all views to show only lines carrying that concern

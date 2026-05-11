# Spec: Experiment 0 — Single-Participant Self-Test of the Daily Interrupt Mechanic

## 0. Purpose

Experiment 0 is an **n=0 self-test**: one participant (Robert), one nominal poem, the existing protocol's `adjacent_pair_rotation` mechanic run against itself, executed over Telegram against state held on Robert's Proxmox slice.

It exists to surface lived-experience friction in the daily-prompt loop — notification timing, prompt phrasing, mobile input ergonomics, the felt experience of being interrupted by a poem — before adding the combinatorial scaffolding of a multi-participant cohort in experiment 1.

It is **not** trying to validate the protocol's combinatorial properties; those are independently testable in simulation. It is trying to validate that the mechanic is *liveable* daily before recruiting other humans into it.

## 1. Protocol semantics

Aligned to the project glossary (`memory/glossary.md`). Terms are used in their existing protocol senses.

### 1.1 Seed

For each new experiment instance:

1. Pick a Shakespearean sonnet at uniform random from the 154-sonnet corpus.
2. Extract lines 12 and 13 (the volta couplet, per glossary definition).
3. These become the **seed pair** `(S₁, S₂)`.

### 1.2 Daily mechanic

Total cycle length: **14 days**. Robert writes 14 lines (`R₁ … R₁₄`). Final assembled poem is 16 lines: `S₁ S₂ R₁ R₂ … R₁₄`.

Let `P` denote the accumulating poem as an ordered list `[S₁, S₂, R₁, …]`.

On day `N` (1 ≤ N ≤ 14):

* **Antithesis** `Π* = (P[N-1], P[N])` — the two most recent lines in the poem at the moment of interrupt.
* **Thesis** — Robert's situated state at the moment of interrupt. Intentionally not captured (per glossary: "the protocol's deliberate negative space").
* **Synthesis** `R_N` — Robert's single-line response, submitted via Telegram reply.

After `R_N` is recorded, append to `P` and advance to day `N+1`.

### 1.3 Protocol invariants in this experiment

| Invariant | Status in experiment 0 |
|---|---|
| `adjacent_pair_rotation` | Honoured. |
| `self-exclusion` | **Suspended** (only one participant). |
| `prompt anonymity` | Moot (only one author; identity is constant). |
| `parent tuple Θ` recording | Honoured. Each `R_N` records `Θ = (hash(P[N-1]), hash(P[N]))`. |
| Append-only ledger 𝓛* | Honoured. Postgres table `responses` is append-only by convention; no `UPDATE` or `DELETE` paths in application code. |
| Ed25519 signing | **Deferred** to experiment 1. Lines are stored unsigned in experiment 0. |
| H3 location anchor | **Deferred** to experiment 1. |

### 1.4 Fire-time scheduling

Each day at 00:01 local time, the scheduler picks a uniform-random minute `t` within Robert's declared waking-hours window `[W_start, W_end]` and schedules the prompt fire for `t`.

Default window: 09:00–22:00 local, configurable per user. If Robert does not reply by `W_end - 30min`, no follow-up nudge is sent in experiment 0 (the experience of missing a day is part of what's being tested).

If a day is missed, the protocol does not advance: day `N` re-fires the next morning with the same antithesis. This preserves the 14-line invariant and lets us observe how recovery feels.

**Scheduling correctness.** When the bot starts mid-day (initial deploy, host reboot, service restart), the random draw must clamp the window start to `max(now, today_at(W_start))` to avoid scheduling a fire in the past. If `now >= today_at(W_end)`, draw from tomorrow's full window instead. APScheduler will silently drop missed-grace-period jobs otherwise — this exact bug ate day 1 of the experiment-0 cycle on 2026-05-11.

### 1.5 Reply discipline

A response is captured by extracting the **first non-blank line** of the Telegram message, after `.strip()`. Subsequent lines in the same message are discarded for the purposes of `R_N` but the **full raw Telegram `Update` payload is persisted** to `responses.raw_update_json` for later analysis.

Rationale: bias toward permissive capture in experiment 0 (no rejection loops, no friction at the moment of synthesis), preserve everything for post-hoc study of how the participant naturally uses the channel. Tighten in later experiments only if the data shows it's needed.

### 1.5 Completion

When `R₁₄` is recorded, the bot delivers the assembled 16-line poem back to Robert as a single message (and persists it to a `completed_poems` view). Experiment 0 ends.

## 2. Stack

| Concern | Choice | Notes |
|---|---|---|
| Language | Python 3.11+ | System Python on Debian 12. Agentic-tooling alignment per the stack decision. |
| Bot framework | `python-telegram-bot` 21.x | Long polling, no inbound exposure. |
| Database | PostgreSQL 16 | With `pgvector` extension preinstalled (unused in exp 0, reserved for later line-similarity work). |
| ORM / migrations | SQLAlchemy 2.x + Alembic | Type-friendly for future agent edits. |
| Scheduler | APScheduler 3.x | In-process; one job per experiment, daily reschedule. |
| Config | `pydantic-settings` v2 | Env-driven, typed. |
| Tests | `pytest`, `pytest-asyncio` | |
| Lint / format | `ruff` (lint + format) | Single tool, agent-friendly. |
| Type check | `pyright` (or `mypy --strict` if preferred) | |
| Process supervision | `systemd` unit on the LXC host | `Restart=on-failure`. |
| Secrets | `.env` file outside the repo, 0600 perms, loaded by `pydantic-settings` | |

No FastAPI / no web framework. There is no inbound HTTP surface in experiment 0.

## 3. Architecture

Single long-lived Python process on the Proxmox LXC container:

```
                    ┌────────────────────────────────────┐
                    │  prufrock.service (systemd)        │
                    │                                    │
                    │  ┌──────────────────────────────┐  │
                    │  │ python-telegram-bot          │  │
                    │  │  · long-poll getUpdates      │──┼──► api.telegram.org
                    │  │  · handle text reply         │  │   (outbound only)
                    │  │  · send_message              │  │
                    │  └──────────────┬───────────────┘  │
                    │                 │                  │
                    │  ┌──────────────▼───────────────┐  │
                    │  │ protocol/arc.py              │  │
                    │  │  · advance state             │  │
                    │  │  · build antithesis          │  │
                    │  └──────────────┬───────────────┘  │
                    │                 │                  │
                    │  ┌──────────────▼───────────────┐  │
                    │  │ APScheduler                  │  │
                    │  │  · 00:01 reseed daily job    │  │
                    │  │  · fire at random t in W     │  │
                    │  └──────────────┬───────────────┘  │
                    │                 │                  │
                    │  ┌──────────────▼───────────────┐  │
                    │  │ SQLAlchemy session           │──┼──► localhost:5432
                    │  └──────────────────────────────┘  │     (Postgres)
                    └────────────────────────────────────┘
```

All network is outbound. No public ingress. Tailscale (optional) is the recommended later path to a personal review surface, not required for the protocol mechanic itself.

## 4. Data model

```sql
-- One participant per row. Experiment 0 has exactly one.
participants(
  id              uuid primary key,
  telegram_user_id   bigint   unique not null,
  telegram_chat_id   bigint   not null,
  display_name       text,
  timezone           text     not null default 'Europe/London',
  waking_start_local time     not null default '09:00',
  waking_end_local   time     not null default '22:00',
  created_at         timestamptz not null default now()
)

-- The 154 Shakespearean sonnets, seeded once at setup.
sonnets(
  id            int primary key,        -- 1..154
  title         text,
  source        text not null,          -- e.g. 'Project Gutenberg #1041'
  full_text     text not null,
  line_12       text not null,
  line_13       text not null
)

-- One row per cycle. Experiment 0 will produce exactly one.
experiments(
  id             uuid primary key,
  participant_id uuid not null references participants(id),
  sonnet_id      int  not null references sonnets(id),
  started_at     timestamptz not null default now(),
  completed_at   timestamptz,
  status         text not null default 'active'
                 check (status in ('active','completed','abandoned'))
)

-- Append-only. One row per fired prompt.
prompts(
  id              uuid primary key,
  experiment_id   uuid not null references experiments(id),
  day_number      int  not null check (day_number between 1 and 14),
  antithesis_a    text not null,        -- P[N-1]
  antithesis_b    text not null,        -- P[N]
  scheduled_for   timestamptz not null,
  fired_at        timestamptz,
  telegram_message_id bigint,
  unique (experiment_id, day_number)
)

-- Append-only. One row per received synthesis.
responses(
  id              uuid primary key,
  prompt_id       uuid not null references prompts(id),
  text            text not null,
  parent_hash_a   text not null,        -- sha256(antithesis_a)
  parent_hash_b   text not null,        -- sha256(antithesis_b)
  received_at     timestamptz not null default now(),
  raw_update_json jsonb not null        -- full Telegram Update payload, audit trail
)

-- View, not table: the assembled poem so far for an experiment.
-- Convenience for the day-N+1 antithesis lookup and final delivery.
create view poem_state as
  select e.id as experiment_id,
         array[s.line_12, s.line_13]
           || array_agg(r.text order by p.day_number) as lines
    from experiments e
    join sonnets s on s.id = e.sonnet_id
    left join prompts p on p.experiment_id = e.id
    left join responses r on r.prompt_id = p.id
   group by e.id, s.line_12, s.line_13;
```

Conventions:

* `responses` is append-only by application contract — no `UPDATE` / `DELETE` codepaths.
* `responses.raw_update_json` preserves the full Telegram payload as audit / provenance, including message timestamps and any future-relevant metadata (location, media, etc.) that the protocol may consume in later experiments.
* `parent_hash_a/b` are stored even though Ed25519 signing is deferred; the hashes lay the groundwork for the parent-tuple `Θ` once signing comes in.

## 5. Repo layout

```
prufrock-experiment0/
├── pyproject.toml
├── README.md                       ← run-it instructions for Robert
├── .env.example
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
│       └── 0001_initial.py
├── src/prufrock/
│   ├── __init__.py
│   ├── config.py                   ← pydantic-settings
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py               ← SQLAlchemy ORM
│   │   └── session.py
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── handlers.py             ← /start, message reply handler
│   │   └── runner.py               ← entry point, Application.run_polling()
│   ├── scheduler/
│   │   ├── __init__.py
│   │   ├── fire_window.py          ← random time within waking hours
│   │   └── tasks.py                ← daily reseed job, fire job
│   ├── protocol/
│   │   ├── __init__.py
│   │   ├── arc.py                  ← advance state, build antithesis
│   │   └── voltas.py               ← sonnet picker, seed extraction
│   └── cli.py                      ← typer CLI for ops (seed-sonnets, start-experiment, etc.)
├── data/
│   └── shakespeare_sonnets.json    ← seeded into the sonnets table
├── deploy/
│   ├── prufrock.service            ← systemd unit
│   └── postgres-init.sql           ← extension + role setup
└── tests/
    ├── test_arc.py                 ← antithesis construction, state advance
    ├── test_fire_window.py         ← random-time generation in window
    ├── test_voltas.py              ← line 12/13 extraction
    └── conftest.py                 ← fixtures, ephemeral pg via testcontainers
```

## 6. Voltas dataset and sonnet selection

### 6.1 Source

Project Gutenberg #1041 (Shakespeare's Sonnets), public domain.

### 6.2 Generation pipeline

One-time, scripted in `cli.py seed-sonnets`:

1. Fetch the plain-text Gutenberg file.
2. Strip header/footer boilerplate.
3. Segment into 154 sonnets using the Roman-numeral headings.
4. For each sonnet: normalise whitespace, drop blank lines, assert exactly 14 lines (sonnets that fail this assertion go to a review queue — sonnet 99 has 15 lines and sonnet 126 has 12; handle both as documented exceptions).
5. Extract `line[11]` and `line[12]` (zero-indexed) → `line_12`, `line_13`.
6. Persist as JSON to `data/shakespeare_sonnets.json`.
7. Loader CLI command reads JSON and inserts into `sonnets` table idempotently.

### 6.3 Exception handling

* Sonnet 99 (15 lines): drop the opening single line, use lines 12–13 of the remaining 14.
* Sonnet 126 (12 lines, no closing couplet): **exclude** from the pool. Document the exclusion in the data file. The random picker filters with `WHERE id != 126`.

### 6.4 Selection rule — "always fresh"

Each new experiment for a given participant draws a sonnet uniformly at random from the set of sonnets that participant has **not yet been seeded with in any prior experiment** (excluding 126 always).

```sql
SELECT id FROM sonnets
 WHERE id != 126
   AND id NOT IN (
     SELECT sonnet_id FROM experiments
      WHERE participant_id = :participant_id
   )
 ORDER BY random() LIMIT 1;
```

If the participant has exhausted all 153 available sonnets, reset by allowing the full pool again and emit a `journal.info` log line noting the wrap. (In practice, with 153 sonnets and a once-per-fortnight cycle, this is ~6 years away; the wrap behaviour exists for correctness, not because it'll fire soon.)

For experiment 0 this rule is a no-op (the participant has no prior experiments), but having the rule live in `arc.start_experiment` from day one means future cycles inherit it for free.

## 7. Setup steps for Robert (Proxmox-side, manual)

These run on Robert's side before Claude Code starts the build, or in parallel with it.

### 7.1 LXC container

1. From the Proxmox web UI, create a new LXC container:
   * **Template**: `debian-12-standard`
   * **Hostname**: `prufrock`
   * **Cores**: 2
   * **RAM**: 2 GiB
   * **Disk**: 10 GiB
   * **Network**: bridged on the internal LAN, DHCP or a static reservation
   * **Unprivileged**: yes
   * **Features**: `nesting=1` (only if you choose the docker-compose Postgres path)
2. Start the container, log in as root.

### 7.2 Base packages

```bash
apt update && apt -y upgrade
apt -y install build-essential git curl ca-certificates \
                python3.12 python3.12-venv python3-pip \
                postgresql-16 postgresql-16-pgvector \
                systemd-timesyncd
timedatectl set-timezone Europe/London  # adjust if travelling
```

### 7.3 Unprivileged service user

```bash
adduser --disabled-password --gecos "" prufrock
mkdir -p /opt/prufrock
chown prufrock:prufrock /opt/prufrock
```

### 7.4 Postgres role and database

```bash
sudo -u postgres psql <<SQL
  CREATE ROLE prufrock LOGIN PASSWORD 'CHANGE_ME';
  CREATE DATABASE prufrock OWNER prufrock;
  \c prufrock
  CREATE EXTENSION IF NOT EXISTS pgvector;
SQL
```

Note the password; it goes into `.env` as `DATABASE_URL`.

### 7.5 Telegram bot

1. Open Telegram → message **@BotFather** → `/newbot` → follow prompts.
2. Save the bot token (format `123456789:ABC...`).
3. Message your new bot once (`/start` or any text) so it has a chat with you.
4. Message **@userinfobot** → it replies with your numeric Telegram user ID. Save it.

### 7.6 Tailscale (optional, deferred until you want a review dashboard)

Skip for experiment 0. Future experiments may add a localhost-only web review surface reachable over Tailscale; nothing in the protocol mechanic itself needs it.

### 7.7 Deploy

After Claude Code finishes the build:

```bash
sudo -u prufrock -i
cd /opt/prufrock
git clone <repo-url> .
python3.12 -m venv .venv
.venv/bin/pip install -e .
cp .env.example .env
# edit .env: DATABASE_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID, TIMEZONE
.venv/bin/alembic upgrade head
.venv/bin/prufrock seed-sonnets data/shakespeare_sonnets.json
.venv/bin/prufrock start-experiment --participant-telegram-id <your-id>
exit
sudo cp /opt/prufrock/deploy/prufrock.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now prufrock.service
sudo journalctl -u prufrock.service -f
```

## 8. Implementation tasks for Claude Code (ordered)

Build in this sequence. Each step should be independently runnable and testable before moving on.

1. **Scaffold** the repo per §5. `pyproject.toml` with dependencies pinned to minor versions. `ruff` and `pyright` configured. `.env.example` with every required var documented.
2. **Config** (`config.py`) — `pydantic-settings` `Settings` class reading `DATABASE_URL`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_USER_ID`, `TIMEZONE`, `LOG_LEVEL`. Fail loudly on missing required vars.
3. **DB layer** — SQLAlchemy 2.x declarative models per §4. Alembic init + initial migration `0001_initial.py`. **Do not** include `CREATE EXTENSION vector` in the default migration: pgvector is unused in experiment 0 and breaks `alembic upgrade head` on any cluster that doesn't already have the extension package installed (e.g. Debian's stock `postgresql-15`). If pgvector becomes needed later, add a separate optional migration gated by a config flag, or install `postgresql-15-pgvector` from PGDG ahead of running migrations.
4. **Sonnet ingestion** — `voltas.py` + `cli seed-sonnets` command. Idempotent. Includes the §6 exception handling for sonnets 99 and 126.
5. **Protocol layer** — `arc.py`:
   * `start_experiment(participant) -> Experiment` — picks a random sonnet (excluding 126), creates the experiment row, returns it.
   * `build_antithesis(experiment, day_number) -> tuple[str, str]` — reads `poem_state` view, returns `(P[N-1], P[N])`.
   * `record_response(prompt, text, raw_update) -> Response` — appends to `responses`, computes parent hashes, advances state (i.e. clears the active prompt and schedules tomorrow's).
   * `is_complete(experiment) -> bool` — true when 14 responses are recorded.
   * `assemble_poem(experiment) -> str` — returns the 16-line text for final delivery.
6. **Scheduler** — `fire_window.py` for the random-time-in-window logic. Use `secrets.SystemRandom` not `random` for the draw. **Clamp the draw to `[max(now, today_at(W_start)), today_at(W_end)]`** per §1.4 so mid-day startups don't pick past times; if `now >= today_at(W_end)`, draw from tomorrow's full window instead. `tasks.py` for the APScheduler jobs: a daily `00:01` reseed that books the day's fire time, and the fire job itself that calls into `arc.build_antithesis` and dispatches via the bot.
7. **Bot** — `handlers.py` with two handlers:
   * `/start` — registers / acknowledges the participant.
   * Default message handler — treats any text from the registered chat as a response to the open prompt for the participant's active experiment. Validates there is an open prompt; rejects silently with a polite reply otherwise.

   `runner.py` builds the `Application`, attaches handlers, kicks off the APScheduler, calls `run_polling()`.
8. **CLI** — `typer`-based, exposing `seed-sonnets`, `start-experiment`, `status` (prints current experiment state and assembled poem so far), `abandon-experiment`, `fire-now` (manual day-N fire for smoke testing). In any command that prints summary output, **capture ORM field values to locals inside the `with db_session() as session:` block** before the session closes, or set `expire_on_commit=False` on the session. Accessing ORM attributes after session close raises `DetachedInstanceError` even when the underlying commit succeeded.
9. **Tests** — at minimum:
   * `test_arc.py`: 14-day end-to-end with a stubbed bot, verifying antithesis pairs match the adjacent-pair rule.
   * `test_fire_window.py`: distribution check on `secrets.SystemRandom` draws within window.
   * `test_voltas.py`: parse a fixture Gutenberg file, assert all 154 sonnets handled correctly including 99 and 126 exceptions.
   * `conftest.py`: ephemeral Postgres via `testcontainers` if available; fall back to a `pytest --pg-url` flag pointing at a local test DB.
10. **systemd unit** — `deploy/prufrock.service`. `Type=simple`, `Restart=on-failure`, `RestartSec=10`, `User=prufrock`, `WorkingDirectory=/opt/prufrock`, `EnvironmentFile=/opt/prufrock/.env`, `ExecStart=/opt/prufrock/.venv/bin/prufrock-bot`.
11. **README.md** — Robert-facing run-it instructions, including the §7 setup checklist and troubleshooting (bot not receiving, scheduler not firing, etc.).

## 9. Acceptance criteria

Experiment 0 is shippable when:

1. `alembic upgrade head` produces the schema in §4 cleanly on a fresh DB.
2. `prufrock seed-sonnets` populates 153 sonnets (excluding 126) idempotently from `data/shakespeare_sonnets.json`.
3. `prufrock start-experiment` creates an active experiment for the registered participant with a randomly chosen sonnet.
4. The bot, run under `systemctl`, can be messaged from Telegram and responds to `/start`.
5. The scheduler fires a prompt within the configured window each day, in the form:

       > Day 3 of 14.
       >
       > S₂ R₁
       >
       > Continue.

   …delivered as a Telegram message, with `(antithesis_a, antithesis_b)` matching `(P[N-1], P[N])`.
6. A Telegram reply during an open prompt is persisted to `responses` with full `raw_update_json` and correct `parent_hash_a/b`.
7. After `R₁₄` is recorded, the bot delivers the assembled 16-line poem.
8. Pytest suite passes; ruff and pyright clean.
9. Nothing in the deployment requires public HTTPS, port forwarding, or inbound exposure of any kind.
10. A simulated 14-day run (scheduler accelerated to fire-every-minute for testing) completes end-to-end without manual intervention.

## 10. Out of scope (defer to experiment 1+)

* Multi-participant cohorts, assignment matrix 𝒜, Latin rectangle balancing.
* Ed25519 signing of contributions.
* H3 location anchors.
* Public-key registration / `prompt anonymity` enforcement.
* Hash-commit / reveal of the assignment matrix.
* Anything Anthropic-API-backed (line analysis, prompt synthesis, generated commentary). The infrastructure is forward-compatible but unused.
* Web dashboard / review surface. Robert reads state via `prufrock status` over SSH for experiment 0.
* Embeddings / similarity / pgvector usage. The extension is installed but no embedding is computed.
* Notification redundancy, missed-day nudges, retry logic beyond `systemd` process restart.
* Sources beyond Shakespeare 154. Petrarchan-volta extraction (lines 8–9) is the obvious next source but not in scope here.

## 11. Decisions log

### Previously open questions, closed 2026-05-11

1. **Sonnet selection across experiments — always fresh.** Per §6.4, each new experiment draws from the set of sonnets the participant has not been seeded with before (excluding 126). Wrap to the full pool when exhausted.
2. **Reply discipline — permissive capture, raw preservation.** Per §1.5, the first non-blank line of the Telegram message is captured as `R_N`; the full raw `Update` payload is preserved in `responses.raw_update_json` for later analysis.

### Deploy learnings, recorded 2026-05-11

Three bugs surfaced during the actual experiment-0 deploy on `peake`. All three were patched in place to unblock the cycle; the spec amendments above lock the fixes in for any future build. Deferred for code-level fix until after the 14-day cycle (do not touch the running daemon).

1. **Scheduler did not clamp the draw window to `now`** (`scheduler/fire_window.py`). On the initial deploy at 19:01 BST, the scheduler drew 15:43 BST — already in the past — and APScheduler dropped the job after the misfire grace period. Day 1 of the live cycle was lost this way. The protocol's missed-day recovery (§1.4) re-books day 1 on the next 00:01 reseed, so the cycle is intact but extended by one calendar day. Spec §1.4 and §8 task 6 amended.
2. **`start_experiment` raised `DetachedInstanceError` after a successful commit** (`cli.py:179`). Echoing ORM attributes after the `with db_session()` block closes triggers an expired-attribute refresh against a non-existent session. Cosmetic — the DB state was correctly committed before the echo failed. Spec §8 task 8 amended.
3. **Default Alembic migration broke on a cluster without pgvector.** SPEC.md §4 originally instructed `CREATE EXTENSION vector` in `0001_initial.py`. This breaks `alembic upgrade head` if the extension files aren't on disk, even with `IF NOT EXISTS` (which only handles "already present", not "package missing"). Hand-patched out of the migration on this slice. Spec §8 task 3 amended to drop the extension creation from the default migration.

### Reference

Operator-facing setup is in [SETUP.md](./SETUP.md). §7 in this spec is the abbreviated reference; SETUP.md is the runbook.

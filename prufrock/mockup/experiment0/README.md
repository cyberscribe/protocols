# Prufrock Experiment 0

Single-participant self-test of the daily-interrupt mechanic. One person (Robert), one Shakespearean sonnet, 14 days, one line per day submitted via Telegram. Full run-it instructions are in [SETUP.md](SETUP.md); this file is the quick-start for once the Proxmox LXC is provisioned.

## Slice state (2026-05-11)

Currently deployed on the `prufrock` LXC on Robert's Proxmox slice:

- `prufrock.service` running under `systemd`, long-polling Telegram. No inbound HTTP.
- PostgreSQL 16 on `localhost:5432`, UTF-8, owned by the `prufrock` role — co-tenanted with the existing `iot` database and `iot-telemetry` service on the same cluster.
- `pgvector` is **not** installed on this slice; `alembic/versions/0001_initial.py` was hand-patched to remove `CREATE EXTENSION vector`. The spec retains pgvector forward-compatibility for experiment 1+ — see [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md).
- Tailscale is up; `prufrock status` and `journalctl` reads are reachable from anywhere.

Experiment `b35f4d95-d549-46a0-9e35-4605037609ba` is active: sonnet 96, day 1 of 14, 0 responses recorded. Day 1 was deferred (start at 19:01 BST after the random window had already drawn 15:43 BST); the 00:01 daily reseed will re-book day 1 for tomorrow per `SPEC.md` §1.4. Operating posture during the 14-day cycle is **observation only** — see [`journal/experiment0.md`](journal/experiment0.md) for meta-observations and [`KNOWN_ISSUES.md`](KNOWN_ISSUES.md) for the three deferred bugs.

## Prerequisites

- Debian 12 LXC container running on Proxmox (see `SETUP.md` §1–3)
- PostgreSQL 16 (§4 — `postgresql-16-pgvector` only required for forward-compatibility with experiment 1+; not used by experiment 0)
- A Telegram bot token and your numeric user ID (§6)

## Quick start

```bash
# Clone and install
cd /opt/prufrock
git clone <repo-url> .
python3 -m venv .venv
.venv/bin/pip install -e .

# Configure
cp .env.example .env
chmod 600 .env
nano .env          # fill in DATABASE_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_USER_ID

# Migrate
.venv/bin/alembic upgrade head

# Seed sonnets (fetches from Project Gutenberg on first run)
.venv/bin/prufrock seed-sonnets data/shakespeare_sonnets.json

# Register yourself
.venv/bin/prufrock register-participant \
    --telegram-user-id <your-id> \
    --telegram-chat-id <your-id> \
    --display-name "Robert"

# Start the experiment
.venv/bin/prufrock start-experiment

# Install and start the systemd service
sudo cp deploy/prufrock.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now prufrock.service

# Verify
sudo journalctl -u prufrock.service -f
```

Then, from Telegram, send `/start` to your bot. The first prompt will arrive at a random time within today's waking-hours window.

## CLI reference

| Command | Description |
|---|---|
| `prufrock seed-sonnets <path>` | Load sonnets from JSON into DB (idempotent). Add `--regenerate` to refetch from Gutenberg. |
| `prufrock register-participant` | Register the Telegram user. |
| `prufrock start-experiment` | Begin a new 14-day cycle. |
| `prufrock status` | Print the assembled poem so far and the current day. |
| `prufrock fire-now` | Immediately fire today's prompt (smoke test). |
| `prufrock abandon-experiment` | Mark the current experiment as abandoned. |
| `prufrock export --experiment-id <uuid>` | Dump the full experiment record to JSON. |

## Running tests

```bash
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest                             # uses testcontainers (Docker required)
.venv/bin/pytest --pg-url postgresql+psycopg://prufrock:pw@127.0.0.1/prufrock_test
```

Tests that hit the database spin up an ephemeral Postgres 16 container via `testcontainers`. If Docker is not available, pass `--pg-url` pointing at a local test database.

Tests that do not need a database (`test_fire_window.py`, `test_voltas.py`) run without any external services.

## Operations

```bash
# Logs
journalctl -u prufrock.service -f
journalctl -u prufrock.service --since today

# Check state
.venv/bin/prufrock status

# Restart
systemctl restart prufrock.service

# Update
git pull && .venv/bin/pip install -e . && .venv/bin/alembic upgrade head
systemctl restart prufrock.service
```

## Troubleshooting

**Bot not receiving messages** — check `systemctl status prufrock.service` and confirm `curl -s https://api.telegram.org/bot<TOKEN>/getMe` returns your bot's profile. If you previously set a webhook, clear it: `curl -s https://api.telegram.org/bot<TOKEN>/deleteWebhook`.

**Scheduler never fires** — check `TIMEZONE`, `WAKING_START_LOCAL`, `WAKING_END_LOCAL` in `.env`. Verify the LXC clock: `date`. Run `prufrock fire-now` to bypass the scheduler entirely.

**Postgres connection refused** — check `systemctl status postgresql` and `ss -lntp | grep 5432`. See `SETUP.md` §4 for the `pg_hba.conf` fix if you get peer-auth errors.

**Sonnet seeding fails** — run `prufrock seed-sonnets --regenerate data/shakespeare_sonnets.json` to refetch from Gutenberg. If the Gutenberg file format has drifted, check the parser in `src/prufrock/protocol/voltas.py`.

## Architecture

Single long-lived Python process under `systemd`:

- `python-telegram-bot` 21 (long-poll, outbound only — no inbound HTTP)
- `APScheduler` 3.x `AsyncIOScheduler` in the same event loop
- `SQLAlchemy` 2 + `Alembic` against PostgreSQL 16 on `localhost`
- `pydantic-settings` v2 reading all config from `.env`

Nothing listens on a public port. Tailscale (optional) is the recommended path to off-LAN SSH access.

## What is out of scope here

Ed25519 signing, H3 location anchors, multi-participant cohorts, web dashboard, embeddings/pgvector usage, and everything else deferred to experiment 1+. See `SPEC.md §10`.

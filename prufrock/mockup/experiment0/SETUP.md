# Setup Runbook: Experiment 0 on Proxmox

Operator-facing runbook for Robert. Walks through provisioning a Debian 12 LXC container on the Proxmox slice, installing Postgres 16 with pgvector, preparing the Python environment, creating the Telegram bot, and (after Claude Code finishes the build) deploying and running the experiment under `systemd`.

Estimated time: **~30–45 minutes** end to end, of which maybe 10 is actual typing.

## Variant: deploying onto the existing container 101 (`peake`)

For the actual experiment-0 deployment, Robert is repurposing the existing Debian 12 LXC (formerly `iot`, renamed to `peake`) which already has Postgres 15 running alongside an `iot-telemetry` Flask app and nginx. The following stages of the canonical runbook below are **skipped or modified** for this deployment:

| Stage | Status for the `peake` deployment |
|---|---|
| §1 Create the LXC container | **Skip.** Container 101 exists. |
| §2 Base system | **Skip.** Already provisioned; only the hostname rename `iot` → `peake` is needed. |
| §3 Tailscale | Optional but recommended; install as written. |
| §4 PostgreSQL 16 with pgvector | **Modified.** Stay on existing Postgres 15. Skip pgvector entirely for experiment 0 (unused). When creating the `prufrock` database, **explicitly use UTF-8 from `template0`** because the cluster is initialised as `SQL_ASCII`: `CREATE DATABASE prufrock OWNER prufrock ENCODING 'UTF8' LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0;` |
| §5 Service user and directory | **Apply as written.** |
| §6 Create the Telegram bot | **Apply as written.** |
| §7 Deploy the application | **Apply as written.** |
| §8 Smoke test | **Apply as written.** |
| Operations | **Apply as written.** |

Coexistence notes:

* The `prufrock` Postgres role/DB are separate from the existing `iot` role/DB. No permission overlap, no port conflict (both share localhost:5432).
* The prufrock bot uses no inbound ports (long polling), so does not conflict with nginx (:80), iot-telemetry (:5000), or openclaw-gateway (:18789–18791).
* Memory: bumped from 2 GiB to 4 GiB during deploy because Claude Code's native installer was OOM-killed at 2 GiB. 4 GiB has comfortable headroom for the bot, iot-telemetry, Postgres, and a Claude Code session running concurrently.
* Tailscale required loading the `tun` kernel module on the Proxmox host and bind-mounting `/dev/net/tun` into the unprivileged LXC via `/etc/pve/lxc/101.conf`. The two `lxc.cgroup2.devices.allow` and `lxc.mount.entry` lines must live in the **active config section** (above any `[snapshot-name]` header), or they are silently ignored.

### Actual deploy outcome (2026-05-11)

What got built diverged from the canonical fresh-LXC runbook below in three ways. None of these are wrong; they're documented here so the next deployer knows what to expect.

1. **Install location:** the repo was cloned to `/home/prufrock/protocols/prufrock/mockup/experiment0/` (inside the 00-protocols workspace clone, so spec and code stay colocated) rather than `/opt/prufrock`. The systemd unit was repathed accordingly via `sed -i 's|/opt/prufrock|/home/prufrock/protocols/prufrock/mockup/experiment0|g' deploy/prufrock.service` before installation. Functionally equivalent; just non-canonical.
2. **Migration patched in place:** the initial Alembic migration was generated with `CREATE EXTENSION vector` per SPEC.md §4 (now fixed in spec, see §11 deploy learnings). It was hand-patched out before `alembic upgrade head` succeeded: `sed -i '/# pgvector extension/d;/CREATE EXTENSION.*vector/d' alembic/versions/0001_initial.py`. The next build from spec won't need this patch.
3. **Day 1 fire dropped** by the scheduler bug logged in SPEC.md §11. The protocol's missed-day recovery handles it; day 1 re-fires on the next 00:01 reseed.

The canonical fresh-LXC runbook follows below for the general case and for reference.

## Conventions used below

* Commands prefixed `pve#` are run on the **Proxmox host** (as root).
* Commands prefixed `prufrock#` are run **inside the LXC** as root.
* Commands prefixed `prufrock$` are run **inside the LXC** as the `prufrock` service user.
* Anything in `<angle brackets>` is a placeholder to substitute.
* "Verify" blocks tell you what success looks like before moving on.

---

## Stage 0 — Prerequisites

You need:

* Proxmox VE access with permission to create unprivileged LXC containers.
* A Debian 12 (bookworm) LXC template downloaded on the Proxmox host. If you don't have one:

  ```
  pve# pveam update
  pve# pveam available | grep debian-12
  pve# pveam download local debian-12-standard_12.7-1_amd64.tar.zst
  ```

  (The exact version suffix will shift over time — pick the most recent `debian-12-standard`.)

* A Telegram account on your phone.
* About 10 GiB free on your Proxmox storage pool.

---

## Stage 1 — Create the LXC container

### 1.1 Via the Proxmox web UI

1. In the Proxmox UI, click **Create CT** (top right).
2. **General**:
   * **Node**: your slice's node.
   * **CT ID**: pick an unused ID (e.g. 200).
   * **Hostname**: `prufrock`
   * **Unprivileged container**: **checked** (default).
   * **Password**: set a strong root password — you'll only use it for emergencies; SSH key login below replaces it.
   * **SSH public key(s)**: paste your laptop's public key. (`cat ~/.ssh/id_ed25519.pub` on your laptop.)
3. **Template**: pick the `debian-12-standard` template you downloaded in Stage 0.
4. **Disks**:
   * **Storage**: whichever pool you usually use.
   * **Disk size**: 10 GiB.
5. **CPU**: 2 cores.
6. **Memory**: 2048 MiB RAM, 512 MiB swap.
7. **Network**:
   * **Bridge**: your internal bridge (usually `vmbr0`).
   * **IPv4**: DHCP, or static if you prefer a fixed address. A reservation in your router/DHCP server is easiest.
   * **IPv6**: as you prefer.
8. **DNS**: leave on host defaults.
9. **Confirm** → **Finish**, but **do not** tick "Start after created" yet.

### 1.2 Adjust container options before first boot

Unprivileged containers default to safe settings; we don't need nesting or device passthrough for this build. Leave defaults.

### 1.3 Start and shell in

```
pve# pct start <CTID>
pve# pct enter <CTID>
```

You're now at a root prompt inside the container.

### Verify

```
prufrock# cat /etc/os-release | head -2
# Expect: PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"

prufrock# ip -4 addr show eth0
# Expect: an inet address on your LAN.

prufrock# ping -c 2 api.telegram.org
# Expect: 0% packet loss.
```

If the network ping fails, fix that before continuing — the bot needs outbound HTTPS to `api.telegram.org`.

---

## Stage 2 — Base system

### 2.1 Update, set timezone, install baseline packages

```
prufrock# apt update && apt -y full-upgrade
prufrock# apt -y install \
    ca-certificates curl gnupg lsb-release \
    git build-essential \
    python3 python3-venv python3-pip python3-dev \
    libpq-dev \
    systemd-timesyncd \
    ufw \
    sudo

prufrock# timedatectl set-timezone Europe/London
# (Substitute your timezone if different. Use `timedatectl list-timezones` to find it.)

prufrock# systemctl enable --now systemd-timesyncd
```

### 2.2 Hostname and hosts file

```
prufrock# hostnamectl set-hostname prufrock
prufrock# grep -q prufrock /etc/hosts || \
    echo "127.0.1.1 prufrock" >> /etc/hosts
```

### 2.3 SSH hardening (optional but recommended)

Edit `/etc/ssh/sshd_config` to disable password login (you've already added an SSH key):

```
prufrock# sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
prufrock# systemctl restart ssh
```

### 2.4 Firewall (optional but recommended)

Since the bot is outbound-only, the only inbound port we need is SSH (22). If you set up Tailscale in Stage 3, you can scope SSH to the Tailscale interface and close 22 on the LAN side entirely.

```
prufrock# ufw default deny incoming
prufrock# ufw default allow outgoing
prufrock# ufw allow 22/tcp
prufrock# ufw --force enable
```

### Verify

```
prufrock# python3 --version
# Expect: Python 3.11.x

prufrock# timedatectl
# Expect: Local time and timezone correct, "System clock synchronized: yes"
```

---

## Stage 3 — (Optional) Tailscale for off-LAN access

Skip this stage if you only want LAN access. Strongly recommended if you want to `ssh prufrock` or run `prufrock status` from your phone or laptop when not at home.

```
prufrock# curl -fsSL https://tailscale.com/install.sh | sh
prufrock# tailscale up --ssh
# Follow the printed URL on your laptop/phone to authenticate the node.
```

After this completes, `tailscale status` shows the node's Tailscale IP. SSH in from anywhere via:

```
your-laptop$ tailscale ssh root@prufrock
```

---

## Stage 4 — Install PostgreSQL 16 with pgvector

We use the PGDG (PostgreSQL Global Development Group) apt repo because it ships pgvector packages for every supported Postgres version, which Debian's main repo does not for Postgres 16.

### 4.1 Add the PGDG repo

```
prufrock# install -d /etc/apt/keyrings
prufrock# curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    | gpg --dearmor -o /etc/apt/keyrings/postgresql.gpg
prufrock# echo "deb [signed-by=/etc/apt/keyrings/postgresql.gpg] \
    http://apt.postgresql.org/pub/repos/apt bookworm-pgdg main" \
    > /etc/apt/sources.list.d/pgdg.list
prufrock# apt update
```

### 4.2 Install

```
prufrock# apt -y install postgresql-16 postgresql-16-pgvector
prufrock# systemctl enable --now postgresql
```

### 4.3 Create the role and database

Pick a strong password (e.g. `openssl rand -base64 24`). Note it — it goes into `.env` in Stage 7.

```
prufrock# sudo -u postgres psql <<'SQL'
  CREATE ROLE prufrock LOGIN PASSWORD 'REPLACE_WITH_GENERATED_PASSWORD';
  CREATE DATABASE prufrock OWNER prufrock;
  \c prufrock
  CREATE EXTENSION IF NOT EXISTS vector;
SQL
```

### Verify

```
prufrock# sudo -u postgres psql -d prufrock -c \
    "SELECT extname, extversion FROM pg_extension WHERE extname='vector';"
# Expect: one row, vector | <some version>.

prufrock# PGPASSWORD='<the password>' \
    psql -h 127.0.0.1 -U prufrock -d prufrock -c '\conninfo'
# Expect: "You are connected to database 'prufrock' as user 'prufrock' ..."
```

If the second command fails with a peer-auth error, edit `/etc/postgresql/16/main/pg_hba.conf`, find the line:

```
local   all             all                                     peer
```

and add above it:

```
host    prufrock        prufrock        127.0.0.1/32            scram-sha-256
```

Then `systemctl reload postgresql` and retry. (PGDG defaults usually have this right out of the box; this is just-in-case.)

---

## Stage 5 — Service user and directory

```
prufrock# adduser --disabled-password --gecos "" prufrock
prufrock# install -d -o prufrock -g prufrock /opt/prufrock
prufrock# install -d -o prufrock -g prufrock /var/log/prufrock
prufrock# install -d -o prufrock -g prufrock /var/backups/prufrock
```

### Verify

```
prufrock# ls -ld /opt/prufrock /var/log/prufrock /var/backups/prufrock
# All three should be owned by prufrock:prufrock.
```

---

## Stage 6 — Create the Telegram bot

On your phone (or Telegram Desktop):

### 6.1 Create the bot

1. Open Telegram, search for **@BotFather**, start a chat.
2. Send `/newbot`.
3. **Name**: something human-readable, e.g. `Prufrock (n=0)`.
4. **Username**: must end in `bot`, e.g. `prufrock_n0_bot` (must be globally unique on Telegram).
5. BotFather replies with a message containing your **HTTP API token** in the format:

   ```
   1234567890:AAH...verylongstring...
   ```

   **Save this.** It's the `TELEGRAM_BOT_TOKEN` for `.env`.

6. Optional polish (also via @BotFather):
   * `/setdescription` — describe what the bot does for your own future reference.
   * `/setuserpic` — upload a picture (perhaps the protocol-diagram).
   * `/setcommands` — register `start - Initialize the experiment`. (Optional — the bot is single-user.)

### 6.2 Open a chat with your bot

Search for your bot by its `@username`, tap **Start**, send any message. This creates the chat the bot will message you on.

### 6.3 Get your numeric Telegram user ID

Search for **@userinfobot** in Telegram, start a chat, send any message. It replies with your numeric `Id` field. Save it. This is `TELEGRAM_USER_ID` for `.env`.

### Verify

You now have two secrets:

```
TELEGRAM_BOT_TOKEN=1234567890:AAH...
TELEGRAM_USER_ID=<your numeric ID>
```

Keep them somewhere safe (your password manager) until Stage 7.

---

## Stage 7 — Deploy the application

This stage assumes Claude Code has produced the repo described in SPEC.md §5 and you've pushed it somewhere you can `git clone` from (GitHub, your own Gitea, etc.).

### 7.1 Clone and install

```
prufrock# su - prufrock
prufrock$ cd /opt/prufrock
prufrock$ git clone <repo-url> .
prufrock$ python3 -m venv .venv
prufrock$ .venv/bin/pip install --upgrade pip
prufrock$ .venv/bin/pip install -e .
```

### 7.2 Configure environment

```
prufrock$ cp .env.example .env
prufrock$ chmod 600 .env
prufrock$ nano .env
```

Fill in:

```dotenv
DATABASE_URL=postgresql+psycopg://prufrock:<db-password>@127.0.0.1:5432/prufrock
TELEGRAM_BOT_TOKEN=<from Stage 6.1>
TELEGRAM_USER_ID=<from Stage 6.3>
TIMEZONE=Europe/London
WAKING_START_LOCAL=09:00
WAKING_END_LOCAL=22:00
LOG_LEVEL=INFO
```

### 7.3 Run migrations

```
prufrock$ .venv/bin/alembic upgrade head
```

### Verify

```
prufrock$ PGPASSWORD='<db-password>' \
    psql -h 127.0.0.1 -U prufrock -d prufrock -c '\dt'
# Expect tables: participants, sonnets, experiments, prompts, responses
```

### 7.4 Seed the sonnets

```
prufrock$ .venv/bin/prufrock seed-sonnets data/shakespeare_sonnets.json
# Expect: log line confirming 153 sonnets inserted (154 minus sonnet 126).
```

### Verify

```
prufrock$ PGPASSWORD='<db-password>' \
    psql -h 127.0.0.1 -U prufrock -d prufrock -c "SELECT count(*) FROM sonnets;"
# Expect: count = 153
```

### 7.5 Register yourself as the participant and start the experiment

```
prufrock$ .venv/bin/prufrock register-participant \
    --telegram-user-id <your-id> \
    --telegram-chat-id <your-id> \
    --display-name "Robert"
# (For a personal bot, chat-id and user-id are the same.)

prufrock$ .venv/bin/prufrock start-experiment --participant-telegram-id <your-id>
# Expect: log line with the chosen sonnet's number and the seed couplet.
```

### 7.6 Install the systemd unit

```
prufrock$ exit   # back to root in the LXC
prufrock# cp /opt/prufrock/deploy/prufrock.service /etc/systemd/system/
prufrock# systemctl daemon-reload
prufrock# systemctl enable --now prufrock.service
```

### Verify

```
prufrock# systemctl status prufrock.service
# Expect: active (running), no recent errors.

prufrock# journalctl -u prufrock.service -n 50 --no-pager
# Expect: startup logs, "Application started", APScheduler job booked for today.
```

---

## Stage 8 — Smoke test

### 8.1 Bot reachability

1. From Telegram, message your bot: `/start`.
2. The bot should reply with an acknowledgement (per `bot/handlers.py`).

```
prufrock# journalctl -u prufrock.service -f
```

Watch the log as you send messages; you should see incoming Update payloads and outgoing send_message calls.

### 8.2 Force-fire today's prompt (one-time, for the smoke test)

Rather than waiting for the random fire window, trigger the prompt manually:

```
prufrock$ .venv/bin/prufrock fire-now
```

You should receive the day-1 prompt on Telegram showing the seed couplet.

### 8.3 Reply

Reply with your first line. Within seconds:

* The bot should acknowledge silently (or with a confirmation; check `handlers.py`).
* `journalctl` shows the response recorded.

```
prufrock$ PGPASSWORD='<db-password>' \
    psql -h 127.0.0.1 -U prufrock -d prufrock \
    -c "SELECT day_number, text FROM prompts p JOIN responses r ON r.prompt_id=p.id;"
# Expect: one row, day_number=1, your response text.
```

### 8.4 Reset for the real run

If the smoke test was on a real experiment row, abandon it and start fresh:

```
prufrock$ .venv/bin/prufrock abandon-experiment --participant-telegram-id <your-id>
prufrock$ .venv/bin/prufrock start-experiment --participant-telegram-id <your-id>
```

The real cycle will fire its first prompt at a random time within tomorrow's waking-hours window (or today's, if there's still time).

---

## Operations

### View logs

```
prufrock# journalctl -u prufrock.service -f          # follow
prufrock# journalctl -u prufrock.service --since today
prufrock# journalctl -u prufrock.service -n 200 --no-pager
```

### Restart / stop / start

```
prufrock# systemctl restart prufrock.service
prufrock# systemctl stop prufrock.service
prufrock# systemctl start prufrock.service
```

### Check experiment state

```
prufrock$ .venv/bin/prufrock status
```

This prints the active experiment, day number, the assembled poem so far, and the next scheduled fire time.

### Daily Postgres backup

A nightly `pg_dump` is cheap insurance. Drop this into root's crontab:

```
prufrock# crontab -e
```

Add:

```
15 3 * * * sudo -u postgres pg_dump -Fc prufrock \
  > /var/backups/prufrock/prufrock-$(date +\%Y\%m\%d).dump \
  && find /var/backups/prufrock -name 'prufrock-*.dump' -mtime +30 -delete
```

Verify after the first run:

```
prufrock# ls -lh /var/backups/prufrock/
```

### Updating the application

```
prufrock# su - prufrock
prufrock$ cd /opt/prufrock
prufrock$ git pull
prufrock$ .venv/bin/pip install -e .
prufrock$ .venv/bin/alembic upgrade head
prufrock$ exit
prufrock# systemctl restart prufrock.service
prufrock# journalctl -u prufrock.service -n 50 --no-pager
```

---

## Troubleshooting

### The bot isn't receiving messages

1. `systemctl status prufrock.service` — is it running?
2. `journalctl -u prufrock.service -n 100` — any tracebacks?
3. From inside the LXC: `curl -s https://api.telegram.org/bot<TOKEN>/getMe` — should return your bot's profile JSON. If this fails, the issue is network or token.
4. Telegram only delivers Updates to one consumer at a time. If you accidentally set a webhook in the past, clear it: `curl -s https://api.telegram.org/bot<TOKEN>/deleteWebhook`.

### The scheduler never fires

1. `prufrock status` — does it show a scheduled fire time today?
2. Check `TIMEZONE`, `WAKING_START_LOCAL`, `WAKING_END_LOCAL` in `.env`.
3. `journalctl -u prufrock.service --since today | grep -i schedul` — look for the day-reseed log line.
4. Confirm the LXC's wall clock: `date`. If it's drifted, `systemctl restart systemd-timesyncd`.

### Postgres connection refused

1. `systemctl status postgresql` — running?
2. `ss -lntp | grep 5432` — listening on 127.0.0.1:5432?
3. `tail -50 /var/log/postgresql/postgresql-16-main.log` — any startup errors?

### "permission denied" in `journalctl`

The `prufrock` user is not in `systemd-journal`. Use `sudo journalctl ...` or run journalctl as root.

### Sonnet seeding fails on Gutenberg parsing

The Gutenberg file format is stable but boilerplate can drift. If `seed-sonnets` errors out, check `data/shakespeare_sonnets.json` was generated correctly (153 entries, each with non-empty `line_12` and `line_13`). The generation pipeline lives in `cli.py seed-sonnets`; rerun with `--regenerate` to refetch from Gutenberg.

---

## Decommission (when experiment 0 is complete)

After `R₁₄` is recorded and the assembled poem is delivered:

```
prufrock# systemctl stop prufrock.service
prufrock$ .venv/bin/prufrock export --experiment-id <id> > /var/backups/prufrock/experiment-0-final.json
prufrock# sudo -u postgres pg_dump -Fc prufrock > /var/backups/prufrock/prufrock-experiment-0-complete.dump
```

Copy both files off the LXC for safekeeping. Then either leave the service running for experiment 0.5+ or `systemctl disable prufrock.service` to park it.

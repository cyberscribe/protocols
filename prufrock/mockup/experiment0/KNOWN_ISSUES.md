# Known Issues — Experiment 0

Three bugs identified during the 2026-05-11 deploy. **Do not patch during the active 14-day cycle.** Debugging traffic against the live daemon contaminates the lived-experience data this experiment exists to capture. Address before experiment 1.

## 1. Fire-window can pick past times at mid-day startup

**File**: `src/prufrock/scheduler/fire_window.py`

**Symptom**: When the experiment is started mid-day, the random draw uses the full `[waking_start, waking_end]` window without clamping to `now`. If `now > drawn_time`, APScheduler silently drops the job and the day fires no prompt. Observed 2026-05-11: experiment started 19:01 BST, scheduler drew 15:43 BST, job dropped.

**Fix**: Clamp `window_start = max(now, today_at(waking_start))`. If `now >= waking_end`, roll the draw to tomorrow's window. Add a test covering mid-day and post-window startup.

## 2. `DetachedInstanceError` in `start_experiment`

**File**: `src/prufrock/cli.py:179`

**Symptom**: `start_experiment` raises `sqlalchemy.exc.DetachedInstanceError` post-commit because it touches ORM attributes after the session has expired the instance.

**Fix**: Either stash field values to locals inside the `with db_session()` block, or set `expire_on_commit=False` on the session factory.

## 3. Default migration installs unused pgvector extension

**Files**: `alembic/versions/0001_initial.py`, plus SPEC.md §2 / §4 / §7 and SETUP.md §4

**Symptom**: The generated migration includes `CREATE EXTENSION vector`, which breaks on Postgres clusters without `pgvector` installed. Hand-patched out for the current slice (the LXC's cluster does not have it, and experiment 0 makes no use of it). SPEC.md and SETUP.md still nominate pgvector.

**Fix**: Either gate the extension on a config flag (e.g. `USE_PGVECTOR=false` by default), or remove from the default migration since experiment 0 makes no use of it. Update SPEC.md §2 / §4 / §7 and SETUP.md §4 to match the chosen path.

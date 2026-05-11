import secrets
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

_rng = secrets.SystemRandom()


def random_fire_time(
    waking_start: time,
    waking_end: time,
    tz: ZoneInfo,
    reference_date: date | None = None,
) -> datetime:
    """Return a tz-aware datetime drawn uniformly from [waking_start, waking_end) on reference_date."""
    today = reference_date or datetime.now(tz).date()
    start_dt = datetime.combine(today, waking_start, tzinfo=tz)
    end_dt = datetime.combine(today, waking_end, tzinfo=tz)
    window_seconds = int((end_dt - start_dt).total_seconds())
    if window_seconds <= 0:
        raise ValueError(
            f"waking_end ({waking_end}) must be after waking_start ({waking_start})"
        )
    offset = _rng.randint(0, window_seconds - 1)
    return start_dt + timedelta(seconds=offset)

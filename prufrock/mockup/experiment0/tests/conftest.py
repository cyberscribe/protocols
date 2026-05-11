import os

# Must be set before any prufrock module is imported, because config.py
# runs Settings() at module level and tasks.py imports config at module level.
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost/prufrock_test")
os.environ.setdefault("TELEGRAM_BOT_TOKEN", "123456789:AAfake_token_for_tests_only")
os.environ.setdefault("TELEGRAM_USER_ID", "99999")

from contextlib import contextmanager
from typing import Iterator

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from prufrock.db.models import Base


def pytest_addoption(parser):
    parser.addoption(
        "--pg-url",
        default=None,
        help="PostgreSQL URL for tests (fallback when testcontainers is unavailable)",
    )


@pytest.fixture(scope="session")
def pg_url(request):
    """Provide a live PostgreSQL URL, preferring testcontainers, then --pg-url."""
    cli_url = request.config.getoption("--pg-url")
    if cli_url:
        yield cli_url
        return

    try:
        from testcontainers.postgres import PostgresContainer

        with PostgresContainer("postgres:16-alpine") as pg:
            # testcontainers returns a psycopg2 URL; swap driver for psycopg (v3)
            url = pg.get_connection_url().replace("psycopg2", "psycopg")
            yield url
    except ImportError:
        pytest.skip("testcontainers not installed; use --pg-url to run DB tests.")
    except Exception as exc:
        pytest.skip(f"Could not start Postgres container ({type(exc).__name__}); use --pg-url to run DB tests.")


@pytest.fixture(scope="session")
def engine(pg_url):
    eng = create_engine(pg_url, pool_pre_ping=True)
    # pgvector may not be installed in the test container — create it if possible,
    # otherwise skip silently (it is unused in experiment 0)
    with eng.connect() as conn:
        try:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.commit()
        except Exception:
            conn.rollback()

    Base.metadata.create_all(eng)
    yield eng
    Base.metadata.drop_all(eng)
    eng.dispose()


@pytest.fixture(scope="session")
def SessionFactory(engine):
    return sessionmaker(bind=engine, autoflush=False, autocommit=False)


@pytest.fixture
def session(engine, SessionFactory) -> Iterator[Session]:
    """Function-scoped session that rolls back after each test."""
    conn = engine.connect()
    tx = conn.begin()
    sess = Session(bind=conn, join_transaction_mode="create_savepoint")
    yield sess
    sess.close()
    tx.rollback()
    conn.close()

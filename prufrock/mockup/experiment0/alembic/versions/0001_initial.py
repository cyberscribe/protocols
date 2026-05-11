"""Initial schema: participants, sonnets, experiments, prompts, responses, poem_state view.

Revision ID: 0001
Revises:
Create Date: 2026-05-11
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # pgvector extension — no-op if already present
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "participants",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("telegram_user_id", sa.BigInteger(), unique=True, nullable=False),
        sa.Column("telegram_chat_id", sa.BigInteger(), nullable=False),
        sa.Column("display_name", sa.Text(), nullable=True),
        sa.Column("timezone", sa.Text(), nullable=False, server_default="Europe/London"),
        sa.Column("waking_start_local", sa.Time(), nullable=False, server_default="09:00"),
        sa.Column("waking_end_local", sa.Time(), nullable=False, server_default="22:00"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )

    op.create_table(
        "sonnets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.Text(), nullable=True),
        sa.Column("source", sa.Text(), nullable=False),
        sa.Column("full_text", sa.Text(), nullable=False),
        sa.Column("line_12", sa.Text(), nullable=False),
        sa.Column("line_13", sa.Text(), nullable=False),
    )

    op.create_table(
        "experiments",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column(
            "participant_id",
            sa.Uuid(),
            sa.ForeignKey("participants.id"),
            nullable=False,
        ),
        sa.Column(
            "sonnet_id",
            sa.Integer(),
            sa.ForeignKey("sonnets.id"),
            nullable=False,
        ),
        sa.Column(
            "started_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("status", sa.Text(), nullable=False, server_default="active"),
        sa.CheckConstraint(
            "status IN ('active','completed','abandoned')",
            name="ck_experiment_status",
        ),
    )

    op.create_table(
        "prompts",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column(
            "experiment_id",
            sa.Uuid(),
            sa.ForeignKey("experiments.id"),
            nullable=False,
        ),
        sa.Column("day_number", sa.Integer(), nullable=False),
        sa.Column("antithesis_a", sa.Text(), nullable=False),
        sa.Column("antithesis_b", sa.Text(), nullable=False),
        sa.Column("scheduled_for", sa.DateTime(timezone=True), nullable=False),
        sa.Column("fired_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("telegram_message_id", sa.BigInteger(), nullable=True),
        sa.CheckConstraint(
            "day_number BETWEEN 1 AND 14",
            name="ck_prompt_day_number",
        ),
        sa.UniqueConstraint("experiment_id", "day_number", name="uq_prompt_experiment_day"),
    )

    op.create_table(
        "responses",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column(
            "prompt_id",
            sa.Uuid(),
            sa.ForeignKey("prompts.id"),
            nullable=False,
        ),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("parent_hash_a", sa.Text(), nullable=False),
        sa.Column("parent_hash_b", sa.Text(), nullable=False),
        sa.Column(
            "received_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column("raw_update_json", postgresql.JSONB(), nullable=False),
    )

    # poem_state view — coalesce handles the no-responses-yet case
    op.execute(
        """
        CREATE VIEW poem_state AS
          SELECT e.id AS experiment_id,
                 array[s.line_12, s.line_13]
                   || COALESCE(
                        array_agg(r.text ORDER BY p.day_number)
                          FILTER (WHERE r.id IS NOT NULL),
                        ARRAY[]::text[]
                      ) AS lines
            FROM experiments e
            JOIN sonnets s ON s.id = e.sonnet_id
            LEFT JOIN prompts p ON p.experiment_id = e.id
            LEFT JOIN responses r ON r.prompt_id = p.id
           GROUP BY e.id, s.line_12, s.line_13
        """
    )


def downgrade() -> None:
    op.execute("DROP VIEW IF EXISTS poem_state")
    op.drop_table("responses")
    op.drop_table("prompts")
    op.drop_table("experiments")
    op.drop_table("sonnets")
    op.drop_table("participants")

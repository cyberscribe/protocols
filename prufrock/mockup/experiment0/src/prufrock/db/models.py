import uuid
from datetime import datetime, time

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    Text,
    Time,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    telegram_user_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    telegram_chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    display_name: Mapped[str | None] = mapped_column(Text, nullable=True)
    timezone: Mapped[str] = mapped_column(Text, nullable=False, default="Europe/London")
    waking_start_local: Mapped[time] = mapped_column(
        Time, nullable=False, default=time(9, 0)
    )
    waking_end_local: Mapped[time] = mapped_column(
        Time, nullable=False, default=time(22, 0)
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default="now()"
    )

    experiments: Mapped[list["Experiment"]] = relationship(back_populates="participant")


class Sonnet(Base):
    __tablename__ = "sonnets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(Text, nullable=False)
    full_text: Mapped[str] = mapped_column(Text, nullable=False)
    line_12: Mapped[str] = mapped_column(Text, nullable=False)
    line_13: Mapped[str] = mapped_column(Text, nullable=False)

    experiments: Mapped[list["Experiment"]] = relationship(back_populates="sonnet")


class Experiment(Base):
    __tablename__ = "experiments"
    __table_args__ = (
        CheckConstraint(
            "status IN ('active','completed','abandoned')", name="ck_experiment_status"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    participant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("participants.id"), nullable=False
    )
    sonnet_id: Mapped[int] = mapped_column(ForeignKey("sonnets.id"), nullable=False)
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default="now()"
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    status: Mapped[str] = mapped_column(Text, nullable=False, default="active")

    participant: Mapped[Participant] = relationship(back_populates="experiments")
    sonnet: Mapped[Sonnet] = relationship(back_populates="experiments")
    prompts: Mapped[list["Prompt"]] = relationship(back_populates="experiment")


class Prompt(Base):
    __tablename__ = "prompts"
    __table_args__ = (
        CheckConstraint("day_number BETWEEN 1 AND 14", name="ck_prompt_day_number"),
        UniqueConstraint("experiment_id", "day_number", name="uq_prompt_experiment_day"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    experiment_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("experiments.id"), nullable=False
    )
    day_number: Mapped[int] = mapped_column(Integer, nullable=False)
    antithesis_a: Mapped[str] = mapped_column(Text, nullable=False)
    antithesis_b: Mapped[str] = mapped_column(Text, nullable=False)
    scheduled_for: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    fired_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    telegram_message_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)

    experiment: Mapped[Experiment] = relationship(back_populates="prompts")
    response: Mapped["Response | None"] = relationship(back_populates="prompt")


class Response(Base):
    __tablename__ = "responses"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    prompt_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("prompts.id"), nullable=False
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    parent_hash_a: Mapped[str] = mapped_column(Text, nullable=False)
    parent_hash_b: Mapped[str] = mapped_column(Text, nullable=False)
    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default="now()"
    )
    raw_update_json: Mapped[dict] = mapped_column(JSONB, nullable=False)

    prompt: Mapped[Prompt] = relationship(back_populates="response")

from datetime import time

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str
    telegram_bot_token: str
    telegram_user_id: int

    timezone: str = "Europe/London"
    waking_start_local: str = "09:00"
    waking_end_local: str = "22:00"
    log_level: str = "INFO"

    @field_validator("waking_start_local", "waking_end_local", mode="before")
    @classmethod
    def validate_time_format(cls, v: str) -> str:
        try:
            time.fromisoformat(v)
        except ValueError:
            raise ValueError(f"Expected HH:MM time string, got {v!r}")
        return v


settings = Settings()

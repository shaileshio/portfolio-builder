from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

COMMON_CONFIG = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore",
)


class AppSettings(BaseSettings):
    model_config = {
        **COMMON_CONFIG,
        "env_prefix": "APP_",
    }

    name: str = "Portfolio"
    environment: Literal["development", "production"] = "development"
    api_prefix: str = "/api/v1"
    debug: bool = True


class CorsSettings(BaseSettings):
    model_config = {
        **COMMON_CONFIG,
        "env_prefix": "CORS_",
    }

    allow_origins: list[str] = ["127.0.0.1", "localhost"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True


class DatabaseSettings(BaseSettings):
    model_config = {
        **COMMON_CONFIG,
        "env_prefix": "DATABASE_",
    }

    url: str | None = None


class Settings:
    def __init__(self) -> None:
        self.app = AppSettings()
        self.cors = CorsSettings()
        self.db = DatabaseSettings()


@lru_cache
def get_settings() -> Settings:
    return Settings()

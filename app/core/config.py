from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseModel):
    title: str = "portfolio builder"
    description: str = "Production-grade AI-powered engineering portfolio builder"
    debug: bool = True


class CorsConfig(BaseModel):
    allow_origins: list[str] = ["127.0.0.1", "localhost"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True


class DatabaseConfig(BaseModel):
    url: str | None = None
    test_url: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    app: AppConfig = Field(default_factory=AppConfig)
    cors: CorsConfig = Field(default_factory=CorsConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)


@lru_cache
def get_settings() -> Settings:
    return Settings()

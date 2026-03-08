from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal, List


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o-mini"
    LLM_TIMEOUT: int = 8
    LLM_MAX_TOKENS: int = 300

    APP_ENV: Literal["development", "production"] = "development"
    APP_NAME: str = "SheShield AI"

    CORS_ORIGINS: List[str] = ["http://localhost:5500"]

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
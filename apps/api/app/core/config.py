from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Content OS"
    app_version: str = "0.1.0"
    app_env: str = "development"

    host: str = "0.0.0.0"
    port: int = 8000

    database_url: str = "sqlite:///./data.db"

    jwt_secret: str = "change-me"

    claude_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

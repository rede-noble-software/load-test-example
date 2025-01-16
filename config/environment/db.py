from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    ENGINE: str = "django.db.backends.postgresql"
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_prefix="DB_",
        env_file_encoding="utf-8",
        case_sensitive=True,
        env_file=".env",
    )


class DatabasesSettings(BaseSettings):
    default: PostgresSettings = PostgresSettings()

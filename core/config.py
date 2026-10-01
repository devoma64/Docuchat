from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FASTAPI_ENV: str = "development"
    PORT: int = 8080
    DATABASE_URL: str

    JWT_SECRET: str
    JWT_EXPIRES_IN: str
    REFRESH_TOKEN_EXPIRES_IN: str

    OPEN_API_KEY: str | None = None

    REDIS_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()  # type: ignore

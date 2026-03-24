from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings(BaseSettings):
    # For SQLite, we just need a file name or path
    SQLITE_DB_NAME: str = "delivery_management.db"

    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        # SQLite connection string format: sqlite:///filename.db
        return f"sqlite:///{self.SQLITE_DB_NAME}"

settings = DatabaseSettings()
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the project root directory (parent of 'app' folder)
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

_base_config = SettingsConfigDict(
    env_file=str(ENV_FILE),
    env_ignore_empty=True,
    extra="ignore",
)

class DatabaseSettings(BaseSettings):
    # For SQLite, we just need a file name or path
    SQLITE_DB_NAME: str = "delivery_management.db"

    model_config = _base_config

    @property
    def DATABASE_URL(self) -> str:
        # SQLite connection string format: sqlite:///filename.db
        return f"sqlite:///{self.SQLITE_DB_NAME}"

class SecuritySettings(BaseSettings):
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = _base_config

security_settings = SecuritySettings()
db_settings = DatabaseSettings()

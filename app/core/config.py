from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # === Project Settings ===
    PROJECT_NAME: str = "API"
    PROJECT_VERSION: str = "1.0.0"

    # === Project Root Path ===
    ROOT_PATH: str = "/"

    # === Database Settings ===
    MONGO_DB_USERNAME: str
    MONGO_DB_PASSWORD: str
    MONGO_DB_HOSTNAME: str = "localhost"
    MONGO_DB_PORT: int = 27017
    MONGO_DB_NAME: str = "admin"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",  # Ignora variáveis não declaradas
    )

    @property
    def DATABASE_URL(self) -> str:
        username = self.MONGO_DB_USERNAME
        password = self.MONGO_DB_PASSWORD
        hostname = self.MONGO_DB_HOSTNAME
        port = self.MONGO_DB_PORT
        db_name = self.MONGO_DB_NAME
        return (
            f"mongodb://{username}:{password}@{hostname}:{port}/{db_name}"
            "?authSource=admin&uuidRepresentation=standard"
        )


# === Singleton Settings Instance ===
settings = Settings()  # type: ignore

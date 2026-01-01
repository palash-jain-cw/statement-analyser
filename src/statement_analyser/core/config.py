from pydantic_settings import BaseSettings
from pathlib import Path
from statement_analyser.core.logging_config import configure_logging

project_root = Path(__file__).parent.parent


logger = configure_logging(__name__)


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str

    class Config:
        env_file = project_root / ".env"
        env_file_encoding = "utf-8"


settings = Settings()

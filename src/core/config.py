from pathlib import Path
from typing import Literal, Optional

from pydantic import Field, SecretStr, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / '.env'

STATIC_DIR = BASE_DIR / 'static'


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH, env_file_encoding='utf-8', extra='ignore'
    )


class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix='db_')

    host: str
    name: str
    password: SecretStr
    port: int
    user: str
    url: Optional[str] = Field(default=None)

    test_host: str = 'localhost'
    test_name: str = 'test_db'
    test_password: SecretStr = SecretStr('postgres')
    test_port: int = 5432
    test_user: str = 'postgres'
    test_url: Optional[str] = Field(default=None)

    @field_validator('url', mode='before')
    @classmethod
    def assemble_url(cls, v: Optional[str], info: ValidationInfo) -> str:
        if not v:
            return (
                f'postgresql+asyncpg://{info.data.get("user")}:'
                f'{info.data.get("password").get_secret_value()}@'
                f'{info.data.get("host")}:{info.data.get("port")}/'
                f'{info.data.get("name")}'
            )
        return v

    @field_validator('test_url', mode='before')
    @classmethod
    def assemble_test_url(cls, v: Optional[str], info: ValidationInfo) -> str:
        if not v:
            return (
                f'postgresql+asyncpg://{info.data.get("test_user")}:'
                f'{info.data.get("test_password").get_secret_value()}@'
                f'{info.data.get("test_host")}:{info.data.get("test_port")}/'
                f'{info.data.get("test_name")}'
            )
        return v


class Settings(BaseSettings):
    """
    Global application settings container.

    Integrates database connection and authentication configurations.
    """

    app_name: str = 'Todo'
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)


    @classmethod
    def load(cls) -> 'Settings':
        """Initializes and returns a Settings instance."""
        return cls()


settings: Settings = Settings.load()


from enum import Enum

from pydantic.v1 import BaseSettings


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings:
    app_env: AppEnvTypes = AppEnvTypes.dev

    class Config:
        env_file = ".env"
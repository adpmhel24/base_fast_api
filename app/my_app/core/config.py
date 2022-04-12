import os
from typing import Any, List, Union
from dotenv import load_dotenv

from pydantic import AnyHttpUrl, BaseSettings, validator

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Settings(BaseSettings):
    # default conf goes here
    app_name: str = "Inventory System"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI")
    FIRST_SUPERUSER_EMAIL: str = os.environ.get("FIRST_SUPERUSER_EMAIL")
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get("FIRST_SUPERUSER_PASSWORD")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Inventory System"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()

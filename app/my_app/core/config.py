import os
from typing import Any
from dotenv import load_dotenv

from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..env"))


class Settings(BaseSettings):
    # default conf goes here
    app_name: str = "Inventory System"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: Any = os.environ.get("SQLALCHEMY_DATABASE_URI")
    FIRST_SUPERUSER: str = os.environ.get("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get("FIRST_SUPERUSER_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 1440


settings = Settings()

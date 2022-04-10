from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from my_app.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False, future=True)

AsyncSessionLocal = sessionmaker(
    class_=AsyncSession, bind=engine, expire_on_commit=False
)

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt
from pydantic import ValidationError

from .db.session import AsyncSessionLocal
from app.my_app.core.config import settings

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


# Dependency
async def async_session() -> AsyncSession:
    async_session = AsyncSessionLocal

    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt
from pydantic import ValidationError

from .schemas.token import TokenPayload

from .db.session import AsyncSessionLocal
from .core.config import settings
from .models import system_user
from .cruds.crud_system_user import system_user_crud

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


async def get_current_user(
    session: AsyncSession = Depends(async_session),
    token: str = Depends(reusable_oauth2),
) -> system_user.SystemUserRead:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await system_user_crud.get_by_id(session, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_active_user(
    current_user: system_user.SystemUserRead = Depends(get_current_user),
) -> system_user.SystemUserRead:
    if not system_user_crud.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return await current_user


async def get_current_active_superuser(
    current_user: system_user.SystemUserRead = Depends(get_current_user),
) -> system_user.SystemUserRead:
    if not system_user_crud.is_super_admin(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user

from sqlalchemy.ext.asyncio import AsyncSession

from ..cruds.crud_system_user import system_user
from .tables import SystemUser
from ..core.config import settings
from ..core.security import get_password_hash


async def create_initial_su(session: AsyncSession) -> None:
    # Create initial super user
    user_query = await system_user.get_super_admin(session=session)
    if not user_query:
        user = await system_user.get_by_email(
            session=session, email=settings.FIRST_SUPERUSER_EMAIL
        )
        if not user:
            user_obj = SystemUser(
                email=settings.FIRST_SUPERUSER_EMAIL, is_super_admin=True
            )
            user_obj.hashed_password = get_password_hash(
                settings.FIRST_SUPERUSER_PASSWORD
            )
            session.add(user_obj)
            await session.commit()
            await session.refresh(user_obj)

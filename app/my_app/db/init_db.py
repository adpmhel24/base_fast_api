# from sqlalchemy.ext.asyncio import AsyncSession

# from app.cruds.user import get_super_admin
# from app.models.user import User
# from app.core.config import settings


# async def create_initial_su(session: AsyncSession) -> None:
#     # Create initial super user
#     user_query = await get_super_admin(session=session)
#     if not user_query:
#         user = User(email=settings.FIRST_SUPERUSER, is_super_admin=True)
#         user.hashing_password(settings.FIRST_SUPERUSER_PASSWORD)
#         session.add(user)
#         await session.commit()
#         await session.refresh(user)

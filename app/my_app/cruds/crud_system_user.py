from typing import Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# from sqlalchemy.sql import text
from fastapi import HTTPException, status
from sqlmodel import func, text


from ..models.system_user import SystemUser, SystemUserCreate, SystemUserRead
from ..core.security import get_password_hash, verify_password
from .crud_authorization import auth_crud
from ..cruds.crud_base import CRUDBase


class CRUDSystemUser(CRUDBase):
    async def create(
        self, session: AsyncSession, schema: SystemUserCreate
    ) -> Optional[SystemUserRead]:

        get_user = await self.get_by_email(session=session, email=schema.email)
        if get_user:
            raise HTTPException(
                status_code=400, detail="Email address is already exist!"
            )

        user_obj = SystemUser(**schema.dict())
        user_obj.hashed_password = get_password_hash(schema.password)

        # Add User to the authorization table
        await auth_crud.create_auth_for_new_user(user_obj=user_obj, session=session)

        await session.commit()
        await session.refresh(user_obj)
        return user_obj

    async def get_by_email(
        self, session: AsyncSession, email: str
    ) -> Optional[SystemUserRead]:
        statement = select(SystemUser).where(SystemUser.email == email)
        user = await session.execute(statement)
        result = user.scalars().first()
        return result

    async def get_super_admin(self, session: AsyncSession) -> Optional[SystemUserRead]:
        statement = select(SystemUser).where(SystemUser.is_super_admin.is_(True))
        user = await session.execute(statement)
        result = user.scalars().first()
        return result

    async def get_all_user(
        self,
        *,
        session: AsyncSession,
        is_active: bool = True,
    ) -> Optional[List[SystemUserRead]]:
        statement = (
            select(SystemUser)
            .where(SystemUser.is_active.is_(is_active))
            .order_by(SystemUser.id)
        )
        exec = await session.execute(statement)
        result = exec.scalars().all()
        return result

    async def authenticate(
        self, session: AsyncSession, *, email: str, password: str
    ) -> Optional[SystemUserRead]:
        user = await self.get_by_email(session=session, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_by_id(self, session: AsyncSession, id) -> Optional[SystemUserRead]:
        statement = select(SystemUser).where(SystemUser.id == id)
        user = await session.execute(statement)
        result = user.scalars().first()
        return result

    def is_active(self, user: SystemUserRead) -> bool:
        return user.is_active

    def is_super_admin(self, user: SystemUserRead) -> bool:
        return user.is_super_admin


system_user_crud = CRUDSystemUser()

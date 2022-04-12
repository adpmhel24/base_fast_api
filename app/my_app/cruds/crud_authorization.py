from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from sqlmodel import and_

from app.my_app.models.system_user import SystemUser
from app.my_app.models.module import Module
from ..models.authorization import (
    Authorization,
    AuthorizationCreate,
    AuthorizationRead,
    AuthRole,
)


class CRUDAuthorization:
    async def create_auth_for_new_user(
        self, user_obj: SystemUser, session: AsyncSession
    ):
        statement = select(Module).where(Module.is_deleted.isnot(True))
        module_exec = await session.execute(statement)
        modules = module_exec.scalars().all()
        if modules:
            for module in modules:
                auth_obj = Authorization(module_id=module.id)

                # Check if the user is super_admin
                if user_obj.is_super_admin:
                    auth_obj.auth_role = AuthRole.all
                else:
                    auth_obj.auth_role = AuthRole.unathorized
                user_obj.auths.append(auth_obj)

                session.add(auth_obj)
        else:
            session.add(user_obj)

    async def create_auth_for_new_module(
        self, *, module_obj: Module, session: AsyncSession
    ):
        statement = select(SystemUser).where(
            and_(SystemUser.is_deleted.isnot(True), SystemUser.is_active.is_(True))
        )
        users_exec = await session.execute(statement)
        users = users_exec.scalars().all()
        if users:
            # Check if theres a user
            for user in users:
                # Loop the user here
                if await self.get_auth_by_user_id(
                    session=session, user_id=user.id, module_id=module_obj.id
                ):
                    # Check if user id is existing in auth table
                    # then continue
                    continue

                auth_obj = Authorization(user_id=user.id, module_id=module_obj.id)

                # Check if the user is super_admin
                if user.is_super_admin:
                    auth_obj.auth_role = AuthRole.all
                else:
                    auth_obj.auth_role = AuthRole.unathorized
                session.add(auth_obj)

    async def get_auth_by_user_id(
        self, *, session: AsyncSession, user_id: int, module_id: int
    ):
        statement = select(Authorization).where(
            Authorization.user_id == user_id, Authorization.module_id == module_id
        )
        auth_exec = await session.execute(statement)
        auth = auth_exec.scalars().all()
        return auth


auth_crud = CRUDAuthorization()

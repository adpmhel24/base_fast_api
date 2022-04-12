from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from fastapi import HTTPException

from ..models.module import Module, ModuleCreate, ModuleRead
from .crud_authorization import auth_crud


class CRUDModule:
    async def create(self, *, session: AsyncSession, schema: ModuleCreate):
        module = await self.get_by_name(session=session, name=schema.name)
        if module:
            raise HTTPException(status_code=400, detail="Module name is exist!")

        module_obj = Module(**schema.dict())
        session.add(module_obj)
        await session.flush()
        await auth_crud.create_auth_for_new_module(
            module_obj=module_obj, session=session
        )

        await session.commit()
        await session.refresh(module_obj)
        return module_obj

    async def get_by_name(
        self, session: AsyncSession, name: str
    ) -> Optional[ModuleRead]:
        statement = select(Module).where(Module.name.contains(name))
        sess_exec = await session.execute(statement)
        module = sess_exec.scalars().first()
        return module


module_crud = CRUDModule()

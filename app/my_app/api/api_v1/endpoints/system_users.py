from typing import Any
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.my_app.schemas.success import SuccessMessage

from ....models.system_user import SystemUserCreate, SystemUserRead
from ....dependencies import (
    async_session,
    get_current_active_superuser,
    get_current_user,
)
from ....cruds.crud_system_user import system_user_crud

router = APIRouter()


@router.post("/", response_model=SuccessMessage)
async def create_system_user(
    *,
    session: AsyncSession = Depends(async_session),
    schema: SystemUserCreate,
    current_user: SystemUserRead = Depends(get_current_active_superuser),
) -> Any:

    result = await system_user_crud.create(session=session, schema=schema)
    return SuccessMessage(message="Successfully created!", data=result)


@router.get("/", response_model=SuccessMessage)
async def get_all_users(
    *,
    is_active: bool = Query(True),
    session: AsyncSession = Depends(async_session),
    current_user: SystemUserRead = Depends(get_current_user),
):
    result = await system_user_crud.get_all_user(session=session, is_active=is_active)
    return SuccessMessage(data=result)

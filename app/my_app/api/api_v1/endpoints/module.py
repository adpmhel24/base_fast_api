from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.my_app.dependencies import async_session, get_current_active_superuser
from app.my_app.models.system_user import SystemUserRead

from app.my_app.schemas.success import SuccessMessage
from ....models.module import ModuleCreate
from ....cruds.crud_module import module_crud


router = APIRouter()


@router.post("/", response_model=SuccessMessage)
async def create_module(
    *,
    session: AsyncSession = Depends(async_session),
    schema: ModuleCreate,
    current_user: SystemUserRead = Depends(get_current_active_superuser),
) -> Any:

    result = await module_crud.create(session=session, schema=schema)
    return SuccessMessage(message="Successfully created!", data=result)

from fastapi import APIRouter
from .endpoints import system_users, login, module


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(
    system_users.router, prefix="/system_users", tags=["system_user"]
)
api_router.include_router(module.router, prefix="/module", tags=["module"])

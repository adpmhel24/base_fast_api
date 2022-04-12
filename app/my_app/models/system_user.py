import asyncio
from typing import List
from fastapi import Depends
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import event, select


from .db_base_model import BaseDbModel


class SystemUserBase(SQLModel):
    email: str = Field(index=True, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    is_super_admin: bool = Field(default=False)


class SystemUser(SystemUserBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "system_users"

    hashed_password: str
    auths: List["Authorization"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Authorization.user_id==SystemUser.id",
            "cascade": "delete",
        },
        back_populates="user",
    )


class SystemUserCreate(SystemUserBase):
    password: str


class SystemUserRead(SystemUserBase):
    id: int


from ..models.authorization import Authorization

SystemUser.update_forward_refs()
# from ..dependencies import AsyncSessionLocal
# from ..cruds.crud_authorization import auth_crud
# from sqlalchemy.orm import Session


# async def fn(obj):
#     async_session = AsyncSessionLocal
#     async with async_session() as session:
#         try:
#             await auth_crud.create_auth_for_new_user(session=session, user_obj=obj)
#         finally:
#             await session.close()


# @event.listens_for(Session, "before_commit")
# def before_flush_event(*args):
#     sess = args[0]
#     for obj in sess.new:
#         if isinstance(obj, SystemUser):
#             print(obj)
#             coro = fn(obj)
#             coro.send(None)

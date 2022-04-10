from typing import List
from sqlmodel import Relationship, SQLModel, Field
from app.my_app.models.authorization import Authorization

from app.my_app.models.base_model import DbBaseModel


class SystemUserBase(SQLModel):
    email: str = Field(index=True, index=True, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    is_super_admin: bool = Field(default=False)


class SystemUser(SystemUserBase, DbBaseModel, table=True):
    __tablename__ = "system_users"

    hashed_password: str
    authorizations: List["Authorization"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="user"
    )


# Will be the body of Create
class SystemUserCreate(SystemUserBase):
    password: str


class SystemUserRead(SystemUserBase):
    id: int

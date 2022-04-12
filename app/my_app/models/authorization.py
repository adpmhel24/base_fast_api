import enum
from typing import Optional
from sqlmodel import Enum, Relationship, SQLModel, Field, Column

from .db_base_model import BaseDbModel


class AuthRole(str, enum.Enum):
    unathorized = "unauthorized"
    create = "create"
    read = "read"
    updated = "update"
    delete = "delete"
    all = "all"


class AuthorizationBase(SQLModel):
    user_id: int = Field(nullable=False, index=True, foreign_key="system_users.id")
    module_id: int = Field(nullable=False, index=True, foreign_key="modules.id")
    auth_role: AuthRole = Field(
        default=AuthRole.unathorized, sa_column=Column(Enum(AuthRole))
    )
    is_active: bool = Field(default=True)


class Authorization(AuthorizationBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "authorizations"

    user: Optional["SystemUser"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Authorization.user_id==SystemUser.id",
            "lazy": "joined",
        },
        back_populates="auths",
    )

    module: Optional["Module"] = Relationship(
        sa_relationship_kwargs={
            "lazy": "joined",
            "cascade": "delete",
        }
    )


class AuthorizationCreate(AuthorizationBase):
    """Create Schema"""

    pass


class AuthorizationRead(AuthorizationBase):
    """Read Schema"""

    pass


from ..models.system_user import SystemUser
from ..models.module import Module

Authorization.update_forward_refs()

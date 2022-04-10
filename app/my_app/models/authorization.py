from typing import Optional
from sqlmodel import Relationship, SQLModel, Field, Column, Integer, ForeignKey

from .db_base_models import BaseDBModel
from .system_user import User


class AuthorizationBase(SQLModel):
    user_id: int = Field(nullable=False, index=True, foreign_key="system_users.id")
    table_id: int = Field(nullable=False, index=True, foreign_key="tables.id")
    is_active: bool = Field(default=True)


class Authorization(AuthorizationBase, BaseDBModel, table=True):
    __tablename__ = "authorizations"
    """Database Schema"""

    user: Optional[User] = Relationship(back_populates="authorizations")


class AuthorizationCreate(AuthorizationBase):
    """Create Schema"""

    pass


class AuthorizationRead(AuthorizationBase):
    """Read Schema"""

    pass

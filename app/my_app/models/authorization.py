from typing import Optional
from sqlmodel import Relationship, SQLModel, Field, Column, Integer, ForeignKey

from app.my_app.models.db_base_model import DbBaseModel
from .system_user import User


class AuthorizationBase(SQLModel):
    user_id: int = Field(nullable=False, index=True, foreign_key="system_users.id")
    table_id: int = Field(nullable=False, index=True, foreign_key="tables.id")
    is_active: bool = Field(default=True)


class Authorization(AuthorizationBase, DbBaseModel, table=True):
    __tablename__ = "authorizations"
    """Database Schema"""

    user: Optional[User] = Relationship(back_populates="authorizations")


class AuthorizationCreate(AuthorizationBase):
    """Create Schema"""

    pass


class AuthorizationRead(AuthorizationBase):
    """Read Schema"""

    pass

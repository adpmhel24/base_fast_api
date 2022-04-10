from typing import Optional
from sqlmodel import Column, ForeignKey, Integer, Relationship, SQLModel, Field

from .db_base_models import BaseDBModel
from app.my_app.models.company import Company


class BranchBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)
    company_id: int = Field(nullable=False, index=True, foreign_key="companies.id")

    company: Optional[Company] = Relationship(back_populates="branches")


class Branch(BranchBase, BaseDBModel, table=True):
    __tablename__ = "branches"
    """Database Schema"""

    pass


class BranchCreate(BranchBase):
    """Create Schema"""

    pass


class BranchRead(BranchBase):
    """Read Schema"""

    pass

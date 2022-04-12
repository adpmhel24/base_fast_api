from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field

from .db_base_model import BaseDbModel


class CompanyBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)


class Company(CompanyBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "companies"

    branches: List["Branch"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="company"
    )


class CompanyCreate(CompanyBase):
    """Create Schema"""

    pass


class CompanyRead(CompanyBase):
    """Read Schema"""

    pass


from ..models.branch import Branch

Company.update_forward_refs()

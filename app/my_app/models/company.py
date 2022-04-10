from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field

from app.my_app.models.base_model import DbBaseModel
from app.my_app.models.branch import Branch


class CompanyBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)


class Company(CompanyBase, DbBaseModel, table=True):
    __tablename__ = "companies"
    """Database Schema"""

    branches: List["Branch"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="company"
    )


class CompanyCreate(CompanyBase):
    """Create Schema"""

    pass


class CompanyRead(CompanyBase):
    """Read Schema"""

    pass

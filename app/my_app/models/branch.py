from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field
from ..models.db_base_model import BaseDbModel


class BranchBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)
    company_id: int = Field(nullable=False, index=True, foreign_key="companies.id")


class Branch(BranchBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "branches"

    company: Optional["Company"] = Relationship(back_populates="branches")
    warehouses: List["Warehouse"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="branch"
    )


class BranchCreate(BranchBase):
    """Create Schema"""

    pass


class BranchRead(BranchBase):
    """Read Schema"""

    pass


from ..models.warehouse import Warehouse
from ..models.company import Company


Branch.update_forward_refs()

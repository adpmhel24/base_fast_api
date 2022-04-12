from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from .db_base_model import BaseDbModel


class WarehouseBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)
    branch_id: int = Field(nullable=False, foreign_key="branches.id")


class Warehouse(WarehouseBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "warehouses"

    branch: Optional["Branch"] = Relationship(back_populates="warehouses")


class WarehouseCreate(WarehouseBase):
    """Create Schema"""

    pass


class WarehouseRead(WarehouseBase):
    """Read Schema"""

    id: int


from ..models.branch import Branch

Warehouse.update_forward_refs()

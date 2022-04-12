from typing import List, Optional

from sqlmodel import Relationship, SQLModel, Field
from ..models.db_base_model import BaseDbModel

from ..models.company import Company
from ..models.warehouse import Warehouse


class UoMBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]
    is_active: bool = Field(default=True)


class UoM(UoMBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "uoms"


class UoMCreate(UoMBase):
    """Create Schema"""

    pass


class UoMRead(UoMBase):
    """Read Schema"""

    pass

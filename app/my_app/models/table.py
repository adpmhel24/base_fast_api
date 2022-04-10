from typing import Optional
from sqlmodel import SQLModel, Field

from app.my_app.models.base_model import DbBaseModel


class TableBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]


class Table(TableBase, DbBaseModel, table=True):
    __tablename__ = "tables"
    """Database Schema"""

    pass


class TableCreate(TableBase):
    """Create Schema"""

    pass


class TableRead(TableBase):
    """Read Schema"""

    pass

from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field

from .db_base_model import BaseDbModel


class ModuleBase(SQLModel):
    name: str = Field(
        default=None, nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    description: Optional[str]


class Module(ModuleBase, BaseDbModel, table=True):
    """Database Model"""

    __tablename__ = "modules"


class ModuleCreate(ModuleBase):
    """Create Schema"""

    pass


class ModuleRead(ModuleBase):
    """Read Schema"""

    pass


from .authorization import Authorization

Module.update_forward_refs()

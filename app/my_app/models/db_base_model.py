from datetime import datetime
from typing import Optional
from sqlalchemy import null

from sqlmodel import SQLModel, Field, func


class BaseDBModel(SQLModel):
    id: int = Field(primary_key=True, nullable=False, sa_column_kwargs={"unique": True})
    date_created: datetime = Field(default=func.now(), nullable=False)
    date_updated: Optional[datetime] = Field(nullable=True)
    date_deleted: Optional[datetime]
    created_by: Optional[int] = Field(default=None, foreign_key="users.id")
    updated_by: Optional[int] = Field(default=None)
    deleted_by: Optional[int] = Field(default=None)
    is_deleted: bool = Field(default=False)

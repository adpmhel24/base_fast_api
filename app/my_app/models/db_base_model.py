from datetime import datetime
from typing import Optional
from sqlalchemy import null

from sqlmodel import SQLModel, Field, func


class BaseDbModel(SQLModel):
    id: int = Field(primary_key=True, nullable=False, sa_column_kwargs={"unique": True})
    date_created: datetime = Field(default=datetime.now(), nullable=False)
    date_updated: Optional[datetime] = Field(nullable=True)
    created_by: Optional[int] = Field(default=None, foreign_key="system_users.id")
    updated_by: Optional[int] = Field(default=None)
    deleted_by: Optional[int] = Field(default=None)
    date_deleted: Optional[datetime]
    is_deleted: bool = Field(default=False)

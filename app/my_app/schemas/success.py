from typing import Any, Optional, TypeVar
from pydantic import BaseModel
from sqlmodel import SQLModel


DataSchemaType = TypeVar("DataSchemaType", bound=SQLModel)


class SuccessMessage(BaseModel):
    message: Optional[str] = "Success"
    data: Optional[Any]

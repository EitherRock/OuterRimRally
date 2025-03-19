from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..category.schemas import CategoryBase

class PartBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category_id: int = Field(..., )
    category: Optional[CategoryBase] = None
    description: Optional[str] = Field(None)
    price: int = Field(default=0)
    stock_quantity: int = Field(default=0)
    rating: int = Field(default=0)


class PartCreate(PartBase):
    pass

class PartUpdate(PartBase):
    name: Optional[str] = None
    category_id: Optional[int] = None
    description: Optional[str] = None
    price: Optional[int] = None
    stock_quantity: Optional[int] = None

class PartResponse(PartBase):
    id: int
    created: datetime

    class Config:
        from_attributes = True
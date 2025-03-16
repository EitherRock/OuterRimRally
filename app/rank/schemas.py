from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class RankBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    credits_first: int = Field(..., ge=0) # ge = greater than or equal
    credits_second: int = Field(..., ge=0)
    credits_third: int = Field(..., ge=0)

class RankCreate(RankBase):
    pass

class RankUpdate(RankBase):
    name: Optional[str] = None
    credits_first: Optional[int] = None
    credits_second: Optional[int] = None
    credits_third: Optional[int] = None

class RankResponse(RankBase):
    id: int
    created: datetime

    class Config:
        from_attributes = True 
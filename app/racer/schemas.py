from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..rank.schemas import RankBase

class RacerBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    rank_id: int = Field(default=1)
    rank: Optional[RankBase] = None
    races_attended: int = Field(default=0, ge=0)
    credits: int = Field(default=1000, ge=0)

class RacerCreate(RacerBase):
    password: str = Field(..., min_length=6, max_length=100)

class RacerUpdate(RacerBase):
    name: Optional[str] = None
    rank_id: Optional[int] = None
    races_attended: Optional[int] = None
    credits: Optional[int] = None
    password: Optional[str] = None

class RacerResponse(RacerBase):
    id: int
    created: datetime

    class Config:
        from_attributes = True # Important for response model to map from SQLAlchemy model to Pydantic model

from pydantic import BaseModel, Field, model_validator
from typing import Optional, Any
from datetime import datetime

from ..part.schemas import PartBase
from ..racer.schemas import RacerBase

class CruiserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    racer_id: int = Field(...,)
    racer: Optional[RacerBase] = None
    power_source_id: int = Field(...,)
    power_source: Optional[PartBase] = None
    propulsion_id: int = Field(...,)
    propulsion: Optional[PartBase] = None
    handling_id: int = Field(...,)
    handling: Optional[PartBase] = None
    total_rating: int = Field(default=0)


class CruiserCreate(CruiserBase):
    pass

class CruiserUpdate(CruiserBase):
    name: Optional[str] = None
    racer_id: Optional[int] = None
    power_source_id: Optional[int] = None
    propulsion_id: Optional[int] = None
    handling_id: Optional[int] = None
    total_rating: Optional[int] = None

class CruiserResponse(CruiserBase):
    id: int
    created: datetime

    class Config:
        from_attributes = True
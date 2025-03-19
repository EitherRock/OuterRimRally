from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .services import create
from .schemas import CruiserCreate, CruiserResponse

from ..database.core import get_db

router = APIRouter(prefix='/cruisers', tags=['cruisers'])

@router.post('/', response_model=CruiserResponse)
def create_cruiser(cruiser: CruiserCreate, db: Session = Depends(get_db)):
    return create(db=db, cruiser=cruiser)
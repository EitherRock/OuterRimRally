from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/ranks", tags=["ranks"])

@router.post("/", response_model=schemas.RankResponse)
def create_rank(rank: schemas.RankCreate, db: Session = Depends(get_db)):
    return crud.create_rank(db=db, rank=rank)
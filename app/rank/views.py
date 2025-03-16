from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .services import create, get_all, get, update, delete
from .schemas import RankCreate, RankUpdate, RankResponse
from ..database.core import get_db

router = APIRouter(prefix="/ranks", tags=["ranks"])

@router.post("/", response_model=RankResponse)
def create_rank(rank: RankCreate, db: Session = Depends(get_db)):
    return create(db=db, rank=rank)

@router.get("/", response_model=List[RankResponse])
def get_ranks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all(db=db, skip=skip, limit=limit)

@router.get("/{rank_id}", response_model=RankResponse)
def get_rank(rank_id: int, db: Session = Depends(get_db)):
    db_rank = get(db=db, rank_id=rank_id)
    if db_rank is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rank id {rank_id} not found"
        )
    return db_rank

@router.put("/{rank_id}", response_model=RankResponse)
def update_rank(rank_id: int, rank: RankUpdate, db: Session = Depends(get_db)):
    return update(db=db, rank_id=rank_id, rank=rank)

@router.delete("/{rank_id}", response_model=None)
def delete_rank(rank_id: int, db: Session = Depends(get_db)):
    return delete(db=db, rank_id=rank_id)
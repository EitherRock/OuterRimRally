from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import rank_crud
from ..schemas import rank, common
from ..database import get_db

router = APIRouter(prefix="/ranks", tags=["ranks"])

@router.post("/", response_model=rank.RankResponse)
def create_rank(rank: rank.RankCreate, db: Session = Depends(get_db)):
    return rank_crud.create_rank(db=db, rank=rank)

@router.get("/", response_model=List[rank.RankResponse])
def get_ranks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return rank_crud.get_ranks(db=db, skip=skip, limit=limit)

@router.get("/{rank_id}", response_model=rank.RankResponse)
def get_rank(rank_id: int, db: Session = Depends(get_db)):
    db_rank = rank_crud.get_rank(db=db, rank_id=rank_id)
    if db_rank is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rank id {rank_id} not found"
        )
    return db_rank

@router.put("/{rank_id}", response_model=rank.RankResponse)
def update_rank(rank_id: int, rank: rank.RankUpdate, db: Session = Depends(get_db)):
    return rank_crud.update_rank(db=db, rank_id=rank_id, rank=rank)

@router.delete("/{rank_id}", response_model=common.DeleteResponse)
def delete_rank(rank_id: int, db: Session = Depends(get_db)):
    return rank_crud.delete_rank(db=db, rank_id=rank_id)
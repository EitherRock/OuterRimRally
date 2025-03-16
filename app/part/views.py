from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .services import create, get_all, get, update, delete
from .schemas import PartCreate, PartUpdate, PartResponse
from ..database.core import get_db

router = APIRouter(prefix="/parts", tags=["parts"])

@router.post("/", response_model=PartResponse)
def create_part(part: PartCreate, db: Session = Depends(get_db)):
    return create(db=db, part=part)


@router.get("/", response_model=List[PartResponse])
def get_parts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all(db=db, skip=skip, limit=limit)

@router.get("/{part_id}", response_model=PartResponse)
def get_part(part_id: int, db: Session = Depends(get_db)):
    db_part = get(db=db, part_id=part_id)
    if db_part is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part id {part_id} not found"
        )
    return db_part

@router.put("/{part_id}", response_model=PartResponse)
def update_part(part_id: int, part: PartUpdate, db: Session = Depends(get_db)):
    return update(db=db, part_id=part_id, part=part)

@router.delete("/{part_id}", response_model=None)
def delete_part(part_id: int, db: Session = Depends(get_db)):
    return delete(db=db, part_id=part_id)
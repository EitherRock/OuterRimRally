from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import part_crud
from ..schemas import part, common
from ..database import get_db

router = APIRouter(prefix="/parts", tags=["parts"])

@router.post("/", response_model=part.PartResponse)
def create_part(part: part.PartCreate, db: Session = Depends(get_db)):
    return part_crud.create_part(db=db, part=part)


@router.get("/", response_model=List[part.PartResponse])
def get_parts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return part_crud.get_parts(db=db, skip=skip, limit=limit)

@router.get("/{part_id}", response_model=part.PartResponse)
def get_part(part_id: int, db: Session = Depends(get_db)):
    db_part = part_crud.get_part(db=db, part_id=part_id)
    if db_part is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part id {part_id} not found"
        )
    return db_part

@router.put("/{part_id}", response_model=part.PartResponse)
def update_part(part_id: int, part: part.PartUpdate, db: Session = Depends(get_db)):
    return part_crud.update_part(db=db, part_id=part_id, part=part)

@router.delete("/{part_id}", response_model=common.DeleteResponse)
def delete_part(part_id: int, db: Session = Depends(get_db)):
    return part_crud.delete_part(db=db, part_id=part_id)
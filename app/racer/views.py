from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .schemas import RacerCreate, RacerResponse, RacerUpdate
from .services import create, update, delete, get, get_all, get_by_name
from ..database.core import get_db
from ..auth.services import get_current_user


router = APIRouter(prefix="/racers", tags=["racers"])

@router.post("/", response_model=RacerResponse)
def create_racer(racer: RacerCreate, db: Session = Depends(get_db)):
    return create(db=db, racer=racer)

@router.get("/", response_model=List[RacerResponse])
def get_racers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all(db=db, skip=skip, limit=limit)

@router.get("/{racer_id}", response_model=RacerResponse)
def get_racer(racer_id: int, db: Session = Depends(get_db)):
    return get(db=db, racer_id=racer_id)


@router.put("/{racer_id}", response_model=RacerResponse)
def update_racer(
    racer_id: int, 
    racer: RacerUpdate, 
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return update(db=db, racer_id=racer_id, racer=racer)

@router.delete("/{racer_id}", response_model=None)
def delete_racer(racer_id: int, db: Session = Depends(get_db)):
    return delete(db=db, racer_id=racer_id)
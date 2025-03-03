from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/racers", tags=["racers"])

@router.post("/", response_model=schemas.RacerResponse)
def create_racer(racer: schemas.RacerCreate, db: Session = Depends(get_db)):
    return crud.create_racer(db=db, racer=racer)

@router.get("/", response_model=List[schemas.RacerResponse])
def get_racers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_racers(db=db, skip=skip, limit=limit)

@router.get("/{racer_id}", response_model=schemas.RacerResponse)
def get_racer(racer_id: int, db: Session = Depends(get_db)):
    db_racer = crud.get_racer(db=db, racer_id=racer_id)
    if db_racer is None:
        raise HTTPException(status_code=404, detail="Racer not found")
    return db_racer

@router.put("/{racer_id}", response_model=schemas.RacerResponse)
def update_racer(racer_id: int, racer: schemas.RacerUpdate, db: Session = Depends(get_db)):
    return crud.update_racer(db=db, racer_id=racer_id, racer=racer)

@router.delete("/{racer_id}", response_model=schemas.RacerResponse)
def delete_racer(racer_id: int, db: Session = Depends(get_db)):
    return crud.delete_racer(db=db, racer_id=racer_id)
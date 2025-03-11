from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import racer_crud
from ..schemas import racer, common
from ..database import get_db
from .. import oauth2

router = APIRouter(prefix="/racers", tags=["racers"])

@router.post("/", response_model=racer.RacerResponse)
def create_racer(racer: racer.RacerCreate, db: Session = Depends(get_db)):
    return racer_crud.create_racer(db=db, racer=racer)

@router.get("/", response_model=List[racer.RacerResponse])
def get_racers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return racer_crud.get_racers(db=db, skip=skip, limit=limit)

@router.get("/{racer_id}", response_model=racer.RacerResponse)
def get_racer(racer_id: int, db: Session = Depends(get_db)):
    return racer_crud.get_racer(db=db, racer_id=racer_id)


@router.put("/{racer_id}", response_model=racer.RacerResponse)
def update_racer(
    racer_id: int, 
    racer: racer.RacerUpdate, 
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    return racer_crud.update_racer(db=db, racer_id=racer_id, racer=racer)

@router.delete("/{racer_id}", response_model=common.DeleteResponse)
def delete_racer(racer_id: int, db: Session = Depends(get_db)):
    return racer_crud.delete_racer(db=db, racer_id=racer_id)
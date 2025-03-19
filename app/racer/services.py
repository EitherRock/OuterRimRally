from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .schemas import RacerCreate, RacerUpdate
from .models import Racer

from ..rank.services import get as get_rank_by_id
from ..database.services import get_by_name
from ..util import hash_password


def create(db: Session, racer: RacerCreate):
    existing_racer = get_by_name(db=db, model=Racer, name=racer.name)
    existing_rank = get_rank_by_id(db=db, rank_id=racer.rank_id)

    if existing_racer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Racer with name {racer.name} already taken'
        )
    
    if not existing_rank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Rank with id {racer.rank_id} does not exist'
        )

    new_racer = Racer(
        name=racer.name,
        password_hash=hash_password(racer.password),
        rank_id=racer.rank_id,
        races_attended=racer.races_attended,
        credits=racer.credits
    )

    db.add(new_racer)
    db.commit()
    db.refresh(new_racer)
    return new_racer

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Racer).offset(skip).limit(limit).all()

def get(db: Session, racer_id: int):
    db_racer = db.query(Racer).filter(Racer.id == racer_id).first()

    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer id {racer_id} not found"
        )
    
    return db_racer 


def update(db: Session, racer_id: int, racer: RacerUpdate):
    db_racer = db.query(Racer).filter(Racer.id == racer_id).first()

    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer with id {racer_id} not found"
        )
    
    update_data = {}

    if racer.name is not None:
        existing_name = db.query(Racer).filter(Racer.id != racer_id).filter(Racer.name == racer.name).first()
        if existing_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Racer name {racer.name} already taken'
            )
        
        update_data['name'] = racer.name
    
    if racer.credits is not None:
        if racer.credits < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Credits cannot be negative"
            )

        update_data['credits'] = racer.credits

    if racer.races_attended is not None:
        update_data['races_attended'] = racer.races_attended
    
    if racer.rank_id is not None:
        update_data['rank_id'] = racer.rank_id

    if racer.password:
        update_data['password_hash'] = racer.password

    if update_data:
        db.query(Racer).filter(Racer.id == racer_id).update(update_data)
        db.commit()
        db.refresh(db_racer)

    return db_racer

def delete(db: Session, racer_id: int):
    db_racer = db.query(Racer).filter(Racer.id == racer_id).first()
    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer with id {racer_id} not found"
        )

    db.delete(db_racer)
    db.commit()
    return {"message": "Racer deleted successfully"}
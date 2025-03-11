from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models
from ..schemas import racer
from fastapi import HTTPException, status
from ..util import hash_password


def get_racer_by_name(db: Session, racer_name: str):
    db_racer = db.query(models.Racer).filter(models.Racer.name == racer_name).first()
    return db_racer

def create_racer(db: Session, racer: racer.RacerCreate):
    existing_racer = get_racer_by_name(db, racer.name)

    if existing_racer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Racer with name {racer.name} already taken"
        )

    new_racer = models.Racer(
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

def get_racers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Racer).offset(skip).limit(limit).all()

def get_racer(db: Session, racer_id: int):
    db_racer = db.query(models.Racer).filter(models.Racer.id == racer_id).first()

    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer id {racer_id} not found"
        )
    
    return db_racer 


def update_racer(db: Session, racer_id: int, racer: racer.RacerUpdate):
    db_racer = db.query(models.Racer).filter(models.Racer.id == racer_id).first()

    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer with id {racer_id} not found"
        )
    
    update_data = {}

    if racer.name is not None:
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
        db.query(models.Racer).filter(models.Racer.id == racer_id).update(update_data)
        db.commit()
        db.refresh(db_racer)

    return db_racer

def delete_racer(db: Session, racer_id: int):
    db_racer = db.query(models.Racer).filter(models.Racer.id == racer_id).first()
    if not db_racer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Racer with id {racer_id} not found"
        )

    db.delete(db_racer)
    db.commit()
    return {"message": "Racer deleted successfully"}
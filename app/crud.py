from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas
from fastapi import HTTPException, status

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_racer(db: Session, racer: schemas.RacerCreate):
    racer = models.Racer(
        name=racer.name,
        password_hash=hash_password(racer.password),
        rank_id=racer.rank_id,
        races_attended=racer.races_attended,
        credits=racer.credits
    )

    db.add(racer)
    db.commit()
    db.refresh(racer)
    return racer

def get_racers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Racer).offset(skip).limit(limit).all()

def get_racer(db: Session, racer_id: int):
    return db.query(models.Racer).filter(models.Racer.id == racer_id).first()

def update_racer(db: Session, racer_id: int, racer: schemas.RacerUpdate):
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
                detail="Credits cannot be negative."
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


def create_rank(db: Session, rank: schemas.RankCreate):
    db_rank = models.Rank(
        name=rank.name,
        credits_first=rank.credits_first,
        credits_second=rank.credits_second,
        credits_third=rank.credits_third
    )

    try:
        db.add(db_rank)
        db.commit()
        db.refresh(db_rank)
        return db_rank
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= f"Rank with name '{rank.name}' already exists."
        )

def get_ranks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rank).offset(skip).limit(limit).all()

def get_rank(db: Session, rank_id: int):
    return db.query(models.Rank).filter(models.Rank.id == rank_id).first()

def update_rank(db: Session, rank_id: int, rank: schemas.RankUpdate):
    db_rank = db.query(models.Rank).filter(models.Rank.id == rank_id).first()

    if not db_rank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rank with id {rank_id} not found"
        )
    
    update_data = {}

    if rank.name is not None:
        update_data['name'] = rank.name
    
    if rank.credits_first is not None:
        if rank.credits_first < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="credits_first cannot be negative"
            )
        
        update_data['credits_first'] = rank.credits_first
    
    if rank.credits_second is not None:
        if rank.credits_second < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="credits_second cannot be negative"
            )
        
        update_data['credits_second'] = rank.credits_second
    
    if rank.credits_third is not None:
        if rank.credits_third < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="credits_third cannot be negative"
            )
        
        update_data['credits_third'] = rank.credits_third

    if update_data:
        db.query(models.Rank).filter(models.Rank.id == rank_id).update(update_data)
        db.commit()
        db.refresh(db_rank)
    
    return db_rank

def delete_rank(db: Session, rank_id: int):
    db_rank = db.query(models.Rank).filter(models.Rank.id == rank_id).first()
    if not db_rank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Rank with id {rank_id} not found'
        )
    
    db.delete(db_rank)
    db.commit()
    return {"message": "Rank deleted successfully"}
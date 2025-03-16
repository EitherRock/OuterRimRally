from sqlalchemy.orm import Session
from .models import Rank
from .schemas import RankCreate, RankUpdate, RankResponse
from fastapi import HTTPException, status

def get_by_name(db: Session, rank_name: str):
    return db.query(Rank).filter(Rank.name == rank_name).first()

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Rank).offset(skip).limit(limit).all()

def get(db: Session, rank_id: int):
    return db.query(Rank).filter(Rank.id == rank_id).first()

def create(db: Session, rank: RankCreate):
    existing_rank = get_by_name(db=db, rank_name=rank.name)

    if existing_rank:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Rank with name {rank.name} already exists"
        )
    
    new_rank = Rank(
        name=rank.name,
        credits_first=rank.credits_first,
        credits_second=rank.credits_second,
        credits_third=rank.credits_third
    )

    db.add(new_rank)
    db.commit()
    db.refresh(new_rank)
    return new_rank

def update(db: Session, rank_id: int, rank: RankUpdate):
    db_rank = db.query(Rank).filter(Rank.id == rank_id).first()

    if not db_rank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rank with id {rank_id} not found"
        )
    
    update_data = {}

    if rank.name is not None:
        existing_rank_name = db.query(Rank).filter(Rank.name == rank.name).first()

        if existing_rank_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Rank with name {rank.name} already exists'
            )
        
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
        db.query(Rank).filter(Rank.id == rank_id).update(update_data)
        db.commit()
        db.refresh(db_rank)
    
    return db_rank

def delete(db: Session, rank_id: int):
    db_rank = db.query(Rank).filter(Rank.id == rank_id).first()
    if not db_rank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Rank with id {rank_id} not found'
        )
    
    db.delete(db_rank)
    db.commit()
    return {"message": "Rank deleted successfully"}
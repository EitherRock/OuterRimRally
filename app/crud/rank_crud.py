from sqlalchemy.orm import Session
from .. import models
from ..schemas import rank
from fastapi import HTTPException, status



def get_ranks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rank).offset(skip).limit(limit).all()

def get_rank(db: Session, rank_id: int):
    return db.query(models.Rank).filter(models.Rank.id == rank_id).first()

def update_rank(db: Session, rank_id: int, rank: rank.RankUpdate):
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
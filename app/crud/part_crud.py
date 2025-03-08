from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models
from ..schemas import part
from fastapi import HTTPException, status
from ..util import hash_password
from datetime import datetime

def create_part(db: Session, part: part.PartCreate):
    new_part = models.Part(
        name=part.name,
        category_id=part.category_id,
        description=part.description,
        price=part.price,
        stock_quantity=part.stock_quantity 
    )

    db.add(new_part)
    db.commit()
    db.refresh(new_part)
    return new_part

def get_parts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Part).offset(skip).limit(limit).all()

def get_part(db: Session, part_id: int):
    return db.query(models.Part).filter(models.Part.id == part_id).first()

def update_part(db: Session, part_id: int, part: part.PartUpdate):
    db_part = db.query(models.Part).filter(models.Part.id == part_id).first()

    if not db_part:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part with id {part_id} not found"
        )
    
    update_data = {}

    if part.name is not None:
        update_data['name'] = part.name

    if part.category_id is not None:
        update_data['category_id'] = part.category_id
    
    if part.description is not None:
        update_data['description'] = part.description
    
    if part.price is not None:
        if part.price < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price cannot be negative"
            )
        
        update_data['price'] = part.price
    
    if part.stock_quantity is not None:
        if part.stock_quanity < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Stock quantity cannot be negative"
            )
    
    update_data['updated'] = datetime.now(datetime.timezone.utc)

    if update_data:
        db.query(models.Part).filter(models.Part.id == part_id).update(update_data)
        db.commit()
        db.refresh(db_part)
    
    return db_part

def delete_part(db: Session, part_id: int):
    db_part = db.query(models.Part).filter(models.Part.id == part_id).first()

    if not db_part:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part with id {part_id} not found"
        )
    
    db.delete(db_part)
    db.commit()
    return {"message": "Part deleted successfully"}
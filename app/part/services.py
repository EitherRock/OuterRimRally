from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

from .models import Part
from .schemas import PartCreate, PartUpdate

from ..category.models import Category


def create(db: Session, part: PartCreate):
    new_part = Part(
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

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Part).offset(skip).limit(limit).all()

def get(db: Session, part_id: int):
    db_part = db.query(Part).filter(Part.id == part_id).first()
    
    if not db_part:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part id {part_id} not found"
        )
    
    return db_part

def update(db: Session, part_id: int, part: PartUpdate):
    db_part = db.query(Part).filter(Part.id == part_id).first()

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
        db.query(Part).filter(Part.id == part_id).update(update_data)
        db.commit()
        db.refresh(db_part)
    
    return db_part

def delete(db: Session, part_id: int):
    db_part = db.query(Part).filter(Part.id == part_id).first()

    if not db_part:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Part with id {part_id} not found"
        )
    
    db.delete(db_part)
    db.commit()
    return {"message": "Part deleted successfully"}

def create_stock_parts(db: Session):
    power_source_category = Category(name='Power Source')
    propulsion_category = Category(name='Propulsion')
    handling_category = Category(name='Handling')
    print('jel;l')

    db.add_all([power_source_category, propulsion_category, handling_category])
    db.commit()

    stock_power_source = Part(name='Stock', category_id=power_source_category.id)
    stock_propulsion = Part(name='Stock', category_id=propulsion_category.id)
    stock_handling = Part(name='Stock', category_id=handling_category.id)

    db.add_all([stock_power_source, stock_propulsion, stock_handling])
    db.commit()
    
    return [stock_power_source, stock_propulsion, stock_handling]
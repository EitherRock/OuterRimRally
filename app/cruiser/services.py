from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

from .models import Cruiser
from .schemas import CruiserCreate, CruiserUpdate, CruiserResponse

from ..database.services import get_by_name
from ..racer.services import get as get_racer_by_id 
from ..part.services import get as get_part_by_id
from ..category.enums import Categories


def create(db: Session, cruiser: CruiserCreate):
    existing_cruiser = get_by_name(db=db, model=Cruiser, name=cruiser.name)
    if existing_cruiser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Cruiser with name {cruiser.name} already exists'
        )
    
    existing_racer = get_racer_by_id(db=db, racer_id=cruiser.racer_id)
    if existing_racer and existing_racer.cruiser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Racer with id {cruiser.racer_id} already has a cruiser'
        )
    
    total_rating = Cruiser.calculate_total_rating(
        db=db, 
        power_source_id=cruiser.power_source_id,
        propulsion_id=cruiser.propulsion_id,
        handling_id=cruiser.handling_id
    )

    new_cruiser = Cruiser(
        name=cruiser.name,
        racer_id=cruiser.racer_id,
        power_source_id=cruiser.power_source_id,
        propulsion_id=cruiser.propulsion_id,
        handling_id=cruiser.handling_id,
        total_rating=total_rating
    )

    db.add(new_cruiser)
    db.commit()
    db.refresh(new_cruiser)

    return new_cruiser

def get(db: Session, cruiser_id: int):
    db_cruiser = db.query(Cruiser).filter(Cruiser.id == cruiser_id).first()

    if not db_cruiser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cruiser id {cruiser_id} not found"
        )
    
    return db_cruiser 

def update(db: Session, cruiser_id: int, cruiser: CruiserUpdate):
    get(db=db, cruiser_id=cruiser_id)

    update_data = {}

    if cruiser.name is not None:
        existing_name = get_by_name(db=db, model=Cruiser, name=cruiser.name)

        if existing_name and existing_name.id != cruiser_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Cruiser name {cruiser.name} already taken'
            )

        update_data['name'] = cruiser.name
    
    if cruiser.racer_id is not None:
        existing_racer = get_racer_by_id(db=db, racer_id=cruiser.racer_id)

        if existing_racer and existing_racer.cruiser:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Racer with id {cruiser.racer_id} already has a cruiser'
            )
        
        update_data['racer_id'] = cruiser.racer_id
    
    if cruiser.power_source_id is not None:
        existing_power_source = get_part_by_id()

from sqlalchemy.orm import Session
from .models import Category
from .schemas import CategoryCreate
from fastapi import HTTPException, status

def create(db: Session, category: CategoryCreate):
    new_category = Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category
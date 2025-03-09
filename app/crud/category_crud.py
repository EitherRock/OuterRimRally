from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models
from ..schemas import category
from fastapi import HTTPException, status
from ..util import hash_password
from datetime import datetime

def create_category(db: Session, category: category.CategoryCreate):
    new_category = models.Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category
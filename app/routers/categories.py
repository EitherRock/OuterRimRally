from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..crud import category_crud
from ..schemas import category, common
from ..database import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=category.CategoryResponse)
def create_category(category: category.CategoryCreate, db: Session = Depends(get_db)):
    print(category)
    return category_crud.create_category(db=db, category=category)
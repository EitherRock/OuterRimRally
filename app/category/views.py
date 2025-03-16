from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .services import create
from .schemas import CategoryCreate, CategoryResponse
from ..database.core import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    print(category)
    return create(db=db, category=category)
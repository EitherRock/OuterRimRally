from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import TypeVar

from .core import Base


def get_by_name(db: Session, model: Base, name: str): # type: ignore
    model_by_name = db.query(model).filter(model.name == name).first()
    return model_by_name
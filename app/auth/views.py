from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .schemas import Token
from .services import create_access_token
from ..racer.models import Racer
from ..database.core import get_db
from .. import util


router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    racer =  db.query(Racer).filter(
        Racer.name == user_credentials.username).first()
    
    if not racer or not util.verify(user_credentials.password, racer.password_hash):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )
    
    # if not util.verify(user_credentials.password, racer.password):
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Invalid Credentials"
    #     )
    
    access_token = create_access_token(data={"user_id": racer.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
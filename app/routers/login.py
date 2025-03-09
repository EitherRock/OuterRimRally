from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import util, models, oauth2
from ..schemas import auth_schema


router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=auth_schema.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    print("start here")
    print(user_credentials.username)
    racer =  db.query(models.Racer).filter(
        models.Racer.name == user_credentials.username).first()
    print(racer)
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
    
    access_token = oauth2.create_access_token(data={"user_id": racer.id})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
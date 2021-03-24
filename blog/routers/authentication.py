from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,database,models,token
from passlib.context import CryptContext
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

router = APIRouter(
    tags=['authentication']
)

get_db = database.get_db

@router.post('/login')
def  login(request:OAuth2PasswordRequestForm=Depends(),db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == 
    request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"invalid Credentials"
        )
    if not pwd_cxt.verify(request.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"invalid Credentials"
        )
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
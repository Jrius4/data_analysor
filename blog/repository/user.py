from fastapi import status,Response,HTTPException
from sqlalchemy.orm import Session
from .. import schemas,models
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")


def all(db:Session):
    users = db.query(models.User).all()
    return users

def show(id:int,response:Response,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with the id {id} is not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':}
    return user

def create(request:schemas.User,db:Session):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashedPassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
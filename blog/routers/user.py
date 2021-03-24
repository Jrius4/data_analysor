from fastapi import APIRouter,Depends,status,Response
from sqlalchemy.orm import Session
from typing import List

from ..repository import user
from .. import schemas,database

router = APIRouter(
    prefix='/users',
    tags=['users']
)
get_db = database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def get_user(id:int,response:Response,db:Session=Depends(get_db)):
    return user.show(id,response,db)


@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def all_users(db:Session=Depends(get_db)):
    return user.all(db)


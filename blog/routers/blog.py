from fastapi import APIRouter,Depends,status,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,database,Oauth
from ..repository import blog
 
router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)
get_db = database.get_db


@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def all_blogs(db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth.get_current_user)):
    return blog.all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth.get_current_user)):
    return blog.show(id,response,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth.get_current_user)):
    return blog.destory(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(Oauth.get_current_user)):
    return blog.update(id,request,db)
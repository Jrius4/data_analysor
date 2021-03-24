from fastapi import status,Response,HTTPException
from sqlalchemy.orm import Session

from .. import schemas,models
from datetime import datetime

def all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(id:int,response:Response,db:Session,):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':}
    return blog

def create(request:schemas.Blog,db:Session):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        published=request.published,
        user_id=2
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def update(id:int,request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == 
    id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
    
    blog.update(
        {'title':request.title,
        'body':request.body,
        'published':request.published,
        'updated_at':datetime.now()
        },synchronize_session=False)
    db.commit()
    return {'detail':'updated successfully'}

def destory(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
    
    blog.delete(synchronize_session=False)

    db.commit()

    return {'detail':'deleted successfully'}

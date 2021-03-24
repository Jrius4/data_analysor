import datetime
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name:str
    email:str
    password:str

class BlogBase(BaseModel):
    title:str
    body:str
    published:bool=False
class Blog(BlogBase):
    class Config():
        orm_mode = True
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []
    class Config():
        orm_mode = True




class ShowBlog(BaseModel):
    title:str
    body:str
    created_at:datetime.datetime
    updated_at:datetime.datetime
    published:bool
    creator:ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None
        
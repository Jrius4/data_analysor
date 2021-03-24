from sqlalchemy import func, Column,Integer,ForeignKey,String, Boolean,DateTime
from .database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User',back_populates="blogs")
    created_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )
    updated_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog',back_populates="creator")
    created_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )
    updated_at = Column(
           DateTime,
           default=datetime.utcnow(),
            server_default=func.now(),
            nullable=False,
            index=True,
        )

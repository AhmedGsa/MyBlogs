from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    userId = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates='blogs')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates='author')
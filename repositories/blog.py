import models
from sqlalchemy.orm import Session
from schemas import Blog
from fastapi import HTTPException

def get_all(db: Session, limit: int, offset: int):
    blogs = db.query(models.Blog).offset(0).limit(limit).all()
    return blogs

def get_one(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found!")
    return blog

def create(db: Session, newBlog: Blog):
    blog = models.Blog(title = newBlog.title, userId = 1)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def update(db: Session, id: int, newBlog: Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail="Blgo not found!")
    blog.update({"title": newBlog.title}, synchronize_session=False)
    db.commit()

def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found!")
    blog.delete(synchronize_session=False)
    db.commit()
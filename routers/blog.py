from fastapi import APIRouter, Depends
from typing import Optional
from database import get_db
from schemas import Blog, BlogResponse
from sqlalchemy.orm import Session
from repositories import blog as BlogRepository
from jwt import JWT


router = APIRouter(prefix='/blogs', tags=['Blogs'])

@router.get("", response_model=list[BlogResponse])
def get_all_blogs(page: int = 1, pageSize: int = 3, sort: Optional[str] = None, db: Session = Depends(get_db)):
    return BlogRepository.get_all(db, offset=pageSize * (page - 1), limit=pageSize)

@router.get("/{id}", response_model=BlogResponse)
def get_single_blog(id: int, db: Session = Depends(get_db)):
    return BlogRepository.get_one(db, id)
    
@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), user = Depends(JWT.verify_token)):
    BlogRepository.delete(db, id)
    return {"msg": "Blog deleted successfully !"}

@router.patch("/{id}")
def update_blog(id: int, newBlog: Blog, db: Session = Depends(get_db), user = Depends(JWT.verify_token)):
    BlogRepository.update(db, id, newBlog)
    return {"msg": "Blog updated successfully !"}
    

@router.post("/", status_code=201)
def create_blog(newBlog: Blog, db: Session = Depends(get_db), user = Depends(JWT.verify_token)):
    blog = BlogRepository.create(db, newBlog)
    return {"msg": "Blog created successfully!", "blog": blog}
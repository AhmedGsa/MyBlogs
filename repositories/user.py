from sqlalchemy.orm import Session
from schemas import User
from hashing import Hash
from fastapi import status, HTTPException
import models

def create(db: Session, userSchema: User):
    user = models.User(email = userSchema.email, password = Hash.bcrypt(userSchema.password), fullname = userSchema.fullname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_one(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with provided id not found !")
    return user

def find_one_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    return user
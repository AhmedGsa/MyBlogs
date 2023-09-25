from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from schemas import UserResponse, User, LoginSchema
from repositories import user as UserRepository
from hashing import Hash
from jwt import JWT

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post("/register", response_model=UserResponse)
def register(userSchema: User, db: Session = Depends(get_db)):
    return UserRepository.create(db, userSchema)

@router.post("/login")
def login(loginSchema: LoginSchema, db: Session = Depends(get_db)):
    user = UserRepository.find_one_by_email(db, loginSchema.email)
    match = Hash.compare(user.password, loginSchema.password)
    if not match:
        raise HTTPException(400, detail='Invalid Credentials')
    token = JWT.create_token({"id": user.id, "email": user.email})
    return {"token": token, "msg": "Logged in successfully !"}

@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return UserRepository.get_one(db, id)
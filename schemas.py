from pydantic import BaseModel

class Blog(BaseModel):
    title: str

class UserInfo(BaseModel):
    fullname: str
    email: str

class User(UserInfo):
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    fullname: str
    email: str
    blogs: list[Blog]

class BlogResponse(Blog):
    author: UserInfo
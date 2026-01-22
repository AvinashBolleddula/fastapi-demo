from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config:
        orm_mode = True

# ShowBlog inherits from Blog to include all its fields
# this is used for response models to include ORM mode
# this helps to get info only we need to show
class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser  # Nested user schema
    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    

from fastapi import FastAPI
from typing import Optional
# for post request body to work
from pydantic import BaseModel
# to change port running using python3 main.py
import uvicorn
app = FastAPI()

# Basic route
@app.get("/")
def index():
    return {'data': 'blog list'}

# Query Parameters
@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}

# Specific routes should be defined before dynamic routes
@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}

# Dynamic route with path parameter
@app.get("/blog/{id}")
# id should be int
def show(id: int):
    return {'data': id}

# Nested dynamic route
@app.get("/blog/{id}/comments")
def comments(id):
    return {'data': f'comments for blog {id}'}

# Pydantic model for request body
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



# POST route to create a blog
# uses the Blog model to parse request body
# post gets values from user in json format
@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': f'blog is created with title {blog.title}'}

#if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=9000)
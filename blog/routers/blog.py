from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schema, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
get_db = database.get_db
router = APIRouter(prefix='/blog', tags=['Blogs'])

# GET ALL BLOGS
# list is used to return multiple blogs
# here we added to route to get current user
@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# CREATE BLOG
# request is what we receive from the user in swagger
# need request for get and put methods
# what ever columns you give here, those values will be required in swagger
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

# DELETE BLOG
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

# UPDATE BLOG
# this is bulk update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


# GET BLOG BY ID
@router.get('/{id}', response_model=schema.ShowBlog,status_code=200)
def show(id: int, response: Response,db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)



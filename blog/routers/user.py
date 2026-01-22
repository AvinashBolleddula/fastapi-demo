from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, models, database
from sqlalchemy.orm import Session
get_db = database.get_db
from ..hashing import Hash
from ..repository import user


router = APIRouter(prefix='/user', tags=['Users'])


# create user schema in shcma.py (name, email, password)
# store user in db (no hashing for now)
# we need to create user model in models.py along with blog model
@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)

# GET USER BY ID    
@router.get('/{id}', response_model=schema.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
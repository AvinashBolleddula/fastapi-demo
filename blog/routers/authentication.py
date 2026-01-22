from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .. import schema, database, models, token
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    
    access_token = token.create_access_token(
        data={"sub": user.email})
    return schema.Token(access_token=access_token, token_type="bearer")

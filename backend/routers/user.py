from fastapi import APIRouter, Depends
from routers.schemas import UserDisplay
from sqlalchemy.orm.session import Session
from .schemas import UserBase
from db.database import get_db
from db import user_db

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user_db.create_user(db=db, request=request)

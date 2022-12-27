from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from routers.schemas import PostDisplay, PostBase
from db import post_db
from typing import List

router = APIRouter(prefix="/post", tags=["POST"])

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Parameter image_url_type can only types .."
        )
    return post_db.create(db=db, request=request)


@router.get("/all", response_model=List[PostDisplay])
def select_all_posts(db: Session = Depends(get_db)):
    return post_db.get_all(db=db)

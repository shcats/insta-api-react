from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from routers.schemas import PostDisplay, PostBase
from db import post_db
from typing import List
import random
import string
import shutil
from routers.schemas import UserAuth

router = APIRouter(prefix="/post", tags=["POST"])

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Parameter image_url_type can only types .."
        )
    return post_db.create(db=db, request=request)


@router.get("/all", response_model=List[PostDisplay])
def select_all_posts(db: Session = Depends(get_db)):
    return post_db.get_all(db=db)


@router.post("/image")
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    rand_str = "_" + "".join(random.choice(string.ascii_letters) for i in range(6))
    filename = rand_str.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}.jpeg"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": filename}


@router.get("/delete/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return post_db.delete_post_by_id(db=db, id=id, user_id=current_user.id)

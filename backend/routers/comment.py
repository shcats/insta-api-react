from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_comment
from routers.schemas import CommentBase, UserAuth
from auth import oauth2

router = APIRouter(prefix="/comment", tags=["Comments"])


@router.get("/all/{post_id}")
def comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db=db, post_id=post_id)


@router.post("")
def create_new_post(
    request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(oauth2.get_current_user)
):
    return db_comment.create(db=db, request=request)

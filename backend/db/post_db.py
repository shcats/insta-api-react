from sqlalchemy.orm.session import Session
from routers.schemas import PostBase
from db.models import DbPost
from datetime import datetime
from fastapi import HTTPException, status


def create(db: Session, request: PostBase):
    post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all(db: Session):
    return db.query(DbPost).all()


def delete_post_by_id(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"That user does not create this post")
    db.delete(post)
    db.commit()
    return "Post was deleted"

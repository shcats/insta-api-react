from sqlalchemy.orm.session import Session
from routers.schemas import PostBase
from db.models import DbPost
from datetime import datetime

def create(db:Session, request: PostBase):
    post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.creator_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
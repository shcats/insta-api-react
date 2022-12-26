from fastapi import APIRouter
from routers.schemas import PostDisplay, PostBase

router = APIRouter(
    prefix="/post",
    tags=["POST"]
)


@router.post("", response_model=PostDisplay)
def create_post(request:PostBase, ):
    ...
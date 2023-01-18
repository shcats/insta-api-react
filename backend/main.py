from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import database
from db.database import engine
from routers import comment
from routers import user
from routers import post
from auth import authentification
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentification.router)
app.include_router(comment.router)


@app.get("/")
def root():
    return {"text": "Hello World"}


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)

database.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")

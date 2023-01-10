from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import database
from db.database import engine
from routers import user
from routers import post
from auth import authentification

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentification.router)

@app.get("/")
def root():
    return {"text": "Hello World"}


database.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")

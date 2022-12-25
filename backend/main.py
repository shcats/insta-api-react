from fastapi import FastAPI
from db import database
from db.database import engine
from routers import user

app = FastAPI()
app.include_router(user.router)



@app.get("/")
def root():
    return {"text":"Hello World"}


database.Base.metadata.create_all(engine)
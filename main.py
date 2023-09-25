from fastapi import FastAPI
from database import engine
from routers import auth, blog
import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(auth.router)

@app.get("/")
def hello():
    return {"msg": "Hello World"}

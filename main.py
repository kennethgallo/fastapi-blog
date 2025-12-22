
from fastapi import FastAPI
from db import models
from router import blog_get, blog_post, user
from db.database import engine

# pip install dark_swag
from dark_swag import get_dark_router

app = FastAPI(docs_url=None)

app.include_router(get_dark_router(app))
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)

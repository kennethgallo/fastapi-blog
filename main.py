
from fastapi import FastAPI
from db import models
from router import blog_get, blog_post
from db.database import engine

# pip install dark_swag
from dark_swag import get_dark_router

# Create ONE FastAPI app, disable default /docs so dark_swag can mount its own.
app = FastAPI(docs_url=None)

# Mount DarkSwag's router (serves dark-mode Swagger UI and assets at /docs)
app.include_router(get_dark_router(app))

# Include your application routers
app.include_router(blog_get.router)
app.include_router(blog_post.router)

# Example endpoint
@app.get("/hello")
def index():
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)

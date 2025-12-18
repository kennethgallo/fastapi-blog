from fastapi import FastAPI, APIRouter
from router import blog_get, blog_post

# pip install fastapi-swagger-dark
import fastapi_swagger_dark as fsd

app = FastAPI(docs_url=None)

docs_router = APIRouter()
fsd.install(
    docs_router,
    path="/docs",
    swagger_ui_parameters={
        "deepLinking": True,
        "docExpansion": "list",
        # Vivid syntax highlighting inside code blocks
        "syntaxHighlight": {"theme":"dracula"},  
    },
)
app.include_router(docs_router)

app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/hello")
def index():
    return {"message": "Hello World"}

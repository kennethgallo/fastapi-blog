from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    num_of_comments: int
    published: bool | None = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog.model_dump(),
        'version': version
        }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, comment_id: int = Query(None, title='Id of the comment',
                   description='Some descritopn for comment ID', alias='commentId', deprecated=True), 
                   content: str = Body(...)):
    return {'blog': blog, 'id': id, 'comment_id': comment_id, 'content': content}
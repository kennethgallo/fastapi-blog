from typing import List, Optional, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    num_of_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key': 'value'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog.model_dump(),
        'version': version
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None, title='Title of the comment',
                   description='Some descritopn for comment_title', alias='commentTitle', 
                   deprecated=True), 
                   content: str = Body(..., min_length=5, max_length=50, regex='^[a-z\s]*$'),
                   v: Optional[List[str]] = Query(['v1.0', 'v1.1', 'v1.2']),
                   comment_id: int = Path(..., gt=5, le=10)
                   ):
    return {'blog': blog, 'id': id, 'comment_id': comment_title, 'content': content, 
            'version': v, 'comment_id': comment_id}
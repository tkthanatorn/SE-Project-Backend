from fastapi import APIRouter
from .usecase import SearchTags

tags_router = APIRouter(prefix='/tags')


@tags_router.get('/')
def search():
    result = SearchTags('b')
    return {
        'data': result
    }

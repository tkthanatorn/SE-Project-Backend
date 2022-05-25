from fastapi import APIRouter

from routes.tags.db import GetTagsByNewsID
from .usecase import SearchTags

tags_router = APIRouter(prefix='/tags')


@tags_router.get('/search')
def search(value: str, limit: int = 5):
    try:
        result = SearchTags(search=value, limit=limit)
        return {
            'data': result,
            'status': 200
        }
    except:
        return{
            'status': 400
        }


@tags_router.get('/byNews')
def byNewsID(news_id: int):
    try:
        result = GetTagsByNewsID(news_id)
        return {
            'data': result,
            'status': 200
        }
    except:
        return {
            'status': 400
        }

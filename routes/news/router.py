from fastapi import APIRouter
from .usecase import GetNews

news_router = APIRouter(prefix='/news')


@news_router.get('/')
async def getNews(limit: int = 100, page: int = 1,  order_by: str = 'desc'):
    limit = limit if limit <= 100 else 100

    try:
        result = GetNews(limit=limit, offset=page, order_by=order_by)
        return {
            'data': result,
            'status': 200
        }
    except:
        return {
            'status': 400
        }

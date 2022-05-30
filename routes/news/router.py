from fastapi import APIRouter
from .usecase import GetNews, SearchNewsByTagsID

news_router = APIRouter(prefix='/news')


@news_router.get('/')
async def getNews(limit: int = 50, page: int = 1,  order_by: str = 'desc', start: int = 0, end: int = 0):
    try:
        limit = limit if limit <= 100 else 1000
        result = GetNews(limit=limit, offset=page,
                         order_by=order_by, start=start, end=end)
        return {
            'data': result,
            'status': 200
        }
    except:
        return {
            'status': 400
        }


@news_router.get('/by_tag')
def searchNewsByTag(tags_id: int, limit: int = 100, page: int = 1, order_by: str = 'desc', start: int = 0, end: int = 0):
    try:
        limit = limit if limit <= 100 else 100
        data = SearchNewsByTagsID(
            tags_id=tags_id, limit=limit, offset=page, order_by=order_by, start=start, end=end)
        return {
            'data': data,
            'status': 200
        }
    except:
        return {
            'status': 400
        }

from fastapi import APIRouter
from .usecase import GetNews

news_router = APIRouter(prefix='/news')


@news_router.get('/')
async def getNews(limit: int = 100, order_by: str = 'desc'):
    # db.cursor.execute(
    #     'select id, title, description, text, icon, date from news;')
    # data = db.cursor.fetchall()
    # result = []
    # for item in data:
    #     db.cursor.execute(
    #         f"select tags_id from news_tags where news_id={item[0]}")
    #     tags_id = db.cursor.fetchall()

    #     tags = []
    #     for tag_id in tags_id:
    #         print(tag_id)
    #         db.cursor.execute(f"select * from tags where id={tag_id[0]};")
    #         tag = db.cursor.fetchall()[0]
    #         tags.append({
    #             'id': tag[0],
    #             'name': tag[1],
    #             'key': tag[2],
    #             'symbol': tag[3],
    #         })

    #     result.append({
    #         'id': item[0],
    #         'title': item[1],
    #         'description': item[2],
    #         'text': item[3],
    #         'icon': item[4],
    #         'tags': tags,
    #         'date': item[5],
    #     })
    try:
        result = GetNews(limit=limit, order_by=order_by)
        return {
            'data': result,
            'status': 200
        }
    except:
        return {
            'data': [],
            'status': 400
        }

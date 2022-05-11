from fastapi import APIRouter
from db import Database

news_router = APIRouter()
db = Database()


@news_router.get('/')
async def all():
    db.cursor.execute(
        'select id, title, description, text, icon, date from news;')
    data = db.cursor.fetchall()
    result = []
    for item in data:
        db.cursor.execute(
            f"select tags_id from news_tags where news_id={item[0]}")
        tags_id = db.cursor.fetchall()

        tags = []
        for tag_id in tags_id:
            print(tag_id)
            db.cursor.execute(f"select * from tags where id={tag_id[0]};")
            tag = db.cursor.fetchall()[0]
            tags.append({
                'id': tag[0],
                'name': tag[1],
                'key': tag[2],
                'symbol': tag[3],
            })

        result.append({
            'id': item[0],
            'title': item[1],
            'description': item[2],
            'text': item[3],
            'icon': item[4],
            'tags': tags,
            'date': item[5],
        })

    return {
        'data': result
    }

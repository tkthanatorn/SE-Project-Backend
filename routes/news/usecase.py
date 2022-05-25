from .db import SelectNews
from routes.tags.db import GetTagsByNewsID


def GetNews(limit: int = 100, offset: int = 1, order_by='desc'):
    data = SelectNews(
        cond=[
            # f"where sentiment is not null and polarity is not null",
            f"order by date {order_by}",
            f"limit {limit}", f"offset {offset}"
        ])

    result = []
    for item in data:
        tags = GetTagsByNewsID(item['id'])
        item['tags'] = tags
        result.append(item)

    return result

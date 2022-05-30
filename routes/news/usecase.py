from datetime import datetime
from .db import GetNewsByTagsID, SelectNews
from routes.tags.db import GetTagsByNewsID


def GetNews(limit: int = 100, offset: int = 1, order_by: str = 'desc', start: int = -1, end: int = -1):
    cond = []
    if start > 0 or end > 0:
        cond.append("where")

    if start > 0 and end > 0:
        cond.append(
            f"date>'{datetime.fromtimestamp(start, tz=None).date().__str__()}' and date<'{datetime.fromtimestamp(end, tz=None).date().__str__()}'")
    elif start > 0:
        cond.append(
            f"date>'{datetime.fromtimestamp(start, tz=None).date().__str__()}'")
    elif end > 0:
        cond.append(
            f"date<'{datetime.fromtimestamp(end, tz=None).date().__str__()}'")

    cond.append(f"order by date {order_by}")
    cond.append(f"limit {limit} offset {offset}")
    # f"where sentiment is not null and polarity is not null",

    data = SelectNews(cond=cond)

    result = []
    for item in data:
        tags = GetTagsByNewsID(item['id'])
        item['tags'] = tags
        result.append(item)

    return result


def SearchNewsByTagsID(tags_id: int, limit: int = 100, offset: int = 1, order_by: str = 'desc', start: int = 0, end: int = 0):
    cond = []

    if start > 0 and end > 0:
        cond.append(
            f"and date>'{datetime.fromtimestamp(start, tz=None).date().__str__()}' and date<'{datetime.fromtimestamp(end, tz=None).date().__str__()}'")
    elif start > 0:
        cond.append(
            f"and date>'{datetime.fromtimestamp(start, tz=None).date().__str__()}'")
    elif end > 0:
        cond.append(
            f"and date<'{datetime.fromtimestamp(end, tz=None).date().__str__()}'")

    cond.append(f"order by date {order_by}")
    cond.append(f"limit {limit} offset {offset}")
    data = GetNewsByTagsID(tags_id=tags_id, cond=cond)

    result = []
    for item in data:
        tags = GetTagsByNewsID(item['id'])
        item['tags'] = tags
        result.append(item)

    return result

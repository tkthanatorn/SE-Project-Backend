from .db import SelectNews


def GetNews(limit: int = 100, order_by='desc'):
    return SelectNews(cond=[f"order by date {order_by}", f"limit {limit}"])

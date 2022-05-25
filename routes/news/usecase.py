from .db import SelectNews


def GetNews(limit: int = 100, offset: int = 1, order_by='desc'):
    result = SelectNews(
        cond=[
            # f"where sentiment is not null and polarity is not null",
            f"order by date {order_by}",
            f"limit {limit}", f"offset {offset}"
        ])

    return result

from .db import SelectNews


def LatestNews():
    return SelectNews(cond=['order by date desc'])

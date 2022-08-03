from sqlalchemy.orm import Session
from repository.news_repository import GetNewsRepo


def GetNewsUsecase(db: Session, limit: int, offset: int, since: str, to: str, order_by:str):
    news = GetNewsRepo(db, limit, offset, since, to, order_by)
    data = list()

    for item in news:
        tmp = dict(
            id=item.id,
            title=item.title,
            description=item.description,
            url=item.url,
            source=item.source,
            icon=item.icon,
            sentiment=item.sentiment,
            polarity=item.polarity,
            date=item.date
        )

        tags = list()
        for tag in item.tags:
            tags.append({
                'id': tag.id,
                'name': tag.name,
                'key': tag.key,
                'symbol': tag.symbol
            })
        
        tmp['tags'] = tags
        data.append(tmp)
    return data

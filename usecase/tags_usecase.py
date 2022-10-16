from sqlalchemy.orm import Session
from model import News
from repository.tags_repository import SearchTagsRepo, GetTagsByIDRepo


def SearchTagsUsecase(db: Session, symbol: str, name: str, key: str, limit: int):
    tags = SearchTagsRepo(db, symbol, name, key, limit)
    data = list()

    for tag in tags:
        tmp = dict(id=tag.id, name=tag.name, key=tag.key, symbol=tag.symbol)
        data.append(tmp)
    return data


def GetNewsFromTagsIDUsecase(db: Session, id: int, order_by: str = "desc"):
    tag = GetTagsByIDRepo(db, id)
    data = list()

    news: list[News] = tag.news
    for item in news:
        if item.sentiment:
            tmp = dict(
                id=item.id,
                title=item.title,
                description=item.description,
                url=item.url,
                source=item.source,
                icon=item.icon,
                sentiment=item.sentiment,
                polarity=item.polarity,
                date=item.date,
            )

            tags = list()
            for tag in item.tags:
                tags.append(
                    {
                        "id": tag.id,
                        "name": tag.name,
                        "key": tag.key,
                        "symbol": tag.symbol,
                    }
                )

            tmp["tags"] = tags
            data.append(tmp)

    data.sort(key=lambda item: item["date"], reverse=(order_by == "desc"))
    return data

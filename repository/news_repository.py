from sqlalchemy import or_, desc, asc
from sqlalchemy.orm import Session
from model import News, Tags


def GetNewsRepo(db: Session, limit: int = 100, offset: int = None, since: str = None, to: str = None, order_by: str = "desc", with_tags: list[int] = []) -> list[News]:
    query = db.query(News).filter(or_(News.text.is_not(None), News.sentiment.is_not(None)))

    if len(with_tags):
        query = query.filter(News.tags.any(Tags.id.in_(with_tags)))

    if since and to:
        query = query.filter(and_(News.date >= since, News.date <= to))
    elif since:
        query = query.filter(News.date >= since)
    elif to:
        query = query.filter(News.date <= to)   

    if order_by == "desc":
        query = query.order_by(desc(News.date))
    elif order_by == "asc":
        query = query.order_by(asc(News.date))
    
    if limit:
        query = query.limit(limit)
    
    if offset:
        query = query.offset(offset)
    
    return query.all()
    
        









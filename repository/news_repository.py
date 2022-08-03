from sqlalchemy import and_, desc, asc
from sqlalchemy.orm import Session
from model import News


def GetNewsRepo(db: Session, limit: int = 100, offset: int = None, since: str = None, to: str = None, order_by: str = "desc") -> list[News]:
    query = db.query(News).filter(and_(News.text.is_not(None), News.sentiment.is_not(None)))
    print(limit, offset, since, to)

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
    
        









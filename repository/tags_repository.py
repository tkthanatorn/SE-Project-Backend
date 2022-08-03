from sqlalchemy import or_
from sqlalchemy.orm import Session
from model import Tags


def SearchTagsRepo(db: Session, symbol: str, name: str, limit: int = 100) -> list[Tags]:
    query = db.query(Tags).filter(or_(Tags.symbol.ilike(f"%{symbol}%"), Tags.name.ilike(f"%{name}%"))).limit(limit)
    return query.all()

def GetTagsByIDRepo(db: Session, id: int) -> Tags:
    return db.query(Tags).get(id)
    
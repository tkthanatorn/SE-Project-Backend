from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from usecase.news_usecase import GetNewsUsecase
from base import get_db


news_router = APIRouter(prefix="/news")


@news_router.get('', status_code=status.HTTP_200_OK)
def get_news(limit:int = 100, offset:int = 0, since: str = "", to: str = "", order_by: str = "desc", db: Session = Depends(get_db)):
    try:
        print(limit, offset, since, to, order_by)
        data = GetNewsUsecase(db, limit, offset, since, to, order_by)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())
    
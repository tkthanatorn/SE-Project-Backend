from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from usecase.news_usecase import GetNewsUsecase
from base import get_db


news_router = APIRouter(prefix="/news")


@news_router.get('', status_code=status.HTTP_200_OK)
def get_news(limit:int = 100, offset:int = 1, since: str = "", to: str = "", order_by: str = "desc", with_tags: str = "", db: Session = Depends(get_db)):
    try:
        if with_tags:
            with_tags = [int(id) for id in with_tags.split(",")]
        if offset < 1:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, "offset should be greater than 0")

        data = GetNewsUsecase(db, limit, offset-1, since, to, order_by, with_tags)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())
    
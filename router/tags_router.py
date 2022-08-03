from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from usecase.tags_usecase import SearchTagsUsecase, GetNewsFromTagsIDUsecase
from base import get_db


tags_router = APIRouter(prefix="/tags")


@tags_router.get("", status_code=status.HTTP_200_OK)
def SearchTags(search:str = "", limit: int = 100, db: Session = Depends(get_db)):
    try:
        data = SearchTagsUsecase(db, search, search, search, limit)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())


@tags_router.get("/{id}/news", status_code=status.HTTP_200_OK)
def GetNewsByTagsID(id: int, order_by: str = "desc", db: Session = Depends(get_db)):
    try:
        data = GetNewsFromTagsIDUsecase(db, id, order_by)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())


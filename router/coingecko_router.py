from fastapi import APIRouter, HTTPException, status
from usecase.coingecko import GetHistoricalDataUsecase, GetMarketDataByKeyUsecase, GetMarketDataUsecase


cg_router = APIRouter(prefix="/coingecko")

@cg_router.get("/historical", status_code=status.HTTP_200_OK)
def GetHistorical(key: str="bitcoin"):
    try:
        data = GetHistoricalDataUsecase(id=key)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())

@cg_router.get("/market", status_code=status.HTTP_200_OK)
def GetMarket():
    try:
        data = GetMarketDataUsecase()
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())

@cg_router.get("/market/{key}", status_code=status.HTTP_200_OK)
def GetMarketByKey(key: str):
    try:
        data = GetMarketDataByKeyUsecase(key)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())
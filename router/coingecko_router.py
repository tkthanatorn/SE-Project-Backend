from fastapi import APIRouter, HTTPException, status
from usecase.coingecko import GetHistoricalDataUsecase


cg_router = APIRouter(prefix="/coingecko")

@cg_router.get("/historical", status_code=status.HTTP_200_OK)
def GetHistorical(key: str="bitcoin"):
    try:
        data = GetHistoricalDataUsecase(id=key)
        response = dict(data=data, detail="OK")
        return response
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, e.__str__())
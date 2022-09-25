from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), ".env")))

from router.news_router import news_router
from router.tags_router import tags_router
from router.coingecko_router import cg_router


# create fastapi app
def create_app() -> FastAPI:
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(news_router, prefix="/api/v1")
    app.include_router(tags_router, prefix="/api/v1")
    app.include_router(cg_router, prefix="/api/v1")
    return app


# create app
app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", port=80, reload=True)

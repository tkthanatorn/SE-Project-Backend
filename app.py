from fastapi import FastAPI
from fastapi.middleware import cors
import uvicorn

from routes import news_router, tags_router

app = FastAPI()

origins = ['*']
methods = ['*']
headers = ['*']
app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)

app.include_router(news_router, prefix='/news')
app.include_router(tags_router, prefix='/tags')

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True)

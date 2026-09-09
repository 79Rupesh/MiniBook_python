from fastapi import FastAPI

from database import create_table

from routers.books import router

app = FastAPI()
create_table()

app.include_router(
    router,
    prefix="/api",
    tags=["Books"]
)

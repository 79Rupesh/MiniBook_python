from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import create_table
from routers.books import router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


create_table()


app.include_router(
    router,
    prefix="/api",
    tags=["Books"]
)
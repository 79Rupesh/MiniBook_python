from fastapi import APIRouter
from pydantic import BaseModel

from services.book_service import(

    getbooks,
    add_book,
    remove_book
)

router = APIRouter()

class BookCreate(BaseModel):
    title:str
    author:str


@router.get("/books")
def get_all():

    books = getbooks()

    return{
        "books":[
            dict(book)
            for book in books
        ]
    }


@router.post("/books")
def create(book:BookCreate):

    book_id = add_book(
        book.title,
        book.author
    )

    return{
        "message":"Book created",
        "id":book_id
    }


@router.delete("/books/{book_id}")
def delete(book_id : int):

    delete = remove_book(book_id)

    if delete == 0:
        return{
            "message":"Book not found"
        }

    return{
        "message":"Book deleted succefully"
    }
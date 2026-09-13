from repositories.book_repository import(

    get_all_books,
    create_book,
    delete_book
)

def getbooks():

    return get_all_books()


def add_book(title:str,author:str):

    if len(title)<3:
        return None

    if len(author)<2:
        return None

    return create_book(
        title,
        author
    )

def remove_book(book_id : int):
    return delete_book(book_id)
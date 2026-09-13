from database import get_connection


def get_all_books():
    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        "SELECT * FROM books"
    )

    books = cursor.fetchall()
    connection.close()
    return books




def create_book(title:str , author:str):


    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO books (title,author)
        VALUES(? , ?)
        """,
        (title,author)
    )

    connection.commit()
    book_id= cursor.lastrowid
    connection.close()
    return book_id



def delete_book(book_id : int):
    connection = get_connection()

    cursor =  connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()

    deleted =  cursor.rowcount

    connection.close()

    return deleted
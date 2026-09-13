const API_URL = "http://127.0.0.1:8000/api/books";


// -------------------------
// GET ALL BOOKS
// -------------------------

async function loadBooks() {

    try {

        const response = await fetch(API_URL);

        const data = await response.json();

        const container = document.getElementById("booksContainer");

        container.innerHTML = "";

        if (data.books.length === 0) {

            container.innerHTML = "<p>No books available.</p>";

            return;
        }

        data.books.forEach(book => {

            const bookDiv = document.createElement("div");

            bookDiv.classList.add("book");

            bookDiv.innerHTML = `
    <h3>📖 ${book.title}</h3>
    <p>Author: ${book.author}</p>

    <button onclick="deleteBook(${book.id})">
        Delete
    </button>
`;

            container.appendChild(bookDiv);

        });

    } catch (error) {

        console.error(error);

        document.getElementById("booksContainer").innerHTML =
            "<p>Backend server se connection nahi ho raha.</p>";
    }
}



// -------------------------
// ADD BOOK
// -------------------------

document
    .getElementById("bookForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const title =
            document.getElementById("title").value;

        const author =
            document.getElementById("author").value;


        try {

            const response = await fetch(API_URL, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    title: title,
                    author: author
                })

            });


            const data = await response.json();

            const message =
                document.getElementById("message");


            if (response.ok) {

                message.textContent =
                    "✅ Book created successfully!";

                document
                    .getElementById("bookForm")
                    .reset();

                loadBooks();

            } else {

                message.textContent =
                    "❌ Book create nahi hui.";

            }

        } catch (error) {

            console.error(error);

            document.getElementById("message").textContent =
                "❌ Backend server se connection nahi ho raha.";
        }

    });


// -------------------------
// LOAD BOOKS WHEN PAGE OPENS
// -------------------------

loadBooks();


async function deleteBook(bookId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this book?"
    );

    if (!confirmDelete) {
        return;
    }

    try {

        const response = await fetch(
            `${API_URL}/${bookId}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        console.log("DELETE response:", response.status, data);

        if (response.ok) {

            alert(data.message);

            loadBooks();

        } else {

            alert("Book delete nahi hui.");

        }

    } catch (error) {

        console.error("DELETE ERROR:", error);

        alert(
            "Backend server se connection nahi ho raha hai."
        );
    }
}
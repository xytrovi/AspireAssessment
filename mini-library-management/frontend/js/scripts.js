// This file contains JavaScript code for frontend interactivity, such as form submissions and dynamic content updates.

document.addEventListener('DOMContentLoaded', function() {
    const bookForm = document.getElementById('book-form');
    const searchForm = document.getElementById('search-form');
    const bookList = document.getElementById('book-list');

    if (bookForm) {
        bookForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(bookForm);
            fetch('/api/books', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Book added successfully!');
                    bookForm.reset();
                    loadBooks();
                } else {
                    alert('Error adding book: ' + data.message);
                }
            });
        });
    }

    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const query = document.getElementById('search-query').value;
            fetch(`/api/books/search?query=${query}`)
            .then(response => response.json())
            .then(data => {
                displayBooks(data.books);
            });
        });
    }

    function loadBooks() {
        fetch('/api/books')
        .then(response => response.json())
        .then(data => {
            displayBooks(data.books);
        });
    }

    function displayBooks(books) {
        bookList.innerHTML = '';
        books.forEach(book => {
            const li = document.createElement('li');
            li.textContent = `${book.title} by ${book.author} - ${book.status}`;
            bookList.appendChild(li);
        });
    }

    loadBooks();
});
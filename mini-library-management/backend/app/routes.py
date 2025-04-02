from flask import Blueprint, request, jsonify, send_from_directory
from .models import db, Book
import os

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return send_from_directory(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/templates')),
        'index.html'
    )

@bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_date=data.get('published_date'),  # Optional field
        is_checked_out=False  # Default to not checked out
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'}), 201

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'is_checked_out': book.is_checked_out
        } for book in books
    ])

@bp.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)
    book.title = data['title']
    book.author = data['author']
    book.published_date = data.get('published_date')  # Optional update
    db.session.commit()
    return jsonify({'message': 'Book updated successfully!'})

@bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'})

@bp.route('/books/checkin/<int:book_id>', methods=['POST'])
def checkin_book(book_id):
    book = Book.query.get_or_404(book_id)
    book.is_checked_out = False
    db.session.commit()
    return jsonify({'message': 'Book checked in successfully!'})

@bp.route('/books/checkout/<int:book_id>', methods=['POST'])
def checkout_book(book_id):
    book = Book.query.get_or_404(book_id)
    book.is_checked_out = True
    db.session.commit()
    return jsonify({'message': 'Book checked out successfully!'})

@bp.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    books = Book.query.filter(
        (Book.title.contains(query)) | (Book.author.contains(query))
    ).all()
    return jsonify([
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'is_checked_out': book.is_checked_out
        } for book in books
    ])
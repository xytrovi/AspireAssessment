def validate_book_data(data):
    if not data.get('title') or not isinstance(data['title'], str):
        return False, "Title is required and must be a string."
    if not data.get('author') or not isinstance(data['author'], str):
        return False, "Author is required and must be a string."
    if 'status' in data and data['status'] not in ['checked_in', 'checked_out']:
        return False, "Status must be either 'checked_in' or 'checked_out'."
    return True, ""

def format_book_response(book):
    return {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'status': book.status
    }
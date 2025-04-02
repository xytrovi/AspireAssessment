import unittest
from app import create_app, db
from app.models import Book

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_add_book(self):
        response = self.client.post('/add_book', data={
            'title': 'Test Book',
            'author': 'Test Author',
            'status': 'available'
        })
        self.assertEqual(response.status_code, 200)
        book = Book.query.filter_by(title='Test Book').first()
        self.assertIsNotNone(book)

    def test_check_out_book(self):
        book = Book(title='Test Book 2', author='Test Author 2', status='available')
        with self.app.app_context():
            db.session.add(book)
            db.session.commit()
        
        response = self.client.post('/check_out', data={'book_id': book.id})
        self.assertEqual(response.status_code, 200)
        book = Book.query.get(book.id)
        self.assertEqual(book.status, 'checked out')

    def test_search_book(self):
        book = Book(title='Searchable Book', author='Search Author', status='available')
        with self.app.app_context():
            db.session.add(book)
            db.session.commit()

        response = self.client.get('/search', query_string={'title': 'Searchable Book'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Searchable Book', response.data)

if __name__ == '__main__':
    unittest.main()
# Mini Library Management System

This is a full-stack application for managing a mini library. It allows users to manage books, check them in and out, and search for available titles. The application is built using Python Flask for the backend, MySQL for the database, and a simple HTML/CSS/JavaScript frontend with Bootstrap for the UI.

## Project Structure

```
touficAssessment
└── mini-library-management
    ├── backend
    │   ├── app
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── routes.py
    │   │   └── utils.py
    │   ├── migrations
    │   │   └── (empty for now)
    │   ├── tests
    │   │   └── test_app.py
    │   ├── .env
    │   ├── .env.example
    │   ├── requirements.txt
    │   └── setup.py
    ├── frontend
    │   ├── css
    │   │   └── styles.css
    │   ├── js
    │   │   └── scripts.js
    │   ├── templates
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   ├── books.html
    │   │   └── search.html
    │   └── static
    │       └── (empty for now)
    ├── .gitignore
    ├── README.md
```

## Features

- **Book Management**: Add, edit, and delete books in the library.
- **Check-In/Check-Out**: Manage the status of books (checked in or checked out).
- **Search Functionality**: Search for books by title, author, or other criteria.

## Requirements

- Python 3.x
- MySQL
- Flask
- SQLAlchemy
- Bootstrap (for frontend)

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd mini-library-management
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the requirements**:
   ```
   pip install -r backend/requirements.txt
   ```

4. **Set up the environment variables**:
   - Copy `.env.example` to `.env` and fill in your database connection details.
   

5. **Initialize the database**:
   ```
   - Create the database named library_db on MySQL command such as "CREATE DATABASE library_db;"
   - python backend/initialize.py
   ```

6. **Run the application**:
   ```
   python backend/run.py
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Testing

To run the tests, navigate to the `backend/tests` directory and execute:
```
pytest test_app.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
# filepath: c:\Users\admin\Desktop\touficAssessment\mini-library-management\backend\initialize.py
import os
from dotenv import load_dotenv
from app import create_app, db

# Load environment variables from .env
load_dotenv()

# Retrieve the DATABASE_URL from the environment
database_url = os.getenv('DATABASE_URL')

if not database_url:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

# Create the Flask app
app = create_app()

# Initialize the database
with app.app_context():
    print("Initializing the database...")
    db.create_all()
    print("Database initialized successfully!")
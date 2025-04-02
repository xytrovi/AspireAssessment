# filepath: c:\Users\admin\Desktop\touficAssessment\mini-library-management\backend\app\__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # Set the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Import models to register them with SQLAlchemy
    with app.app_context():
        from app import models

    # Register the Blueprint
    from app.routes import bp
    app.register_blueprint(bp, url_prefix='/api')

    return app
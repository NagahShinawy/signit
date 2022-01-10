"""
app basic config
"""

import os

PROFILES_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(PROFILES_DIR))
root = lambda *x: os.path.join(BASE_DIR, *x)
DEBUG = True
SERVER_PORT = 5000
# SERVER_NAME = 'http://127.0.0.1:5000'
# SERVER_NAME = "localhost.dev"
SQLALCHEMY_ECHO = False
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, "db_repository")
SECRET_KEY = "changeme"
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger/swagger.json"

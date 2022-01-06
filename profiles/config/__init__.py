"""
app basic config
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SERVER_PORT = 5000
# SERVER_NAME = 'http://127.0.0.1:5000'
# SERVER_NAME = "localhost.dev"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_ADDR = os.environ.get("DB_ADDR")
DB_NAME = os.environ.get("DB_NAME")
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDR}/{DB_NAME}"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
SECRET_KEY = "changeme"  # for generating jwt token
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger/swagger.json"

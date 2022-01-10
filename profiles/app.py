"""
init app configuration
"""

from flask import Flask

from profiles.api.v1 import views as v1_views
from profiles.config import SQLALCHEMY_DATABASE_URI
from profiles.extensions import db, migrate


def create_app():
    """
    :return: flask app obj
    """
    app = Flask(__name__)
    configure_app(app)
    configure_extensions(app)
    register_blueprints(app)  # domain/api/

    return app


def configure_app(app):
    """set configuration for application"""
    # default configuration
    app.config.from_object("profiles.config.develop")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.url_map.strict_slashes = False


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(v1_views.blueprint)

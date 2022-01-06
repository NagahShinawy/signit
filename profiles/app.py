"""
init app configuration
"""

from flask import Flask

# from api.extensions import db, migrate
# from api.views.views import api_bp
from profiles.api.v1 import views as v1_views


def create_app(config_filename):
    """

    :param config_filename: file contains app config
    :return: flask app obj
    """
    app = Flask(__name__)
    app.config.from_object(config_filename)
    configure_extensions(app)
    register_blueprints(app)  # domain/api/

    return app


def configure_extensions(app):
    """configure flask extensions"""
    # db.init_app(app)
    # migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(v1_views.blueprint)

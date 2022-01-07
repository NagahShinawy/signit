"""
connect endpoints with resources
"""

from flask import Blueprint
from flask_restful import Api

from profiles.api.v1.resources import (
    UserResource,
    UserCreateResource,
)

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(UserCreateResource, "/user/")
api.add_resource(UserResource, "/users/<int:pk>/")

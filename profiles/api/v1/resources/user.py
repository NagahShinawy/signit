"""
user resources
"""
from http import HTTPStatus

from flask import request
from flask_restful import Resource
from profiles.models import User
from profiles.api.v1.schemas import UserSchema
from profiles.commons import constants, utils


class UserMixin:
    model = User
    schema = UserSchema


class UserResource(Resource, UserMixin):
    """
    user apis [ get, patch, delete ]
    """

    def get(self, _id):
        user = self.model.query.get_or_404(_id)
        return self.schema().dump(user)

    def patch(self):
        pass

    def delete(self):
        pass


class UserCreateResource(Resource, UserMixin):
    """
    user create api [ post ]
    """

    model = User
    schema = UserSchema

    def post(self):
        payload = request.get_json()
        data = utils.get_json_from_request(request)
        return data

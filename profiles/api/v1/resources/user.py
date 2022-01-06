"""
user resources
"""

from flask_restful import Resource
from profiles.models import User
from profiles.api.v1.schemas import UserSchema


class UserResource(Resource):
    """
    user apis [ get, post ]
    """
    model = User
    schema = UserSchema

    def get(self, _id):
        user = self.model.query.get_or_404(_id)
        return self.schema().dump(user)


class UserUpdateResource(Resource):
    """
    user update api [ patch]
    """


class UserDeleteResource(Resource):
    """
    user delete api
    """

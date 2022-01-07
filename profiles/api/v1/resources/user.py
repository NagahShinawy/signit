"""
user resources
"""
from http import HTTPStatus
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy import engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker
from profiles.api.v1.schemas import UserSchema
from profiles.commons import utils
from profiles.commons.crud import CRUDMixin
from profiles.models import User

session = scoped_session(sessionmaker(bind=engine))


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


class UserCreateResource(Resource, UserMixin, CRUDMixin):
    """
    user create api [ post ]
    """

    def post(self):
        json_data = utils.get_json_from_request(request)
        try:

            user = self.schema().load(json_data)
        except ValidationError as errors:
            return {"errors": errors.messages}, HTTPStatus.BAD_REQUEST

        self.add(user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

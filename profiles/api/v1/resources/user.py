"""
user resources
"""
from http import HTTPStatus

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from profiles.api.v1.schemas import UserSchema
from profiles.commons import utils
from profiles.commons.crud import CRUDMixin
from profiles.config.logs import logger
from profiles.models import User


class UserMixin:
    """
    share between user resources
    """

    model = User
    schema = UserSchema


class UserResource(Resource, UserMixin, CRUDMixin):
    """
    user apis [ GET, PATCH, DELETE ]
    """

    def get(self, pk):
        """
        get single user
        :param pk: pk for single user
        :return: user obj or 404
        """
        user = self.model.query.get_or_404(pk)
        logger.info(f"user '%s' found", user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

    def patch(self, pk):
        """
        update user data
        :param pk: pk for single user
        :return: update user obj
        """
        user = User.query.get_or_404(pk)
        json_data = utils.get_json_from_request(request)
        try:
            user = self.schema().load(json_data, instance=user, partial=True)
        except ValidationError as errors:
            logger.error(f"bad params [%s]", errors.messages)
            return {"errors": errors.messages}, HTTPStatus.BAD_REQUEST
        self.add(user)
        logger.info(f"user '%s' saved successfully", user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

    def delete(self, pk):
        """

        :param pk: pk for single user
        :return: delete user or 404
        """
        user = User.query.get_or_404(pk)
        logger.info(f"user '%s' found", user)
        super().delete(user)
        logger.info(f"user '%s' deleted successfully", user)
        return "", HTTPStatus.NO_CONTENT


class UserCreateResource(Resource, UserMixin, CRUDMixin):
    """
    user create api [ POST ]
    """

    def post(self):
        """
        create new user
        :return:
        """
        json_data = utils.get_json_from_request(request)
        logger.info(f"getting data %s", json_data)
        try:

            user = self.schema().load(json_data)
        except ValidationError as errors:
            logger.error(f"bad params [%s]", errors.messages)
            return {"errors": errors.messages}, HTTPStatus.BAD_REQUEST

        self.add(user)
        logger.info(f"user '%s' saved successfully", user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

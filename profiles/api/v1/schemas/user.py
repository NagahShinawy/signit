"""
handle user scheme
"""
from marshmallow import Schema, ValidationError, fields, validate, validates
from profiles.commons.validation import validate_email
from profiles.extensions import ma
from profiles.models import User
# from profiles.extensions import db


class UserSchema(ma.SQLAlchemyAutoSchema):
    EXCLUDE_FOR_DUMP = ("password", )
    EXCLUDE_FOR_LOAD = ("id", "created")

    email = fields.Email(validate=[validate_email])
    password = fields.String(required=True)

    class Meta:
        model = User
        load_instance = True


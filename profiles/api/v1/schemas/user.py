"""
handle user scheme
"""
from marshmallow import fields
from profiles.commons.validation import EmailAlreadyExistValidator, FullNameValidator, PasswordValidator
from profiles.extensions import ma
from profiles.models import User
from profiles.extensions import db
from profiles.commons import constants


class UserSchema(ma.SQLAlchemyAutoSchema):
    EXCLUDE_FOR_DUMP = ("password",)

    fullname = fields.String(required=True, validate=FullNameValidator(constants.FULLNAME_REGX))
    email = fields.Email(validate=EmailAlreadyExistValidator())
    password = fields.String(
        required=True, validate=PasswordValidator(constants.PWD_REGEX),
    )

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

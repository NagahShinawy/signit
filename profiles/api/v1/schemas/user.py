"""
handle user scheme
"""
from marshmallow import fields, validate
from profiles.commons.validation import validate_email
from profiles.extensions import ma
from profiles.models import User
from profiles.extensions import db


class UserSchema(ma.SQLAlchemyAutoSchema):
    EXCLUDE_FOR_DUMP = ("password",)
    EXCLUDE_FOR_LOAD = ("id", "created")

    fullname = fields.String(required=True)
    email = fields.Email(validate=[validate_email])
    password = fields.String(
        required=True,
        validate=validate.Regexp(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,50}$"
        ),
    )

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

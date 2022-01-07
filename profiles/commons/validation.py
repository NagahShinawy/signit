"""
data validation
"""
from sqlalchemy import func
from profiles.models import User
from marshmallow import ValidationError
from profiles.commons.errors import EmailAlreadyExistError


def validate_email(value):
    user = User.query.filter_by(email=func.lower(value)).first()
    if user:
        raise ValidationError(EmailAlreadyExistError.message)
    return value

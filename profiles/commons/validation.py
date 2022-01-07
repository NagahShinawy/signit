"""
data validation
"""
from sqlalchemy import func
from profiles.models import User
from marshmallow import ValidationError, validate


class EmailAlreadyExistValidator(validate.Email):
    message = "Email already exist"

    def __call__(self, value):
        user = User.query.filter_by(email=func.lower(value)).first()
        if user:
            raise ValidationError(self.message)
        return value


class PasswordValidator(validate.Regexp):
    default_message = "password must contains lower letter, upper letters, special letters and numbers"


class FullNameValidator(validate.Regexp):
    default_message = "fullname must contains at least 4 letters and 30 max letters"

"""
data validation
"""

from marshmallow import ValidationError, validate
from sqlalchemy import func

from profiles.models import User


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
    default_message = "invalid fullname.Only letters with spaces"


class FullNameLengthValidator(validate.Validator):
    MIN = 5
    MAX = 50
    default_message = f"fullname length in between {MIN} and {MAX}"

    def __call__(self, value):
        if len(value) in range(self.MIN, self.MAX):
            return value
        raise ValidationError(self.default_message)

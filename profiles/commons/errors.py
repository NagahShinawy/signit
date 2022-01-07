"""
custom errors
"""


class BaseError(Exception):
    message = "Unknown error"


class EmailAlreadyExistError(BaseError):
    message = "Email already exist"

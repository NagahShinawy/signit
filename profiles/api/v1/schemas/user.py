"""
handle user scheme
"""
from marshmallow import validate
from profiles.extensions import ma


class UserSchema(ma.Schema):
    email = ma.String(required=True, validate=[validate.Email()])
    username = ma.String(required=True)

    class Meta:
        fields = ("_id", "username", "first_name", "last_name", "email")

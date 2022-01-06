"""
user model
"""

from profiles.extensions import db, pwd_context
from profiles.commons.crud import CRUDMixin


class User(db.Model, CRUDMixin):
    """Basic user model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )  # optional requirement but it is import to data team to work on data with timestamp

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return f"<User {self.username}>"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}".title()

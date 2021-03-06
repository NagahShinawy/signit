"""
user model
"""

from profiles.commons.crud import CRUDMixin
from profiles.extensions import db, pwd_context


class User(db.Model, CRUDMixin):
    """Basic user model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )  # optional requirement but it is import to data team to work on data with timestamp
    #

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return f"<User {self.id}-{self.fullname}>"

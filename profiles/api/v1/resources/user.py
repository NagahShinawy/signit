"""
user resources
"""

from flask_restful import Resource


class UserResource(Resource):
    """
    user apis
    """

    def get(self):
        return {"status": "ok"}

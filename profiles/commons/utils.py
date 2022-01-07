"""
utils funcs
"""
import json


def get_json_from_request(request, data=True) -> dict:
    return request.get_json() or dict(data=dict() if data else dict())


def pretty_error(errors: str) -> dict:
    return json.loads(str(errors))

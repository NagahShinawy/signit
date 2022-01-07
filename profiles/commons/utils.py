"""
utils funcs
"""


def get_json_from_request(request, data=True) -> dict:
    return request.get_json() or dict(data=dict() if data else dict())

from typing import Callable
from bson import ObjectId, json_util
from functools import wraps


def bson_to_json_compatible(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return convert_bson_to_json_compatible(result)

    return wrapper


def convert_bson_to_json_compatible(data):
    """Recursively convert BSON types to JSON-compatible types."""
    if isinstance(data, list):
        return [convert_bson_to_json_compatible(item) for item in data]
    elif isinstance(data, dict):
        return {
            key: convert_bson_to_json_compatible(value) for key, value in data.items()
        }
    elif isinstance(data, ObjectId):
        return str(data)
    elif isinstance(data, (json_util.datetime.datetime, json_util.datetime.date)):
        return data.isoformat()
    else:
        return data

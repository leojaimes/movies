from typing import List, Dict
from bson import ObjectId, json_util
from app.dependences.bson_to_json.generator import convert_bson_to_json_compatible


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


def user_entity(user: Dict) -> Dict:
    return convert_bson_to_json_compatible(user)


def users_entity(users: List[Dict]) -> List[Dict]:
    return [user_entity(user) for user in users]

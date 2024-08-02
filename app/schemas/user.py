from typing import List, Dict
from bson import ObjectId, json_util


def user_entity(user: Dict) -> Dict:
    return user


def users_entity(users: List[Dict]) -> List[Dict]:
    return [user_entity(user) for user in users]

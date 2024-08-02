from fastapi.responses import JSONResponse
import orjson
from bson import ObjectId
from datetime import datetime


# Función para convertir BSON a JSON compatible usando orjson
def convert_bson_to_json(data):
    def orjson_default(obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, bytes):
            return obj.decode("utf-8")
        raise TypeError(f"Type not serializable: {type(obj)}")

    json_data = orjson.dumps(data, default=orjson_default)
    return orjson.loads(json_data)


# Función auxiliar para devolver una respuesta JSON
def create_json_response(data):
    json_compatible_data = convert_bson_to_json(data)
    return JSONResponse(content=json_compatible_data)

# Imports
from pymongo.database import Database
from bson import ObjectId


def process_response(db_response: dict | list) -> dict | list:
    """Find the _id key and transform to string value

    Args:
        db_response (dict | list): the cursor or document value

    Raises:
        ValueError: if the db_response is not a dict o list instance, raise a ValueError

    Returns:
        (dict | list): return the same db_response instance but with _id keys transformed to string type
    """
    if isinstance(db_response, list):
        for document in db_response:
            document["_id"] = str(document["_id"])
        return db_response
    elif isinstance(db_response, dict):
        db_response["_id"] = str(db_response["_id"])
        return db_response
    else:
        raise ValueError(
            f"db_response will be dict or a list and is a {type(db_response)} instance"
        )


def check_if_item_exists(
    db_instance: Database, collection_name: str, item_id: str
) -> bool:
    """Check if the item exists en the database and return true or false

    Args:
        db_instance (Database)
        collection_name (str)
        item_id (str)

    Returns:
        bool: True if item exist, else return false
    """
    ITEM = db_instance[collection_name].find_one({"_id": ObjectId(item_id)})

    return True if ITEM else False

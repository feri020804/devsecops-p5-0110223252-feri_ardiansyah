from uuid import uuid4


def create_asset(name, location, condition):
    return {
        "id": str(uuid4()),
        "name": name,
        "location": location,
        "condition": condition,
    }
from app.infra.connections import mongodb_connection


def create_novel_collection():
    client = mongodb_connection()
    db = client["daily-novels"]
    collection_to_create = {
        "$jsonSchema": {
            "bsonType": "object",
            "additionalProperties": True,
            "required": ["name", "year", "actor", "inserted_at"],
            "properties": {
                "name": {
                    "bsonType": "string"
                },
                "year": {
                    "bsonType": "int"
                },
                "actor": {
                    "bsonType": "string"
                },
                "inserted_at": {
                    "bsonType": "date"
                },
                "last_updated": {
                    "bsonType": "date"
                },
                "chapters": {
                    "bsonType": ["array"],
                    "items": {
                        "bsonType": "object",
                        "properties": {
                            "weekly_count": {
                                "bsonType": "string"
                            },
                            "available_chapters": {
                                "bsonType": ["array"],
                                "items": {
                                    "bsonType": "object",
                                    "properties": {
                                        "chapter_number": {
                                            "bsonType": "int"
                                        },
                                        "content_url": {
                                            "bsonType": "string"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    collections_created = db.create_collection("novels", validator=collection_to_create)

    return collections_created

from app.infra.connections import mongodb_connection


def find_novel_by_name(name):
    collection = mongodb_connection()["daily-novels"]["novels"]
    return collection.find_one({'name': name})

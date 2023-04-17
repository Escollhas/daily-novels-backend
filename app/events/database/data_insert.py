from app.events.models import ModelCollectionNovels
from app.infra.connections import mongodb_connection


def insert_data_novel(data_to_insert: ModelCollectionNovels):
    collection = mongodb_connection()["daily-novels"]["novels"]

    return collection.insert_one(data_to_insert.__dict__)


import akeyless
from akeyless.models.auth_output import AuthOutput
from pika import BlockingConnection, URLParameters
from pymongo import MongoClient

from app.infra.secrets import Secrets

secrets = Secrets()


def mongodb_connection() -> MongoClient:
    client = MongoClient(secrets.mongodb_connection)

    return client


def rabbitmq_connection() -> BlockingConnection:
    return BlockingConnection(URLParameters(secrets.rabbitmq_url_connection))


def secrets_api_connection() -> AuthOutput:
    configuration = akeyless.Configuration(
        host="https://api.akeyless.io"
    )
    api_client = akeyless.ApiClient(configuration)
    api = akeyless.V2Api(api_client)

    credentials = akeyless.Auth(
        access_id=secrets.secrets_access_id,
        access_key=secrets.secrets_access_key
    )

    response = api.auth(credentials)

    return response

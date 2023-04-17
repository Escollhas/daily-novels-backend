import os

from dotenv import load_dotenv

from app.commons.singleton import Singleton

load_dotenv()


class Secrets(metaclass=Singleton):
    def __init__(self):
        self.secrets_access_id = os.getenv("SECRETS_ACCESS_ID")
        self.secrets_access_key = os.getenv("SECRETS_ACCESS_KEY")
        self.rabbitmq_url_connection = os.getenv("RABBITMQ_URL_CONNECTION")
        self.mongodb_connection = os.getenv("MONGODB_CONNECTION")


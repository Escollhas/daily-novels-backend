import json

from app.infra.connections import rabbitmq_connection
from app.utils.mocks import random_number_int, random_name


def publish_message(exchange_name: str, routing_key: str, data: dict) -> None:
    # TODO Checar como lidar o body ser enviado para multiplos tipos e se vale a pena ser um método único
    # TODO Criar mensagem de envio com sucesso ou erro

    exchange_name = exchange_name

    channel = rabbitmq_connection().channel()

    serialized_data = json.dumps(data)

    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=serialized_data)
    print("Foi?", exchange_name, routing_key, serialized_data)

    channel.close()


if __name__ == "__main__":
    mocked_data = {"user": random_name(), "chapter_number": random_number_int(), "novel": "Against The Gods"}

    mocked_exchange_name = "staging"

    publish_message(exchange_name=mocked_exchange_name, routing_key="chapter_read", data=mocked_data)

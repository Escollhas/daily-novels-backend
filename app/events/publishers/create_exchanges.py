from typing import Union
from pika.exchange_type import ExchangeType as ExType

from app.infra.connections import rabbitmq_connection


def new_exchange(exchange_name: str,
                 exchange_type: Union[ExType.direct, ExType.fanout, ExType.topic, ExType.headers]) -> None:

    channel = rabbitmq_connection().channel()

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type=exchange_type
    )


if __name__ == "__main__":
    new_exchange(exchange_name="staging", exchange_type=ExType.direct)

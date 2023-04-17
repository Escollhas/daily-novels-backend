import pika
from enum import Enum

from app.enums import QueueEnum
from app.infra.connections import rabbitmq_connection


def create_all_queues():
    channel = rabbitmq_connection().channel()
    for queue in QueueEnum:
        queue_name = queue.value
        channel.queue_declare(queue=queue_name, durable=True)
        print(f"Queue {queue_name} declared")

    channel.close()

from app.infra.connections import rabbitmq_connection


def create_binding_chapter_read():
    channel = rabbitmq_connection().channel()

    channel.queue_bind(exchange="chapter_read", queue="update_novel_counts", routing_key="chapter_read")

    channel.close()


def create_binding_novels(queue, routing_key):
    channel = rabbitmq_connection().channel()

    channel.queue_bind(exchange="novels", queue=queue, routing_key=routing_key)

    channel.close()


if __name__ == "__main__":
    create_binding_chapter_read()
    create_binding_novels(queue="novel.create", routing_key="novel.create")

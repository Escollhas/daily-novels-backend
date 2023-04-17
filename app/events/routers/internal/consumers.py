import asyncio
import json

from app.events.consumers.create_queues import create_all_queues

from fastapi import APIRouter

from app.events.publishers.create_bindings import create_binding_chapter_read, create_binding_novels
from app.infra.connections import rabbitmq_connection

router = APIRouter(prefix="/internal")


@router.get("/create_all_queues")
async def create_queues():
    create_all_queues()


@router.get("/create_all_bindings")
async def bindings():
    create_binding_chapter_read()
    create_binding_novels(queue="novel.create", routing_key="novel.create")


@router.get("/read_queue")
async def read_create_novel_queue():
    ## TODO create file to consumers and save to MongoDBg
    ## TODO make consumers and save to DB in GO
    channel = rabbitmq_connection().channel()

    messages = []
    while True:
        method_frame, properties, body = channel.basic_get("novel.create", auto_ack=False)

        if method_frame is None:
            break

        messages.append(json.loads(body))

        channel.basic_ack(method_frame.delivery_tag)

    channel.close()

    return {"messages": messages}

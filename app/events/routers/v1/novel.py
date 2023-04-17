from fastapi import APIRouter

from app.events.models import ModelCollectionNovels
from app.events.publishers.publish_messages import publish_message

router = APIRouter()


@router.post("/novel")
async def read_chapter(novel_to_create_payload: ModelCollectionNovels):
    # TODO Improve
    # TODO should be unique

    publish_message(exchange_name="novels", routing_key="novel.create", data=novel_to_create_payload.json())

    response = f"Usuário solicitou a criação da novel {novel_to_create_payload.json()}"

    return response

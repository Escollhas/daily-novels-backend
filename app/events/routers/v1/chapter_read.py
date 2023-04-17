from fastapi import APIRouter
from pydantic import BaseModel

from app.events.publishers.publish_messages import publish_message

router = APIRouter(prefix="/novel")


class ChapterReadInfo(BaseModel):
    chapter_number: int
    novel_name: str
    username: str


@router.post("/chapter_read")
async def read_chapter(chapter_info: ChapterReadInfo):
    # TODO Improve

    chapter_number = chapter_info.chapter_number
    novel_name = chapter_info.novel_name
    username = chapter_info.username

    publish_message(exchange_name="chapter_read", routing_key="chapter_read", data=chapter_info.__dict__)

    response = f"Usuário {username} leu o capítulo {chapter_number} da novel {novel_name}"

    return response

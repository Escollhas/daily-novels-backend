from fastapi import APIRouter
from pika.exchange_type import ExchangeType

from app.events.publishers.create_exchanges import new_exchange

router = APIRouter(prefix="/internal")


@router.get("/create_all_publishers")
async def read_chapter():
    new_exchange(exchange_name="novels", exchange_type=ExchangeType.direct)


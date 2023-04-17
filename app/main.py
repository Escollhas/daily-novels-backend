from fastapi import FastAPI

from app.events.routers.v1 import chapter_read, novel
from app.events.routers.internal import consumers, publishers

app = FastAPI()

app.include_router(chapter_read.router)
app.include_router(novel.router)
app.include_router(consumers.router)
app.include_router(publishers.router)


@app.get("/")
async def root():
    return {"message": "In development"}

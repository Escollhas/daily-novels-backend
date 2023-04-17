from enum import Enum


class ExchangeEnum(Enum):
    """This Enum should contain all exchange in prod"""
    CHAPTER_READ = "chapter_read"
    NOVELS = "novels"


class QueueEnum(Enum):
    """This Enum should contain all queues in prod"""
    CREATE_NOVEL = "novel.create"
    UPDATE_NOVEL = "novel.update"


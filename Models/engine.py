from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.config import CONFIG


DATABASE_URI: str = CONFIG.DATABASE.URI
ENGINE = create_engine(DATABASE_URI)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            func(**kwargs, session=session)
    return wrapper


ASYNC_ENGINE = create_async_engine(CONFIG.DATABASE.ASYNC_URI)


def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=ASYNC_ENGINE) as session:
            return await func(**kwargs, session=session)
    return wrapper

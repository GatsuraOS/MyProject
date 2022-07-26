from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import CONFIG


DATABASE_URI: str = CONFIG.DATABASE.URI
ENGINE = create_engine(DATABASE_URI)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            func(**kwargs, session=session)
    return wrapper

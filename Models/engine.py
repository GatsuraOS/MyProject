from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI: str = "postgresql://belhard:belhard@localhost:5432/belhard"
ENGINE = create_engine(DATABASE_URI)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            func(**kwargs, session=session)
    return wrapper

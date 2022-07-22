from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URI: str = "postgresql://belhard:belhard@localhost:5432/belhard"
ENGINE = create_engine(DATABASE_URI)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):


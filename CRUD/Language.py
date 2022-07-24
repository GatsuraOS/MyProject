from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Schemas import LanguageSchema, LanguageInDBSchema
from Models import Language, create_session


class CRUDLanguage:

    @staticmethod
    @create_session
    def add(language: LanguageSchema, session: Session = None) -> LanguageInDBSchema | None:
        language = Language(
            **language.__dict__
        )
        session.add(language)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(language)
            return LanguageInDBSchema(**language.__dict__)

    @staticmethod
    @create_session
    def get(language_id: int, session: Session = None) -> Language | None:
        language = session.execute(
            select(Language).where(Language.id == language_id)
        )
        language = language.first()
        if language:
            return language[0]

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[Language]:
        languages = session.execute(
            select(Language)
        )
        return [language[0] for language in languages.all()]

    @staticmethod
    @create_session
    def delete(language_id: int, session: Session = None) -> None:
        session.execute(
            delete(Language).where(Language.id == language_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(language: LanguageInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Language).where(Language.id == language.id).values(
                **language.__dict__
            )
        )
        session.commit()

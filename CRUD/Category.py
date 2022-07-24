from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models import Category, create_session
from Schemas import CategorySchema, CategoryInDBSchema


class CRUDCategory:

    @staticmethod
    @create_session
    def add(category: CategorySchema, session: Session = None) -> CategoryInDBSchema | None:
        category = Category(
            **category.dict()
        )
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Category | None:
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_session
    def get(session: Session = None) -> list[Category]:
        categories = session.execute(
            select(Category)
        )
        return [category[0] for category in categories.all()]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category).where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(category: CategoryInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Category).where(Category.id == category.id).values(
                **category.__dict__
            )
        )
        session.commit()

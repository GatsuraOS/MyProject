from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Schemas import StatusSchema, StatusInDBSchema
from Models import Status, create_session


class CRUDStatus:

    @staticmethod
    @create_session
    def add(status: StatusSchema, session: Session = None) -> StatusInDBSchema | None:
        status = Status(
            **status.dict()
        )
        session.add(status)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(status)
            return StatusInDBSchema(**status.__dict__)

    @staticmethod
    @create_session
    def get(status_id: int, session: Session = None) -> StatusInDBSchema | None:
        status = session.execute(
            select(Status).where(Status.id == status_id)
        )
        status = status.first()
        if status:
            return StatusInDBSchema(**status[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session) -> list[StatusInDBSchema]:
        statuses = session.execute(
            select(Status)
        )
        return [StatusInDBSchema(**status[0].__dict__) for status in statuses.all()]

    @staticmethod
    @create_session
    def delete(status_id: int, session: Session = None) -> None:
        session.execute(
            delete(Status).where(Status.id == status_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(status: StatusInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Status).where(Status.id == status.id). values(
                **status.dict()
            )
        )
        session.commit()

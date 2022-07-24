from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Schemas import BotUserSchema, BotUserInDBSchema
from Models import BotUser, create_session


class CRUDBotUser:

    @staticmethod
    @create_session
    def add(bot_user: BotUserSchema, session: Session = None) -> BotUserInDBSchema | None:
        bot_user = BotUser(
            **bot_user.__dict__
        )
        session.add(bot_user)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(bot_user)
            return BotUserInDBSchema(**bot_user.__dict__)

    @staticmethod
    @create_session
    def get(bot_user_id: str, session: Session = None) -> BotUser | None:
        bot_user = session.execute(
            select(BotUser).where(BotUser.id == bot_user_id)
        )
        bot_user = bot_user.first()
        if bot_user:
            return bot_user[0]

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[BotUser]:
        bot_users = session.execute(
            select(BotUser)
        )
        return [bot_user[0] for bot_user in bot_users.all()]

    @staticmethod
    @create_session
    def delete(bot_user: str, session: Session = None) -> None:
        session.execute(
            delete(BotUser).where(BotUser.id == bot_user)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(bot_user: BotUserInDBSchema, session: Session = None) -> None:
        session.execute(
            update(BotUser).where(BotUser.id == bot_user.id).values(
                **bot_user.__dict__
            )
        )
        session.commit()

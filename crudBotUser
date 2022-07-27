import sqlite3
from Schemas import BotUserSchema
from Schemas import BotUserInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class BotUserCRUD:

    @staticmethod
    def add(bot_user: BotUserSchema) -> None:
        cur.execute("""
        INSERT INTO bot_users(is_blocked, balance, language_id);
        """, (bot_user.is_blocked, bot_user.balance, bot_user.language_id))
        conn.commit()

    @staticmethod
    def get(bot_user_id: str) -> list[BotUserInDBSchema]:
        cur.execute("""
        SELECT * FROM bot_users WHERE id = ?;
        """, (bot_user_id, ))
        bot_users = []
        for bot_user in cur.fetchall():
            bot_users.append(
                BotUserInDBSchema(
                    id=bot_user[0],
                    is_blocked=bot_user[1],
                    balance=bot_user[2],
                    language_id=bot_user[3]
                )
            )
        return bot_users

    @staticmethod
    def get_all() -> list[BotUserInDBSchema]:
        cur.execute("""
        SELECT * FROM bot_users;
        """)
        bot_users = []
        for bot_user in cur.fetchall():
            bot_users.append(
                BotUserInDBSchema(
                    id=bot_user[0],
                    is_blocked=bot_user[1],
                    balance=bot_user[2],
                    language_id=bot_user[3]
                )
            )
        return bot_users

    @staticmethod
    def update(bot_user_id: str, bot_user: BotUserSchema) -> None:
        cur.execute("""
        UPDATE bot_users SET (is_blocked, balance, language_id) WHERE id = ?;
        """, (bot_user.is_blocked, bot_user.balance, bot_user.language_id, bot_user_id))
        conn.commit()

    @staticmethod
    def delete(bot_user_id: str) -> None:
        cur.execute("""
        DELETE FROM bot_users WHERE id = ?;
        """, (bot_user_id, ))
        conn.commit()

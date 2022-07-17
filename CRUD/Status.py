import sqlite3
from Schemas import StatusSchema
from Schemas import StatusInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class StatusCRUD:

    @staticmethod
    def add(status: StatusSchema) -> None:
        cur.execute("""
        INSERT INTO statuses(name);
        """, (status.name, ))
        conn.commit()

    @staticmethod
    def get(status_id: int) -> list[StatusInDBSchema]:
        cur.execute("""
        SELECT * FROM statuses WHERE id = ?;
        """, (status_id, ))
        statuses = []
        for status in cur.fetchall():
            statuses.append(
                StatusInDBSchema(
                    id=status[0],
                    name=status[1]
                )
            )
        return statuses

    @staticmethod
    def get_all() -> list[StatusInDBSchema]:
        cur.execute("""
        SELECT * FROM statuses;
        """)
        statuses = []
        for status in cur.fetchall():
            statuses.append(
                StatusInDBSchema(
                    id=status[0],
                    name=status[1]
                )
            )
        return statuses

    @staticmethod
    def update(status_id: int, status: StatusSchema) -> None:
        cur.execute("""
        UPDATE statuses SET (name) WHERE id = ?;
        """, (status.name, status_id))
        conn.commit()

    @staticmethod
    def delete(status_id: int) -> None:
        cur.execute("""
        DELETE FROM statuses where id = ?;
        """, (status_id, ))
        conn.commit()
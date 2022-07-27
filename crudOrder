import sqlite3
from Schemas import OrderSchema
from Schemas import OrderInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class OrderCRUD:

    @staticmethod
    def add(order: OrderSchema) -> None:
        cur.execute("""
        INSERT INTO orders(bot_user_id, date_create, status_id, invoice_id);
        """, (order.bot_user_id, order.date_create, order.status_id, order.invoice_id))
        conn.commit()

    @staticmethod
    def get(order_id: int) -> list[OrderInDBSchema]:
        cur.execute("""
        SELECT * FROM orders WHERE id = ?;
        """, (order_id, ))
        orders = []
        for order in cur.fetchall():
            orders.append(
                OrderInDBSchema(
                    id=order[0],
                    bot_user_id=order[1],
                    date_create=order[2],
                    status_id=order[3],
                    invoice_id=order[4]
                )
            )
        return orders

    @staticmethod
    def get_all() -> list[OrderInDBSchema]:
        cur.execute("""
        SELECT * FROM orders;
        """)
        orders = []
        for order in cur.fetchall():
            orders.append(
                OrderInDBSchema(
                    id=order[0],
                    bot_user_id=order[1],
                    date_create=order[2],
                    status_id=order[3],
                    invoice_id=order[4]
                )
            )
        return orders

    @staticmethod
    def update(order_id: int, order: OrderSchema) -> None:
        cur.execute("""
        UPDATE orders SET (bot_user_id, date_create, status_id, invoice_id) WHERE id = ?;
        """, (order.bot_user_id, order.date_create, order.status_id, order.invoice_id, order_id))
        conn.commit()

    @staticmethod
    def delete(order_id: int) -> None:
        cur.execute("""
        DELETE FROM orders WHERE id = ?;
        """, (order_id, ))
        conn.commit()

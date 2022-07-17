import sqlite3
from Schemas import OrderItemSchema
from Schemas import OrderItemInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class OrderItemCRUD:

    @staticmethod
    def add(order_item: OrderItemSchema) -> None:
        cur.execute("""
        INSERT INTO order_items(order_id, product_id, total);
        """, (order_item.order_id, order_item.product_id, order_item.total))
        conn.commit()

    @staticmethod
    def get(order_item_id: int) -> list[OrderItemInDBSchema]:
        cur.execute("""
        SELECT * FROM order_items WHERE id = ?;
        """, (order_item_id, ))
        order_items = []
        for order_item in cur.fetchall():
            order_items.append(
                OrderItemInDBSchema(
                    id=order_item[0],
                    order_id=order_item[1],
                    product_id=order_item[2],
                    total=order_item[3]
                )
            )
        return order_items

    @staticmethod
    def get_all() -> list[OrderItemInDBSchema]:
        cur.execute("""
        SELECT * FROM order_items;
        """)
        order_items = []
        for order_item in cur.fetchall():
            order_items.append(
                OrderItemInDBSchema(
                    id=order_item[0],
                    order_id=order_item[1],
                    product_id=order_item[2],
                    total=order_item[3]
                )
            )
        return order_items

    @staticmethod
    def update(order_item_id: int, order_item: OrderItemSchema) -> None:
        cur.execute("""
        UPDATE order_items SET (order_id, product_id, total) WHERE id = ?;
        """, (order_item.order_id, order_item.product_id, order_item.total, order_item_id))
        conn.commit()

    @staticmethod
    def delete(order_item_id: int) -> None:
        cur.execute("""
        DELETE FROM order_items WHERE id = ?;
        """, (order_item_id, ))
        conn.commit()

from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models import OrderItem, create_session
from Schemas import OrderItemSchema, OrderItemInDBSchema


class CRUDOrderItem:

    @staticmethod
    @create_session
    def add(order_item: OrderItemSchema, session: Session = None) -> OrderItemInDBSchema | None:
        order_item = OrderItem(
            **order_item.__dict__
        )
        session.add(order_item)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order_item)
            return OrderItemInDBSchema(**order_item.__dict__)

    @staticmethod
    @create_session
    def get(order_item_id: int, session: Session = None) -> OrderItem | None:
        order_item = session.execute(
            select(OrderItem).where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return order_item[0]

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[OrderItem]:
        order_items = session.execute(
            select(OrderItem)
        )
        return [order_item[0] for order_item in order_items.all()]

    @staticmethod
    @create_session
    def delete(order_item_id: int, session: Session = None) -> None:
        session.execute(
            delete(OrderItem).where(OrderItem.id == order_item_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(order_item: OrderItemInDBSchema, session: Session = None) -> None:
        session.execute(
            update(OrderItem).where(OrderItem.id == order_item.id).values(
                **order_item.__dict__
            )
        )
        session.commit()

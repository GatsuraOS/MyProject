from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models import Order, create_session
from Schemas import OrderSchema, OrderInDBSchema


class CRUDOrders:

    @staticmethod
    @create_session
    def add(order: OrderSchema, session: Session = None) -> OrderInDBSchema | None:
        order = Order(
            **order.dict()
        )
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order)
            return OrderInDBSchema(**order.__dict__)

    @staticmethod
    @create_session
    def get(order_id: int, session: Session = None) -> OrderInDBSchema | None:
        order = session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return OrderInDBSchema(**order[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[OrderInDBSchema]:
        orders = session.execute(
            select(Order)
        )
        return [OrderInDBSchema(**order[0].__dict__) for order in orders.all()]

    @staticmethod
    @create_session
    def delete(order_id: int, session: Session = None) -> None:
        session.execute(
            delete(Order).where(Order.id == order_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(order: OrderInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Order).where(Order.id == order.id).values(
                **order.dict()
            )
        )
        session.commit()

from sqlalchemy import delete, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from Models import OrderItem, create_async_session
from Schemas import OrderItemSchema, OrderItemInDBSchema


class CRUDOrderItem:

    @staticmethod
    @create_async_session
    def add(order_item: OrderItemSchema, session: AsyncSession = None) -> OrderItemInDBSchema | None:
        order_item = OrderItem(
            **order_item.dict()
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
    @create_async_session
    def get(order_item_id: int, session: AsyncSession = None) -> OrderItemInDBSchema | None:
        order_item = await session.execute(
            select(OrderItem).where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return OrderItemInDBSchema(**order_item[0].__dict__)

    @staticmethod
    @create_async_session
    def get_all(session: AsyncSession = None) -> list[OrderItemInDBSchema]:
        order_items = await session.execute(
            select(OrderItem)
        )
        return [OrderItemInDBSchema(**order_item[0].__dict__) for order_item in order_items.all()]

    @staticmethod
    @create_async_session
    def delete(order_item_id: int, session: AsyncSession = None) -> None:
        session.execute(
            delete(OrderItem).where(OrderItem.id == order_item_id)
        )
        session.commit()

    @staticmethod
    @create_async_session
    def update(order_item: OrderItemInDBSchema, session: AsyncSession = None) -> None:
        session.execute(
            update(OrderItem).where(OrderItem.id == order_item.id).values(
                **order_item.dict()
            )
        )
        session.commit()

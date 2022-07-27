from sqlalchemy import delete, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from Models import Order, create_async_session
from Schemas import OrderSchema, OrderInDBSchema


class CRUDOrders:

    @staticmethod
    @create_async_session
    async def add(order: OrderSchema, session: AsyncSession = None) -> OrderInDBSchema | None:
        order = Order(
            **order.dict()
        )
        session.add(order)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(order)
            return OrderInDBSchema(**order.__dict__)

    @staticmethod
    @create_async_session
    async def get(order_id: int, session: AsyncSession = None) -> OrderInDBSchema | None:
        order = await session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return OrderInDBSchema(**order[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[OrderInDBSchema]:
        orders = await session.execute(
            select(Order)
        )
        return [OrderInDBSchema(**order[0].__dict__) for order in orders.all()]

    @staticmethod
    @create_async_session
    async def delete(order_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Order).where(Order.id == order_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(order: OrderInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Order).where(Order.id == order.id).values(
                **order.dict()
            )
        )
        await session.commit()

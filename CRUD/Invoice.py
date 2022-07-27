from sqlalchemy import delete, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from Models import Invoice, create_async_session
from Schemas import InvoiceSchema, InvoiceInDBSchema


class CRUDInvoice:

    @staticmethod
    @create_async_session
    async def add(invoice: InvoiceSchema, session: AsyncSession = None) -> InvoiceInDBSchema | None:
        invoice = Invoice(
            **invoice.dict()
        )
        session.add(invoice)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(invoice)
            return InvoiceInDBSchema(**invoice.__dict__)

    @staticmethod
    @create_async_session
    async def get(invoice_id: str, session: AsyncSession = None) -> InvoiceInDBSchema | None:
        invoice = await session.execute(
            select(Invoice).where(Invoice.id == invoice_id)
        )
        invoice = invoice.first()
        if invoice:
            return InvoiceInDBSchema(**invoice[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[InvoiceInDBSchema]:
        invoices = await session.execute(
            select(Invoice)
        )
        return [InvoiceInDBSchema(**invoice[0].__dict__) for invoice in invoices.all()]

    @staticmethod
    @create_async_session
    async def delete(invoice_id: str, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Invoice).where(Invoice.id == invoice_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(invoice: InvoiceInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Invoice).where(Invoice.id == invoice.id).values(
                **invoice.dict()
            )
        )
        await session.commit()

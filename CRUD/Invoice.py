from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from Models import Invoice, create_session
from Schemas import InvoiceSchema, InvoiceInDBSchema


class CRUDInvoice:

    @staticmethod
    @create_session
    def add(invoice: InvoiceSchema, session: Session) -> InvoiceInDBSchema | None:
        invoice = Invoice(
            **invoice.dict()
        )
        session.add(invoice)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(invoice)
            return InvoiceInDBSchema(**invoice.__dict__)

    @staticmethod
    @create_session
    def get(invoice_id: str, session: Session = None) -> InvoiceInDBSchema | None:
        invoice = session.execute(
            select(Invoice).where(Invoice.id == invoice_id)
        )
        invoice = invoice.first()
        if invoice:
            return InvoiceInDBSchema(**invoice[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[InvoiceInDBSchema]:
        invoices = session.execute(
            select(Invoice)
        )
        return [InvoiceInDBSchema(**invoice[0].__dict__) for invoice in invoices.all()]

    @staticmethod
    @create_session
    def delete(invoice_id: str, session: Session = None) -> None:
        session.execute(
            delete(Invoice).where(Invoice.id == invoice_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(invoice: InvoiceInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Invoice).where(Invoice.id == invoice.id).values(
                **invoice.dict()
            )
        )
        session.commit()

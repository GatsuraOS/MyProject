import sqlite3
from Schemas import InvoiceSchema
from Schemas import InvoiceInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class InvoiceCRUD:

    @staticmethod
    def add(invoice: InvoiceSchema) -> None:
        cur.execute("""
        INSERT INTO invoices(bot_user_id, date_create, total, status_id);
        """, (invoice.bot_user_id, invoice.date_create, invoice.total, invoice.status_id))
        conn.commit()

    @staticmethod
    def get(invoice_id: str) -> list[InvoiceInDBSchema]:
        cur.execute("""
        SELECT * FROM invoices WHERE id = ?;
        """, (invoice_id, ))
        invoices = []
        for invoice in cur.fetchall():
            invoices.append(
                InvoiceInDBSchema(
                    id=invoice[0],
                    bot_user_id=invoice[1],
                    date_create=invoice[2],
                    total=invoice[3],
                    status_id=invoice[4]
                )
            )
        return invoices

    @staticmethod
    def get_all() -> list[InvoiceInDBSchema]:
        cur.execute("""
        SELECT * FROM invoices;
        """)
        invoices = []
        for invoice in cur.fetchall():
            invoices.append(
                InvoiceInDBSchema(
                    id=invoice[0],
                    bot_user_id=invoice[1],
                    date_create=invoice[2],
                    total=invoice[3],
                    status_id=invoice[4]
                )
            )
        return invoices

    @staticmethod
    def update(invoice_id: str, invoice: InvoiceSchema) -> None:
        cur.execute("""
        UPDATE invoices SET (bot_user_id, date_create, total, status_id) WHERE id = ?;
        """, (invoice.bot_user_id, invoice.date_create, invoice.total, invoice.status_id, invoice_id))
        conn.commit()

    @staticmethod
    def delete(invoice_id: int) -> None:
        cur.execute("""
        DELETE FROM invoices WHERE id = ?;
        """, (invoice_id, ))
        conn.commit()

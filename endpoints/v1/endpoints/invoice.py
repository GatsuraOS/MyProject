from fastapi import APIRouter, HTTPException, Depends

from Schemas import InvoiceInDBSchema
from CRUD import CRUDInvoice


invoice_router = APIRouter(
    prefix="/invoice"
)


async def check_invoice_id(invoice_id: str) -> str | None:
    invoice = await CRUDInvoice.get(invoice_id=invoice_id)
    if invoice:
        return invoice_id
    else:
        raise HTTPException(status_code=404, detail="invalid invoice_id arrived")


@invoice_router.get("/get", response_model=InvoiceInDBSchema, tags=["Invoice"])
async def get_invoice(invoice_id: str = Depends(check_invoice_id)):
    invoice = await CRUDInvoice.get(invoice_id=invoice_id)
    if invoice:
        return invoice
    else:
        raise HTTPException(status_code=404, detail="invoice was not found")


@invoice_router.get("/all", response_model=list[InvoiceInDBSchema], tags=["Invoice"])
async def get_all_invoices():
    invoices = await CRUDInvoice.get_all()
    if invoices:
        return invoices
    else:
        raise HTTPException(status_code=404, detail="invoices are not found")


@invoice_router.post("/add", response_model=InvoiceInDBSchema, tags=["Invoice"])
async def add_invoice(invoice: InvoiceInDBSchema):
    invoice = await CRUDInvoice.add(invoice=invoice)
    if invoice:
        return invoice
    else:
        raise HTTPException(status_code=404, detail="this invoice is exist")


@invoice_router.delete("/del", tags=["Invoice"])
async def delete_invoice(invoice_id: str = Depends(check_invoice_id)):
    await CRUDInvoice.delete(invoice_id=invoice_id)
    raise HTTPException(status_code=200, detail=f"invoice with id {invoice_id} was deleted")


@invoice_router.put("/update", tags=["Invoice"])
async def update_invoice(invoice: InvoiceInDBSchema):
    await CRUDInvoice.update(invoice=invoice)
    raise HTTPException(status_code=200, detail="invoice was updated")

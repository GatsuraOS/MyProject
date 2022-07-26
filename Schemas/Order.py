from datetime import datetime

from pydantic import BaseModel, Field
from . import BotUserInDBSchema
from . import StatusInDBSchema
from . import InvoiceInDBSchema


class OrderSchema(BaseModel):
    bot_user_id: list[BotUserInDBSchema]
    date_create: datetime = Field(default=datetime.now())
    status_id: list[StatusInDBSchema]
    invoice_id: list[InvoiceInDBSchema]


class OrderInDBSchema(OrderSchema):
    id: int = Field(ge=1)

from datetime import datetime

from pydantic import BaseModel, Field
from . import BotUserInDBSchema
from . import StatusInDBSchema


class InvoiceSchema(BaseModel):
    bot_user_id: list[BotUserInDBSchema]
    date_create: datetime = Field(default=datetime.now())
    total: float = Field(default=0)
    status_id: list[StatusInDBSchema]


class InvoiceInDBSchema(InvoiceSchema):
    id: str = Field(max_length=15)

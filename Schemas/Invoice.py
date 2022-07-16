from pydantic import BaseModel, Field
from . import BotUserInDBSchema
from . import StatusInDBSchema


class InvoiceSchema(BaseModel):
    bot_user_id: list[BotUserInDBSchema]
    date_create: int | float
    total: int = Field(default=0)
    status_id: list[StatusInDBSchema]


class InvoiceInDBSchema(InvoiceSchema):
    id: str = Field(max_length=15)

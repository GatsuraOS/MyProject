from datetime import datetime

from pydantic import BaseModel, Field


class InvoiceSchema(BaseModel):
    bot_user_id: str = Field(max_length=20)
    date_create: datetime = Field(default=datetime.now())
    total: int = Field(default=0)
    status_id: int = Field(ge=1)


class InvoiceInDBSchema(InvoiceSchema):
    id: str = Field(max_length=15)

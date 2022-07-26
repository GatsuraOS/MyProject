from datetime import datetime

from pydantic import BaseModel, Field


class OrderSchema(BaseModel):
    bot_user_id: str = Field(max_length=20)
    date_create: datetime = Field(default=datetime.now())
    status_id: int = Field(ge=1)
    invoice_id: str = Field(max_length=15)


class OrderInDBSchema(OrderSchema):
    id: int = Field(ge=1)

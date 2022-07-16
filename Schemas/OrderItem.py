from pydantic import BaseModel, Field
from . import OrderInDBSchema
from . import ProductInDBSchema


class OrderItemSchema(BaseModel):
    order_id: list[OrderInDBSchema]
    product_id: list[ProductInDBSchema]
    total: int = Field(default=0)


class OrderItemInDBSchema(OrderItemSchema):
    id: int = Field(ge=1)

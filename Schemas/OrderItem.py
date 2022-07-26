from pydantic import BaseModel, Field


class OrderItemSchema(BaseModel):
    order_id: int = Field(ge=1)
    product_id: int = Field(ge=1)
    total: int = Field(default=0)


class OrderItemInDBSchema(OrderItemSchema):
    id: int = Field(ge=1)

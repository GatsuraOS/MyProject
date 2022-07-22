from pydantic import BaseModel, Field
from . import CategoryInDBSchema


class ProductSchema(BaseModel):
    category_id: list[CategoryInDBSchema]
    price: int = Field(default=0)
    total: int = Field(default=0)
    is_published: bool = Field(default=False)
    name: str = Field(max_length=24)


class ProductInDBSchema(ProductSchema):
    id: int = Field(ge=1)


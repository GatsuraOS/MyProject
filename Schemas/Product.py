from pydantic import BaseModel, Field
from . import CategoryInDBSchema


class ProductSchema(BaseModel):
    category_id: list[CategoryInDBSchema]
    price: int = Field(default=None)
    total: int = Field(default=None)
    is_published: bool = Field(default=False)
    name: str = Field(max_length=20)
    name_en: str = Field(default=None)


class ProductInDBSchema(ProductSchema):
    id: int = Field(ge=1)


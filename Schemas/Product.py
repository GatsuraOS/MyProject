from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    category_id: int = Field(ge=1)
    price: float = Field(default=0)
    total: int = Field(default=0)
    is_published: bool = Field(default=False)
    name: str = Field(max_length=24)


class ProductInDBSchema(ProductSchema):
    id: int = Field(ge=1)

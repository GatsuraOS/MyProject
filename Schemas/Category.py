from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    parent_id: int = Field(
        default=None,
        ge=1
    )
    is_published: bool
    name: str = Field(max_length=20, unique_items=True)


class CategoryInDBSchema(CategorySchema):
    id: int = Field(ge=1)

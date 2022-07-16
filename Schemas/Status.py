from pydantic import BaseModel, Field


class StatusSchema(BaseModel):
    name: str = Field(
        default="new",
        max_length=15
    )


class StatusInDBSchema(StatusSchema):
    id: int = Field(ge=1)

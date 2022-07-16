from pydantic import BaseModel, Field


class LanguageSchema(BaseModel):
    language_code: int = Field(
        default="eng",
        max_length=10
    )


class LanguageInDBSchema(LanguageSchema):
    id: int = Field(ge=1)
from pydantic import BaseModel, Field


class LanguageSchema(BaseModel):
    language_code: str = Field(max_length=10)


class LanguageInDBSchema(LanguageSchema):
    id: int = Field(ge=1)

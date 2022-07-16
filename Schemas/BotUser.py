from pydantic import BaseModel, Field
from . import LanguageInDBSchema


class BotUserSchema(BaseModel):
    is_blocked: bool = Field(default=False)
    balance: int = Field(default=0)
    language_id: list[LanguageInDBSchema]


class BotUserInDBSchema(BotUserSchema):
    id: str = Field(max_length=20)

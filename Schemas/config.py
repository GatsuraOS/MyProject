from pydantic import BaseModel, PostgresDsn


class DatabaseSchema(BaseModel):
    URI: PostgresDsn


class ConfigSchema(BaseModel):
    DATABASE: DatabaseSchema


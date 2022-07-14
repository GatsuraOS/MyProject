from pydantic import BaseModel, Field, validator
import datetime


class Categories(BaseModel):
    id: str = Field(min_length=2)
    parent_id: int | None
    is_published: bool
    name: str
    name_en: str | None


class Products(BaseModel):
    id: str = Field(min_length=7)
    category_id: list[Categories]
    price: int
    media: str | None
    total: int | None
    is_published: bool
    name: str
    name_en: str | None


class Language(BaseModel):
    id: str = Field(max_length=3)
    language_code: int


class BotUsers(BaseModel):
    id: str
    is_blocked: bool
    balance: int | None
    language_id: list[Language]


class Status(BaseModel):
    id: int
    name: str = Field(max_length=3)


class Invoices(BaseModel):
    id: str
    bot_user_id: list[BotUsers]
    data_create: int
    total: int | None
    status_id: list[Status]


class Orders(BaseModel):
    id: str
    bot_user_id: list[BotUsers]
    data_create: int
    status_id: list[Status]
    invoice_id: list[Invoices]


class OrderItems(BaseModel):
    id: str
    order_id: list[Orders]
    product_id: list[Products]
    total: int | None


    @validator("data_create", pre=True)
    def validate_date(cls, data_create: int | datetime):
        if isinstance(data_create, (int, float)):
            return data_create
        elif isinstance(data_create, datetime):
            return data_create.timestamp()
        raise TypeError("argument data_create must be int or datetime")


data = {
    "id": "1354897",
    "order_id": {
        "id": "123548798",
        "bot_user_id": {
            "id": "123",
            "is_blocked": False,
            "language_id": {
                "id": "eng",
                "language_code": 1
            },
        },
        "data_create": datetime.now(),
        "status_id": {
            "id": "2",
            "name": "act"
        },
        "invoice_id": {
            "id": "123123",
            "bot_user_id": {
                "id": "123",
                "is_blocked": False,
                "language_id": {
                    "id": "eng",
                    "language_code": 1
                },
            },
            "data_create": datetime.now().timestamp,
            "status_id": {
                "id": "2",
                "name": "act"
            },
        },
    },
    "product_id": {
        "id": "1234567",
        "category_id": {
            "id": "1222855",
            "is_published": True,
            "name": "products"
        },
        "price": 2,
        "is_published": True,
        "name": "milk"
    },
}


order_item = OrderItems(**data)

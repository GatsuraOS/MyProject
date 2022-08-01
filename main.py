from fastapi import FastAPI

from endpoints.v1 import api_v1_router


tags = [
    {
        "name": "Category",
        "description": "endpoints for category"
    },
    {
        "name": "Product",
        "description": "endpoints for product"
    },
    {
        "name": "Language",
        "description": "endpoints for language"
    },
    {
        "name": "Status",
        "description": "endpoints for status"
    },
    {
        "name": "Invoice",
        "description": "endpoints for invoice"
    },
    {
        "name": "BotUser",
        "description": "endpoints for bot_user"
    },
    {
        "name": "Order",
        "description": "endpoints for order"
    },
    {
        "name": "OrderItem",
        "description": "endpoints for order_item"
    }
]

app = FastAPI(
    title="BelHard",
    description="Belhard lesson",
    openapi_tags=tags
)
app.include_router(api_v1_router)

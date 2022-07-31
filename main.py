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
    }
]

app = FastAPI(
    title="BelHard",
    description="Belhard lesson",
    openapi_tags=tags
)
app.include_router(api_v1_router)
from fastapi import FastAPI

from endpoints.v1 import api_v1_router


app = FastAPI(
    title="BelHard",
    description="Belhard lesson"
)
app.include_router(api_v1_router)
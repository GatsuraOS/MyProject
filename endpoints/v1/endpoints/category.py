from fastapi import APIRouter, HTTPException

from  Schemas import  CategorySchema, CategoryInDBSchema
from CRUD import CRUDCategory


category_router = APIRouter(
    prefix="/category"
)


@category_router.get("/get", response_model=CategoryInDBSchema)
async def get_category(category_id: int):
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="category not found")
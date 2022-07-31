from fastapi import APIRouter, HTTPException

from Schemas import CategorySchema, CategoryInDBSchema
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


@category_router.get("/all", response_model=list[CategoryInDBSchema])
async def get_all_categories():
    categories = await CRUDCategory.get_all()
    if categories:
        return categories
    else:
        raise HTTPException(status_code=404, detail="categories not found")


@category_router.post("/add", response_model=CategoryInDBSchema)
async def add_category(category: CategorySchema):
    category = await CRUDCategory.add(category=category)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="category is exist")

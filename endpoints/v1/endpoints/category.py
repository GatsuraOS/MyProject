from fastapi import APIRouter, HTTPException, Depends

from Schemas import CategorySchema, CategoryInDBSchema, ProductInDBSchema
from CRUD import CRUDCategory


category_router = APIRouter(
    prefix="/category"
)


async def check_category_id(category_id: int) -> int | None:
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return category_id
    else:
        raise HTTPException(status_code=404, detail="invalid category_id arrived")


@category_router.get("/get", response_model=CategoryInDBSchema, tags=["Category"])
async def get_category(category_id: int = Depends(check_category_id)):
    category = await CRUDCategory.get(category_id=category_id)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="category not found")


@category_router.get("/all", response_model=list[CategoryInDBSchema], tags=["Category"])
async def get_all_categories(parent_id: int = None):
    categories = await CRUDCategory.get_all(parent_id=parent_id)
    if categories:
        return categories
    else:
        raise HTTPException(status_code=404, detail="categories not found")


@category_router.post("/add", response_model=CategoryInDBSchema, tags=["Category"])
async def add_category(category: CategorySchema):
    category = await CRUDCategory.add(category=category)
    if category:
        return category
    else:
        raise HTTPException(status_code=404, detail="category is exist")


@category_router.delete("/del", tags=["Category"])
async def delete_category(category_id: int = Depends(check_category_id)):
    await CRUDCategory.delete(category_id=category_id)
    raise HTTPException(status_code=200, detail="category was deleted")


@category_router.put("/update", tags=["Category"])
async def update_category(category: CategoryInDBSchema):
    await CRUDCategory.update(category=category)
    raise HTTPException(status_code=200, detail="category was updated")


@category_router.get("/get_products",
                     response_model=list[tuple[CategoryInDBSchema, ProductInDBSchema]],
                     tags=["Category"])
async def get_products_from_category(category_id: int = None):
    products = await CRUDCategory.get_products(category_id=category_id)
    if products:
        return products
    else:
        raise HTTPException(status_code=404, detail="category not found")

from fastapi import APIRouter, HTTPException

from Schemas import ProductSchema, ProductInDBSchema
from CRUD import CRUDProduct


product_router = APIRouter(
    prefix="/product"
)


@product_router.get("/get", response_model=ProductInDBSchema)
async def get_product(product_id: int):
    product = await CRUDProduct.get(product_id=product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail=f"product with id {product_id} not found")

from fastapi import APIRouter, HTTPException

from Schemas import ProductSchema, ProductInDBSchema
from CRUD import CRUDProduct


product_router = APIRouter(
    prefix="/product"
)


@product_router.get("/get", response_model=ProductInDBSchema, tags=["Product"])
async def get_product(product_id: int):
    product = await CRUDProduct.get(product_id=product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail=f"product with id {product_id} not found")


@product_router.get("/all", response_model=ProductInDBSchema, tags=["Product"])
async def get_all_products():
    products = await CRUDProduct.get_all()
    if products:
        return products
    else:
        HTTPException(status_code=404, detail="products not found")


@product_router.post("/add", tags=["Product"])
async def add_product(product: ProductSchema):
    product = await CRUDProduct.add(product=product)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="this product is exist")


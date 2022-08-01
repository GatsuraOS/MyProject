from fastapi import APIRouter, HTTPException, Depends

from Schemas import ProductSchema, ProductInDBSchema
from CRUD import CRUDProduct


product_router = APIRouter(
    prefix="/product"
)


async def check_product_id(product_id: int) -> int | None:
    product = await CRUDProduct.get(product_id=product_id)
    if product:
        return product_id
    else:
        raise HTTPException(status_code=404, detail="invalid product_id arrived")


@product_router.get("/get", response_model=ProductInDBSchema, tags=["Product"])
async def get_product(product_id: int = Depends(check_product_id)):
    product = await CRUDProduct.get(product_id=product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail=f"product with id {product_id} not found")


@product_router.get("/all", response_model=list[ProductInDBSchema], tags=["Product"])
async def get_all_products():
    products = await CRUDProduct.get_all()
    if products:
        return products
    else:
        HTTPException(status_code=404, detail="products not found")


@product_router.post("/add", response_model=ProductInDBSchema, tags=["Product"])
async def add_product(product: ProductSchema):
    product = await CRUDProduct.add(product=product)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="this product is exist")


@product_router.delete("/del", tags=["Product"])
async def delete_product(product_id: int = Depends(check_product_id)):
    await CRUDProduct.delete(product_id=product_id)
    raise HTTPException(status_code=200, detail=f"product with id {product_id} was deleted")


@product_router.put("/update", tags=["Product"])
async def update_product(product: ProductInDBSchema):
    await CRUDProduct.update(product=product)
    raise HTTPException(status_code=200, detail="product was updated")

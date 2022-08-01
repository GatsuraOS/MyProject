from fastapi import APIRouter, HTTPException, Depends

from Schemas import OrderSchema, OrderInDBSchema
from CRUD import CRUDOrders


order_router = APIRouter(
    prefix="/order"
)


async def check_order_id(order_id: int) -> int | None:
    order = await CRUDOrders.get(order_id=order_id)
    if order:
        return order_id
    else:
        raise HTTPException(status_code=404, detail="invalid order_id arrived")


@order_router.get("/get", response_model=OrderInDBSchema, tags=["Order"])
async def get_order(order_id: int = Depends(check_order_id)):
    order = await CRUDOrders.get(order_id=order_id)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="order was not found")


@order_router.get("/all", response_model=list[OrderInDBSchema], tags=["Order"])
async def get_all_order():
    orders = await CRUDOrders.get_all()
    if orders:
        return orders
    else:
        raise HTTPException(status_code=404, detail="orders are not found")


@order_router.post("/add", response_model=OrderInDBSchema, tags=["Order"])
async def add_order(order: OrderSchema):
    order = await CRUDOrders.add(order=order)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="this order is exist")


@order_router.delete("/del", tags=["Order"])
async def delete_order(order_id: int = Depends(check_order_id)):
    await CRUDOrders.delete(order_id=order_id)
    raise HTTPException(status_code=200, detail=f"order with id {order_id} was deleted")


@order_router.put("/update", tags=["Order"])
async def update_order(order: OrderInDBSchema):
    await CRUDOrders.update(order=order)
    raise HTTPException(status_code=200, detail="order was updated")

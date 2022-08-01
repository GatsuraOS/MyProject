from fastapi import APIRouter, HTTPException, Depends

from Schemas import OrderItemSchema, OrderItemInDBSchema
from CRUD import CRUDOrderItem


order_item_router = APIRouter(
    prefix="/order_item"
)


async def check_order_item_id(order_item_id: int) -> int | None:
    order_item = await CRUDOrderItem.get(order_item_id=order_item_id)
    if order_item:
        return order_item_id
    else:
        raise HTTPException(status_code=404, detail="invalid order_item_id arrived")


@order_item_router.get("/get", response_model=OrderItemInDBSchema, tags=["OrderItem"])
async def get_order_item(order_item_id: int = Depends(check_order_item_id)):
    order_item = await CRUDOrderItem.get(order_item_id=order_item_id)
    if order_item:
        return order_item
    else:
        raise HTTPException(status_code=404, detail="order_item was not found")


@order_item_router.get("/all", response_model=list[OrderItemInDBSchema], tags=["OrderItem"])
async def get_all_order_item():
    orders_item = await CRUDOrderItem.get_all()
    if orders_item:
        return orders_item
    else:
        raise HTTPException(status_code=404, detail="orders_item are not found")


@order_item_router.post("/add", response_model=OrderItemInDBSchema, tags=["OrderItem"])
async def add_order_item(order_item: OrderItemSchema):
    order_item = await CRUDOrderItem.add(order_item=order_item)
    if order_item:
        return order_item
    else:
        raise HTTPException(status_code=404, detail="this order_item is exist")


@order_item_router.delete("/del", tags=["OrderItem"])
async def delete_order_item(order_item_id: int = Depends(check_order_item_id)):
    await CRUDOrderItem.delete(order_item_id=order_item_id)
    raise HTTPException(status_code=200, detail=f"order_item with id {order_item_id} was deleted")


@order_item_router.put("/update", tags=["OrderItem"])
async def update_order_item(order_item: OrderItemInDBSchema):
    await CRUDOrderItem.update(orde_itemr=order_item)
    raise HTTPException(status_code=200, detail="order_item was updated")

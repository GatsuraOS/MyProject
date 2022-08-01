from fastapi import APIRouter, HTTPException, Depends

from Schemas import StatusSchema, StatusInDBSchema
from CRUD import CRUDStatus


status_router = APIRouter(
    prefix="/status"
)


async def check_status_id(status_id: int) -> int | None:
    status = await CRUDStatus.get(status_id=status_id)
    if status:
        return status_id
    else:
        raise HTTPException(status_code=404, detail="invalid status_id arrived")


@status_router.get("/get", response_model=StatusInDBSchema, tags=["Status"])
async def get_status(status_id: int = Depends(check_status_id)):
    status = await CRUDStatus.get(status_id=status_id)
    if status:
        return status
    else:
        raise HTTPException(status_code=404, detail="status was not found")


@status_router.get("/all", response_model=list[StatusInDBSchema], tags=["Status"])
async def get_all_statuses():
    statuses = await CRUDStatus.get_all()
    if statuses:
        return statuses
    else:
        raise HTTPException(status_code=404, detail="statuses are not found")


@status_router.post("/add", response_model=StatusInDBSchema, tags=["Status"])
async def add_status(status: StatusSchema):
    status = await CRUDStatus.add(status=status)
    if status:
        return status
    else:
        raise HTTPException(status_code=404, detail="this status is exist")


@status_router.delete("/del", tags=["Status"])
async def delete_status(status_id: int = Depends(check_status_id)):
    await CRUDStatus.delete(status_id=status_id)
    raise HTTPException(status_code=200, detail=f"status with id {status_id} was deleted")


@status_router.put("/update", tags=["Status"])
async def update_status(status: StatusInDBSchema):
    await CRUDStatus.update(status=status)
    raise HTTPException(status_code=200, detail="status was updated")

from fastapi import APIRouter

from  Schemas import  CategorySchema, CategoryInDBSchema
from CRUD import CRUDCategory


category_router = APIRouter(
    prefix="/category"
)
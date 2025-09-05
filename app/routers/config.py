from fastapi import APIRouter
from app.routers.product import router as product

api_router = APIRouter()
api_router.include_router(product, prefix="/products")

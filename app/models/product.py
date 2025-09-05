from app.models.base import CreateBaseModel
from app.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...

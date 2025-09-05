from decimal import Decimal
from typing import Annotated
from bson import Decimal128
from pydantic import AfterValidator, Field
from app.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    description: str = Field(..., description="Product description")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    desciption: str | None = Field(
        default=None,
        description="Product description",
    )
    quantity: int | None = Field(
        default=None,
        description="Product quantity",
    )
    price: Decimal_ | None = Field(
        default=None,
        description="Product price",
    )
    status: bool | None = Field(
        default=None,
        description="Product status",
    )


class ProductUpdateOut(ProductOut):
    ...

from enum import Enum

from lib.command import Command
from typing import Optional
from pydantic import BaseModel


class AddBatch(Command):
    sku: str
    purchased_quantity: int
    eta: Optional[str]


class UpdateBatch(BaseModel):
    ref: Optional[str] = None
    sku: Optional[str] = None
    purchased_quantity: Optional[int] = None
    eta: Optional[str] = None


class ProductTypeEnum(str, Enum):
    standard = "Standard"
    combo = "Combo"
    digital = "Digital"
    service = "Service"


class BarcodeSymbologyEnum(str, Enum):
    crem01 = "CREM01"
    um01 = "UM01"
    sem01 = "SEM01"
    cof01 = "COF01"
    fun01 = "FUN01"
    dis01 = "DIS01"
    nis01 = "NIS01"


class CategoryEnum(str, Enum):
    beauty = "Beauty"
    grocery = "Grocery"
    food = "Food"
    furniture = "Furniture"
    shoes = "Shoes"
    frames = "Frames"
    jewellery = "Jewellery"


class TaxMethodEnum(str, Enum):
    exclusive = "Exclusive"
    inclusive = "Inclusive"


class AddProduct(Command):
    product_type: ProductTypeEnum
    name: str
    code: str
    barcode_symbology: BarcodeSymbologyEnum
    category: CategoryEnum
    cost: float
    price: float
    tax_method: TaxMethodEnum
    quantity: int
    image: str
    discription: str


class UpdateProduct(BaseModel):
    id_: Optional[str] = None
    product_type: Optional[ProductTypeEnum] = None
    name: Optional[str] = None
    code: Optional[str] = None
    barcode_symbology: Optional[BarcodeSymbologyEnum] = None
    category: Optional[CategoryEnum] = None
    cost: Optional[float] = None
    price: Optional[float] = None
    tax_method: Optional[TaxMethodEnum] = None
    quantity: Optional[int] = None
    image: Optional[str] = None
    discription: Optional[str] = None




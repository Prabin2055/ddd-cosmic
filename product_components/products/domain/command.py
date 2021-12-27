import uuid
from enum import Enum
from lib.command import Command
from typing import Optional
from product_components.products.domain import model


class AddBatch(Command):
    sku: str
    purchased_quantity: int
    eta: str


class UpdateBatchCommand(Command):
    batch: model.Batch = None


class UpdateBatch(UpdateBatchCommand):
    ref: uuid.UUID
    sku: str
    purchased_quantity: int
    eta: str


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


class UpdateProductCommand(Command):
    product: model.Product = None


class UpdateProduct(UpdateProductCommand):
    id_: uuid.UUID
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




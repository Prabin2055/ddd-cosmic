from enum import Enum
from lib.command import Command
from typing import Optional
from pydantic import BaseModel


class SupplierEnum(str, Enum):
    select_supplier = "SelectSupplier"
    test_supplier = "TestSupplier"


class ReceivedEnum(str, Enum):
    received = "Received"
    not_received_yet = "NotReceivedYet"


class OrderTaxEnum(str, Enum):
    no_tax = "NoTax"
    gst = "GST@5%"
    vat = "VAT@20%"


class AddPurchase(Command):
    date: str
    purchase_no: str
    supplier: SupplierEnum
    received: ReceivedEnum
    order_tax: OrderTaxEnum
    discount: float
    shipping: str
    payment: float
    note: str


class UpdatePurchase(BaseModel):
    id_: Optional[str] = None
    date: Optional[str] = None
    purchase_no: Optional[str] = None
    supplier: Optional[SupplierEnum] = None
    received: Optional[ReceivedEnum] = None
    order_tax: Optional[OrderTaxEnum] = None
    discount: Optional[float] = None
    shipping: Optional[str] = None
    payment: Optional[float] = None
    note: Optional[str] = None





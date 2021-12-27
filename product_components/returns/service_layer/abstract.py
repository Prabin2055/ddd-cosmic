from enum import Enum

from lib.command import Command
from typing import Optional
from pydantic import BaseModel


class BillerEnum(str, Enum):
    test_biller = "TestBiller"


class OrderTaxEnum(str, Enum):
    no_tax = "NoTax"
    gst = "GST@5%"
    vat = "VAT@10%"


class AddReturn(Command):
    date: str
    reference_no: str
    biller: BillerEnum
    customer: str
    order_tax: OrderTaxEnum
    order_discount: float
    shipping: str
    attach_document: str
    return_note: str


class UpdateReturn(BaseModel):
    id_: Optional[str] = None
    date: Optional[str] = None
    reference_no: Optional[str] = None
    biller: Optional[BillerEnum] = None
    customer: Optional[str] = None
    order_tax: Optional[OrderTaxEnum] = None
    order_discount: Optional[float] = None
    shipping: Optional[str] = None
    attach_document: Optional[str] = None
    return_note: Optional[str] = None

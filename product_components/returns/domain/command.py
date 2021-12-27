import uuid
from enum import Enum
from lib.command import Command
from typing import Optional
from product_components.returns.domain import model


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


class UpdateReturnCommand(Command):
    returns: model.Return = None


class UpdateReturn(UpdateReturnCommand):
    id_: uuid.UUID
    date: str
    reference_no: str
    biller: BillerEnum
    customer: str
    order_tax: OrderTaxEnum
    order_discount: float
    shipping: str
    attach_document: str
    return_note: str




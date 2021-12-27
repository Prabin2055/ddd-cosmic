import uuid
from enum import Enum
from lib.command import Command
from typing import Optional
from product_components.sale.domain import model


class BillerEnum(str, Enum):
    test_biller = "TestBiller"


class OrderTaxEnum(str, Enum):
    no_tax = "NoTax"
    gst = "GST@5%"
    vat = "VAT@10%"


class SaleStatusEnum(str, Enum):
    completed = "Completed"
    pending = "Pending"


class PaymentStatusEnum(str, Enum):
    pending = "Pending"
    due = "Due"
    paid = "Paid"


class AddSale(Command):
    date: str
    reference_no: str
    biller: BillerEnum
    customer: str
    order_tax: OrderTaxEnum
    order_discount: float
    shipping: str
    attach_document: str
    sales_status: SaleStatusEnum
    payment_status: PaymentStatusEnum
    sales_note: str


class UpdateSaleCommand(Command):
    sale: model.Sale = None


class UpdateSale(UpdateSaleCommand):
    id_: uuid.UUID
    date: str
    reference_no: str
    biller: BillerEnum
    customer: str
    order_tax: OrderTaxEnum
    order_discount: float
    shipping: str
    attach_document: str
    sales_status: SaleStatusEnum
    payment_status: PaymentStatusEnum
    sales_note: str




import uuid
from enum import Enum
from lib.command import Command
from order_components.purchases.domain import model


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


class UpdatePurchaseCommand(Command):
    purchase: model.Purchase = None


class UpdatePurchase(UpdatePurchaseCommand):
    id_: uuid.UUID
    date: str
    purchase_no: str
    supplier: SupplierEnum
    received: ReceivedEnum
    order_tax: OrderTaxEnum
    discount: float
    shipping: str
    payment: float
    note: str




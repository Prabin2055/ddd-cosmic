from __future__ import annotations
import datetime
import uuid
from enum import Enum
from pydantic import BaseModel as Model
from typing import Any, Dict, Optional
from datetime import date


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


class Purchase(Model):
    id_: uuid.UUID
    date: str
    purchase_no: str
    supplier: SupplierEnum
    received: ReceivedEnum
    order_tax: OrderTaxEnum
    discount: float
    quantity: int
    shipping: str
    payment: float
    note: str

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "purchase"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.id_)

    async def update(self, mapping: Dict[str, Any]) -> Purchase:
        return self.copy(update=mapping)


async def purchase_factory(
        date: str,
        purchase_no: str,
        supplier: SupplierEnum,
        received: ReceivedEnum,
        order_tax: OrderTaxEnum,
        discount: float,
        shipping: str,
        payment: float,
        note: str
) -> Purchase:
    return Purchase(
        id_=uuid.uuid4(),
        date=date,
        purchase_no=purchase_no,
        supplier=supplier,
        received=received,
        order_tax=order_tax,
        discount=discount,
        shipping=shipping,
        payment=payment,
        note=note,

    )

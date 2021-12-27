from __future__ import annotations
import datetime
import uuid
from enum import Enum
from pydantic import BaseModel as Model
from typing import Any, Dict, Optional
from datetime import date


class BillerEnum(str, Enum):
    test_biller = "TestBiller"


class OrderTaxEnum(str, Enum):
    no_tax = "NoTax"
    gst = "GST@%%"
    vat = "VAT@10%"


class SaleStatusEnum(str, Enum):
    completed = "Completed"
    pending = "Pending"


class PaymentStatusEnum(str, Enum):
    pending = "Pending"
    due = "Due"
    paid = "Paid"


class Sale(Model):
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

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "sale"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.id_)

    async def update(self, mapping: Dict[str, Any]) -> Sale:
        return self.copy(update=mapping)


async def sale_factory(
        date: str,
        reference_no: str,
        biller: BillerEnum,
        customer: str,
        order_tax: OrderTaxEnum,
        order_discount: float,
        shipping: str,
        attach_document: str,
        sales_status: SaleStatusEnum,
        payment_status: PaymentStatusEnum,
        sales_note: str,
) -> Sale:
    return Sale(
        id_=uuid.uuid4(),
        date=date,
        reference_no=reference_no,
        biller=biller,
        customer=customer,
        order_tax=order_tax,
        order_discount=order_discount,
        shipping=shipping,
        attach_document=attach_document,
        sales_status=sales_status,
        payment_status=payment_status,
        sales_note=sales_note,
    )

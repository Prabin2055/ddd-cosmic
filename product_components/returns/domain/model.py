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


class Return(Model):
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

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "sale"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.id_)

    async def update(self, mapping: Dict[str, Any]) -> Return:
        return self.copy(update=mapping)


async def return_factory(
        date: str,
        reference_no: str,
        biller: BillerEnum,
        customer: str,
        order_tax: OrderTaxEnum,
        order_discount: float,
        shipping: str,
        attach_document: str,
        return_note: str,
) -> Return:
    return Return(
        id_=uuid.uuid4(),
        date=date,
        reference_no=reference_no,
        biller=biller,
        customer=customer,
        order_tax=order_tax,
        order_discount=order_discount,
        shipping=shipping,
        attach_document=attach_document,
        return_note=return_note,
    )

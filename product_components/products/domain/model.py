from __future__ import annotations
import datetime
import uuid
from enum import Enum
from pydantic import BaseModel as Model
from typing import Any, Dict, Optional
from datetime import date
from order_components.purchases.domain import model
from typing import List
from lib import event
from product_components.products.domain import events


class Batch(Model):
    ref: uuid.UUID
    sku: str
    eta: Optional[str]
    purchased_quantity: int
    allocations = set()

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "batch"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.ref)

    async def update(self, mapping: Dict[str, Any]) -> Batch:
        return self.copy(update=mapping)

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.ref == self.ref

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def __lt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta < other.eta

    async def allocate(self, line: model.Purchase):
        if await self.can_allocate(line):
            self.allocations.add(line)

    async def deallocate(self, line: model.Purchase):
        if line in await self.allocations:
            self.allocations.remove(line)

    async def deallocate_one(self) -> model.Purchase:
        return self.allocations.pop()

    @property
    async def allocate_quantity(self) -> int:
        return int(sum(line.qty for line in self.allocations))

    @property
    async def available_quantity(self) -> int:
        return int(self.purchased_quantity) - int(await self.allocate_quantity)

    async def can_allocate(self, line: model.Purchase) -> bool:
        return self.sku == line.purchase_no and self.available_quantity >= line.quantity


async def batch_factory(
        sku: str,
        purchased_quantity: int,
        eta: Optional[str]
) -> Batch:
    return Batch(
        ref=uuid.uuid4(),
        sku=sku,
        purchased_quantity=purchased_quantity,
        eta=eta
    )


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


class Product(Model):
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
    batches: List[Batch]
    events: List[event.Event]

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "product"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.id_)

    async def update(self, mapping: Dict[str, Any]) -> Product:
        return self.copy(update=mapping)

    async def allocate(self, line: model.Purchase) -> str:
        try:
            batch = next(b for b in sorted(self.batches) if b.can_allocate(line))
            print("\n ___before available quantity___")
            print(await batch.allocate_quantity)
            await batch.allocate(line)
            print("\n __ after available quantity__")
            print(await batch.available_quantity)
            self.version_number += 1
            self.events.append(
                events.Allocated(
                    purchase_no=line.purchase_no, sku=line.shipping, purchased_quantity=line.quantity,
                    ref=batch.ref,
                )
            )
            print("\n  ___Event allocated___", events.Allocated)
            return str(batch.ref)
        except StopIteration:
            await self.events.append(events.OutOfStock(sku=line.shipping))
            return "None"
        finally:
            print(events)

    async def change_batch_quantity(self, ref: str, purchased_quantity: int):
        batch = next(b for b in self.batches if str(b.ref) == ref)
        batch.purchased_quantity = purchased_quantity
        while await batch.available_quantity < 0:
            line = await batch.deallocate_one()
            self.events.append(
                events.AllocationRequired(str(line.purchase_no), line.shipping, line.quantity)
            )
        self.events.append(events.BatchQuantityChanged(ref=ref, purchased_quantity=purchased_quantity))
        return "ok"


async def product_factory(
        product_type: ProductTypeEnum,
        name: str,
        code: str,
        barcode_symbology: BarcodeSymbologyEnum,
        category: CategoryEnum,
        cost: float,
        price: float,
        tax_method: TaxMethodEnum,
        quantity: int,
        image: str,
        discription: str
) -> Product:
    return Product(
        id_=uuid.uuid4(),
        product_type=product_type,
        name=name,
        code=code,
        barcode_symbology=barcode_symbology,
        category=category,
        cost=cost,
        price=price,
        tax_method=tax_method,
        quantity=quantity,
        image=image,
        discription=discription
    )

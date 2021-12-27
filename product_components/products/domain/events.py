from lib import event
from dataclasses import dataclass


class BatchAdded(event.Event):
    sku: str
    purchased_quantity: int

    def __hash__(self):
        return hash(self.sku)


class ProductAdded(event.Event):
    name: str
    quantity: int

    def __hash__(self):
        return hash(self.name)


@dataclass
class OutOfStock(event.Event):
    sku: str

    def __hash__(self):
        return hash(self.sku)


@dataclass
class AllocationRequired(event.Event):
    purchase_no: str
    shipping: str
    purchased_quantity: int


@dataclass
class BatchQuantityChanged(event.Event):
    ref: str
    purchased_quantity: int


@dataclass
class Allocated(event.Event):
    purchase_no: str
    sku: str
    purchased_quantity: int
    ref: str

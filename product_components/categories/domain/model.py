from __future__ import annotations
import datetime
import uuid
from enum import Enum
from pydantic import BaseModel as Model
from typing import Any, Dict, Optional


class CategoryEnum(str, Enum):
    beauty = "Beauty"
    grocery = "Grocery"
    food = "Food"
    furniture = "Furniture"
    shoes = "Shoes"
    frames = "Frames"
    jewellery = "Jewellery"


class Category(Model):
    id_: uuid.UUID
    image: str
    product_name: str
    category: CategoryEnum
    code: str

    class Config:
        extra = "forbid"
        allow_mutation = False
        title = "categories"
        arbitrary_types_allowed = True

    def __hash__(self):
        return hash(self.id_)

    async def update(self, mapping: Dict[str, Any]) -> Category:
        return self.copy(update=mapping)


async def category_factory(
        image: str,
        product_name: str,
        category: CategoryEnum,
        code: str,
) -> Category:
    return Category(
        id_=uuid.uuid4(),
        iamge=image,
        product_name=product_name,
        category=category,
        code=code,

    )

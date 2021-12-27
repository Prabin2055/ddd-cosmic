from enum import Enum
from lib.command import Command
from typing import Optional
from pydantic import BaseModel


class CategoryEnum(str, Enum):
    beauty = "Beauty"
    grocery = "Grocery"
    food = "Food"
    furniture = "Furniture"
    shoes = "Shoes"
    frames = "Frames"
    jewellery = "Jewellery"


class AddCategory(Command):
    image: str
    product_name: str
    category: CategoryEnum
    code: str


class UpdateCategory(BaseModel):
    id_: Optional[str] = None
    image: Optional[str] = None
    product_name: Optional[str] = None
    category: Optional[CategoryEnum] = None
    code: Optional[str] = None





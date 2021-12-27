import uuid
from enum import Enum
from lib.command import Command
from typing import Optional
from product_components.categories.domain import model


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


class UpdateCategoryCommand(Command):
    categories: model.Category = None


class UpdateCategory(UpdateCategoryCommand):
    id_: uuid.UUID
    image: str
    product_name: str
    category: CategoryEnum
    code: str




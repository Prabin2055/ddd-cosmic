import pandas as pd
import sqlalchemy as sa
from datetime import datetime, timedelta, date
from sqlalchemy import func, desc

from product_components.categories.adapters.orm import categorie
from lib.db_connection import DbConnection


async def get_category(product_name: str, db: DbConnection):
    query = categorie.select().where(categorie.c.name == product_name)
    result = await db.fetch_one(query=query)
    return result


async def get_category_id(id_: str, db: DbConnection):
    query = categorie.select().where(categorie.c.id == id_)
    result = await db.fetch_one(query=query)
    return result


async def get_all_category(db: DbConnection):
    query = categorie.select()
    result = await db.fetch_all(query=query)
    return result


async def get_categories_by_category(db: DbConnection, category: str):
    query = categorie.select().where(categorie.c.category == category)
    result = await db.fetch_all(query=query)
    return result


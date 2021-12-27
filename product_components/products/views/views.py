import pandas as pd
import sqlalchemy as sa
from datetime import datetime, timedelta, date
from sqlalchemy import func, desc

from product_components.products.adapters.orm import product, batch
from lib.db_connection import DbConnection


async def get_product(name: str, db: DbConnection):
    query = product.select().where(product.c.name == name)
    result = await db.fetch_one(query=query)
    return result


async def get_product_id(id_: str, db: DbConnection):
    query = product.select().where(product.c.id == id_)
    result = await db.fetch_one(query=query)
    return result


async def get_all_products(db: DbConnection):
    query = product.select()
    result = await db.fetch_all(query=query)
    return result


async def get_product_by_category(db: DbConnection, categories: str):
    query = product.select().where(product.c.categories == categories)
    result = await db.fetch_all(query=query)
    return result


async def get_product_by_name(db: DbConnection, name: str):
    query = product.select().where(product.c.name == name)
    result = await db.fetch_all(query=query)
    return result


async def get_batch_by_ref(ref: str, db: DbConnection):
    query = batch.select().where(batch.c.ref == ref)
    result = await db.fetch_one(query=query)
    return result


async def get_all_batch(db: DbConnection):
    query = batch.select()
    result = await db.fetch_all(query=query)
    return result

import pandas as pd
import sqlalchemy as sa
from datetime import datetime, timedelta, date
from sqlalchemy import func, desc

from product_components.sale.adapters.orm import sale
from lib.db_connection import DbConnection


async def get_sale_by_reference_no(reference_no: str, db: DbConnection):
    query = sale.select().where(sale.c.reference_no == reference_no)
    result = await db.fetch_one(query=query)
    return result


async def get_sale_id(id_: str, db: DbConnection):
    query = sale.select().where(sale.c.id == id_)
    result = await db.fetch_one(query=query)
    return result


async def get_all_sales(db: DbConnection):
    query = sale.select()
    result = await db.fetch_all(query=query)
    return result


async def get_sale_by_date(db: DbConnection, date: str):
    query = sale.select().where(sale.c.date == date)
    result = await db.fetch_all(query=query)
    return result



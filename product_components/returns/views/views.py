import pandas as pd
import sqlalchemy as sa
from datetime import datetime, timedelta, date
from sqlalchemy import func, desc

from product_components.returns.adapters.orm import returns
from lib.db_connection import DbConnection


async def get_return_by_reference_no(reference_no: str, db: DbConnection):
    query = returns.select().where(returns.c.reference_no == reference_no)
    result = await db.fetch_all(query=query)
    return result


async def get_return_id(id_: str, db: DbConnection):
    query = returns.select().where(returns.c.id == id_)
    result = await db.fetch_one(query=query)
    return result


async def get_all_returns(db: DbConnection):
    query = returns.select()
    result = await db.fetch_all(query=query)
    return result


async def get_return_by_date(db: DbConnection, date: str):
    query = returns.select().where(returns.c.date == date)
    result = await db.fetch_all(query=query)
    return result



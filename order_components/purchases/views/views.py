from order_components.purchases.adapters.orm import purchase
from lib.db_connection import DbConnection


async def get_purchase(purchase_no: str, db: DbConnection):
    query = purchase.select().where(purchase.c.purchase_no == purchase_no)
    result = await db.fetch_one(query=query)
    return result


async def get_purchase_id(id_: str, db: DbConnection):
    query = purchase.select().where(purchase.c.id == id_)
    result = await db.fetch_one(query=query)
    return result


async def get_purchase_by_date(date: str, db: DbConnection):
    query = purchase.select().where(purchase.c.date == date)
    result = await db.fetch_all(query=query)
    return result


async def get_all_purchases(db: DbConnection):
    query = purchase.select()
    result = await db.fetch_all(query=query)
    return result

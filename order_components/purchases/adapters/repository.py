from lib.repository import Repository, SqlAlchemyRepository
from lib.repository import DbConnection
from order_components.purchases.domain import model
from order_components.purchases.adapters.orm import purchase


class Purchase(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlPurchasesRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Purchase):

        await self.db.execute(
            query=purchase.insert(),
            values={
                "id": model.id_,
                "date": model.date,
                "purchase_no": model.purchase_no,
                "supplier": model.supplier,
                "received": model.received,
                "order_taxes": model.order_tax,
                "discount": model.discount,
                "shipping": model.shipping,
                "payment": model.payment,
                "note": model.note,
            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=purchase.select().where(purchase.c.id == ref),
        )

    async def get_all_purchases(self):
        return await self.db.fetch_all(query=purchase.select())

    async def update(self, model: model.Purchase):
        await self.db.execute(
            query=purchase.update().where(purchase.c.id == model.id_),
            values={
                "id": model.id_,
                "date": model.date,
                "purchase_no": model.purchase_no,
                "supplier": model.supplier,
                "received": model.received,
                "order_taxes": model.order_tax,
                "discount": model.discount,
                "shipping": model.shipping,
                "payment": model.payment,
                "note": model.note,
            },
        )

from lib.repository import Repository, SqlAlchemyRepository
from lib.repository import DbConnection
from product_components.returns.domain import model
from product_components.returns.adapters.orm import returns


class Return(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlReturnsRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Return):
        await self.db.execute(
            query=returns.insert(),
            values={
                "id": model.id_,
                "date": model.date,
                "reference_no": model.reference_no,
                "return_biller": model.biller,
                "customer": model.customer,
                "order_tax": model.order_tax,
                "order_discount": model.order_discount,
                "shipping": model.shipping,
                "attach_document": model.attach_document,
                "return_note": model.return_note,
            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=returns.select().where(returns.c.id == ref),
        )

    async def get_all_returns(self):
        return await self.db.fetch_all(query=returns.select())

    async def update(self, model: model.Return):
        await self.db.execute(
            query=returns.update().where(returns.c.id == model.id_),
            values={
                "id": model.id_,
                "date": model.date,
                "reference_no": model.reference_no,
                "return_biller": model.biller,
                "customer": model.customer,
                "order_tax": model.order_tax,
                "order_discount": model.order_discount,
                "shipping": model.shipping,
                "attach_document": model.attach_document,
                "return_note": model.return_note,
            },
        )

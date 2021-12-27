from lib.repository import Repository, SqlAlchemyRepository
from lib.repository import DbConnection
from product_components.sale.domain import model
from product_components.sale.adapters.orm import sale


class Sale(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlSalesRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Sale):
        await self.db.execute(
            query=sale.insert(),
            values={
                "id": model.id_,
                "date": model.date,
                "reference_no": model.reference_no,
                "sale_biller": model.biller,
                "customer": model.customer,
                "tax": model.order_tax,
                "order_discount": model.order_discount,
                "shipping": model.shipping,
                "attach_document": model.attach_document,
                "sale_status": model.sales_status,
                "payments_status": model.payment_status,
                "sales_note": model.sales_note,
            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=sale.select().where(sale.c.id == ref),
        )

    async def get_all_sales(self):
        return await self.db.fetch_all(query=sale.select())

    async def update(self, model: model.Sale):
        await self.db.execute(
            query=sale.update().where(sale.c.id == model.id_),
            values={
                "id": model.id_,
                "date": model.date,
                "reference_no": model.reference_no,
                "sale_biller": model.biller,
                "customer": model.customer,
                "tax": model.order_tax,
                "order_discount": model.order_discount,
                "shipping": model.shipping,
                "attach_document": model.attach_document,
                "sale_status": model.sales_status,
                "payments_status": model.payment_status,
                "sales_note": model.sales_note,
            },
        )

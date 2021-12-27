from lib.repository import Repository, SqlAlchemyRepository
from lib.repository import DbConnection
from product_components.products.domain import model
from product_components.products.adapters.orm import product, batch


class Product(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlProductsRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Product):

        await self.db.execute(
            query=product.insert(),
            values={
                "id": model.id_,
                "products_type": model.product_type,
                "name": model.name,
                "code": model.code,
                "barcodes_symbology": model.barcode_symbology,
                "categories": model.category,
                "cost": str(model.cost),
                "price": str(model.price),
                "tax_method": model.tax_method,
                "quantity": model.quantity,
                "image": model.image,
                "discription": model.discription,
            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=product.select().where(product.c.id == ref),
        )

    async def get_all_products(self):
        return await self.db.fetch_all(query=product.select())

    async def update(self, model: model.Product):
        await self.db.execute(
            query=product.update().where(product.c.id == model.id_),
            values={
                "id": model.id_,
                "products_type": model.product_type,
                "name": model.name,
                "code": model.code,
                "barcodes_symbology": model.barcode_symbology,
                "categories": model.category,
                "cost": str(model.cost),
                "price": str(model.price),
                "tax_method": model.tax_method,
                "quantity": model.quantity,
                "image": model.image,
                "discription": model.discription,
            },
        )


class Batch(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlBatchesRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Batch):
        await self.db.execute(
            query=batch.insert(),
            values={
                "ref": model.ref,
                "sku": model.sku,
                "purchased_quantity": str(model.purchased_quantity),
                "eta": model.eta,

            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=batch.select().where(batch.c.ref == ref),
        )

    async def get_all_batches(self):
        return await self.db.fetch_all(query=batch.select())

    async def update(self, model: model.Batch):
        await self.db.execute(
            query=batch.update().where(batch.c.ref == model.ref),
            values={
                "ref": model.ref,
                "sku": model.sku,
                "purchased_quantity": str(model.purchased_quantity),
                "eta": model.eta,
            },
        )


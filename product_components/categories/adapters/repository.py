from lib.repository import Repository, SqlAlchemyRepository
from lib.repository import DbConnection
from product_components.categories.domain import model
from product_components.categories.adapters.orm import categorie


class Category(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class SqlCategoryRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(self, model: model.Category):

        await self.db.execute(
            query=categorie.insert(),
            values={
                "id": model.id_,
                "image": model.image,
                "product_name": model.product_name,
                "category": model.category,
                "code": model.code,

            },
        )

    async def get(self, ref: str):
        return await self.db.fetch_one(
            query=categorie.select().where(categorie.c.id == ref),
        )

    async def get_all_categories(self):
        return await self.db.fetch_all(query=categorie.select())

    async def update(self, model: model.Category):
        await self.db.execute(
            query=categorie.update().where(categorie.c.id == model.id_),
            values={
                "id": model.id_,
                "image": model.image,
                "product_name": model.product_name,
                "category": model.category,
                "code": model.code,

            },
        )


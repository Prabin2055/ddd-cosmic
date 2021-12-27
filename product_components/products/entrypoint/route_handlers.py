import json
import pandas as pd
from datetime import datetime
from product_components.products.adapters import repository
from product_components.products.domain import command
from product_components.products.service_layer import abstract, unit_of_work, query
from product_components.products.views import views
from entrypoint.messagebus import messagebus
from lib.err_msg import DATA_NOT_FOUND
from lib import err_msg
from lib.json_encoder import jsonable_encoder
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView


class BatchView(HTTPMethodView):
    async def get(self, request, ref):
        if ref:
            ref = ref
            result = await views.get_batch_by_ref(ref, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        batch = await views.get_all_batch(request.app.ctx.db)
        result = jsonable_encoder(batch)
        return response.json(result)

    async def post(self, request, ref):
        data = abstract.AddBatch(**request.json)
        try:
            await messagebus.handle(
                message=command.AddBatch(**data.dict()),
                uow=unit_of_work.BatchSqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlBatchesRepository,
                ),
            )
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)
        return response.json(data.dict(), status=201)

    async def put(self, request, ref):
        q_model = query.BatchQueryParamModel(ref=str(ref))
        batch_ = abstract.UpdateBatch(ref=q_model.ref, **request.json)
        if q_model.ref:
            try:
                await messagebus.handle(
                    message=command.UpdateBatch(**batch_.dict()),
                    uow=unit_of_work.BatchSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlBatchesRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(batch_.dict())
        return response.json({"error": "url not found"}, status=400)


class ProductView(HTTPMethodView):
    async def get(self, request, id_):
        if id_:
            id = id_
            result = await views.get_product_id(id, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        product = await views.get_all_products(request.app.ctx.db)
        result = jsonable_encoder(product)
        return response.json(result)

    async def post(self, request, id_):
        data = abstract.AddProduct(**request.json)
        try:
            await messagebus.handle(
                message=command.AddProduct(**data.dict()),
                uow=unit_of_work.ProductSqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlProductsRepository,
                ),
            )
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)
        return response.json(data.dict(), status=201)

    async def put(self, request, id_):
        q_model = query.ProductQueryParamModel(id_=id_)
        product_ = abstract.UpdateProduct(id_=q_model.id_, **request.json)
        if q_model.id_:
            try:
                await messagebus.handle(
                    message=command.UpdateProduct(**product_.dict()),
                    uow=unit_of_work.ProductSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlProductsRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(product_.dict())
        return response.json({"error": "url not found"}, status=400)


async def get_product_by_category(request):
    categories = request.args.get("categories")
    if categories:
        product = await views.get_product_by_category(db=request.app.ctx.db, categories=categories, )
        return response.json(jsonable_encoder(product))


async def get_product_by_name(request):
    name = request.args.get("name")
    if name:
        product = await views.get_product_by_name(db=request.app.ctx.db, name=name, )
        return response.json(jsonable_encoder(product))

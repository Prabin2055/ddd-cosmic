import json
import pandas as pd
from datetime import datetime
from product_components.categories.adapters import repository
from product_components.categories.domain import command
from product_components.categories.service_layer import abstract, unit_of_work, query
from product_components.categories.views import views
from entrypoint.messagebus import messagebus
from lib.err_msg import DATA_NOT_FOUND
from lib import err_msg
from lib.json_encoder import jsonable_encoder
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView


class Categoriesiew(HTTPMethodView):
    async def get(self, request, id_):
        if id_:
            id = id_
            result = await views.get_category_id(id, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        category = await views.get_all_category(request.app.ctx.db)
        result = jsonable_encoder(category)
        return response.json(result)

    async def post(self, request, id_):
        data = abstract.AddCategory(**request.json)
        try:
            await messagebus.handle(
                message=command.AddCategory(**data.dict()),
                uow=unit_of_work.CategorySqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlCategoryRepository,
                ),
            )
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)
        return response.json(data.dict(), status=201)

    async def put(self, request, id_):
        q_model = query.CategoryQueryParamModel(id_=id_)
        category_ = abstract.UpdateCategory(id_=q_model.id_, **request.json)
        if q_model.id_:
            try:
                await messagebus.handle(
                    message=command.UpdateCategory(**category_.dict()),
                    uow=unit_of_work.CategorySqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlCategoryRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(category_.dict())
        return response.json({"error": "url not found"}, status=400)


async def get_categories_by_category(request):
    categories = request.args.get("categories")
    if categories:
        product = await views.get_categories_by_category(request.app.ctx.db, categories, )
        return response.json(jsonable_encoder(product))

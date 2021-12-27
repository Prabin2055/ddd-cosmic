import json
import pandas as pd
from datetime import datetime
from product_components.sale.adapters import repository
from product_components.sale.domain import command
from product_components.sale.service_layer import abstract, unit_of_work, query
from product_components.sale.views import views
from entrypoint.messagebus import messagebus
from lib.err_msg import DATA_NOT_FOUND
from lib import err_msg
from lib.json_encoder import jsonable_encoder
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView


class SaleView(HTTPMethodView):
    async def get(self, request, id_):
        if id_:
            id = id_
            result = await views.get_sale_id(id, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        sale = await views.get_all_sales(request.app.ctx.db)
        result = jsonable_encoder(sale)
        return response.json(result)

    async def post(self, request, id_):
        data = abstract.AddSale(**request.json)
        try:
            await messagebus.handle(
                message=command.AddSale(**data.dict()),
                uow=unit_of_work.SaleSqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlSalesRepository,
                ),
            )
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)
        return response.json(data.dict(), status=201)

    async def put(self, request, id_):
        q_model = query.SaleQueryParamModel(id_=id_)
        sale_ = abstract.UpdateSale(id_=q_model.id_, **request.json)
        if q_model.id_:
            try:
                await messagebus.handle(
                    message=command.UpdateSale(**sale_.dict()),
                    uow=unit_of_work.SaleSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlSalesRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(sale_.dict())
        return response.json({"error": "url not found"}, status=400)


async def get_sale_by_reference_no(request):
    reference_no = request.args.get("reference_no")
    if reference_no:
        sale = await views.get_sale_by_reference_no(request.app.ctx.db, reference_no, )
        return response.json(jsonable_encoder(sale))

import json
import pandas as pd
from datetime import datetime
from product_components.returns.adapters import repository
from product_components.returns.domain import command
from product_components.returns.service_layer import abstract, unit_of_work, query
from product_components.returns.views import views
from entrypoint.messagebus import messagebus
from lib.err_msg import DATA_NOT_FOUND
from lib import err_msg
from lib.json_encoder import jsonable_encoder
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView
from asyncpg.exceptions import UniqueViolationError


class ReturnView(HTTPMethodView):
    async def get(self, request, id_):
        if id_:
            id = id_
            result = await views.get_return_id(id, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        return_ = await views.get_all_returns(request.app.ctx.db)
        result = jsonable_encoder(return_)
        return response.json(result)

    async def post(self, request, id_):
        data = abstract.AddReturn(**request.json)
        try:
            await messagebus.handle(
                message=command.AddReturn(**data.dict()),
                uow=unit_of_work.ReturnSqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlReturnsRepository,
                ),
            )

        except UniqueViolationError:
            return response.json({"error": "reference number must be unique "}, status=400)
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)

        return response.json(data.dict(), status=201)

    async def put(self, request, id_):
        q_model = query.ReturnQueryParamModel(id_=id_)
        return_ = abstract.UpdateReturn(id_=q_model.id_, **request.json)
        if q_model.id_:
            try:
                await messagebus.handle(
                    message=command.UpdateReturn(**return_.dict()),
                    uow=unit_of_work.ReturnSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlReturnsRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(return_.dict())
        return response.json({"error": "url not found"}, status=400)


async def get_return_by_reference_no(request):
    reference_no = request.args.get("reference_no")
    if reference_no:
        return_ = await views.get_return_by_reference_no(db=request.app.ctx.db, reference_no=reference_no)
        return response.json(jsonable_encoder(return_))


async def get_return_by_date(request):
    date = request.args.get("date")
    if date:
        return_ = await views.get_return_by_date(db=request.app.ctx.db, date=date)
        return response.json(jsonable_encoder(return_))

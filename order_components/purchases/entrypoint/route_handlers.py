import json
from order_components.purchases.adapters import repository
from order_components.purchases.domain import command
from order_components.purchases.service_layer import abstract, query
from order_components.purchases.service_layer import unit_of_work
from order_components.purchases.views import views
from entrypoint.messagebus import messagebus
from lib.err_msg import DATA_NOT_FOUND
from lib.json_encoder import jsonable_encoder
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView


class PurchaseView(HTTPMethodView):
    async def get(self, request, id_):
        if id_:
            id = id_
            result = await views.get_purchase_id(id, request.app.ctx.db)
            if result is None:
                return response.json({"error": DATA_NOT_FOUND}, status=404)
            return response.json(jsonable_encoder(result))
        purchase = await views.get_all_purchases(request.app.ctx.db)
        result = jsonable_encoder(purchase)
        return response.json(result)

    async def post(self, request, id_):
        data = abstract.AddPurchase(**request.json)
        try:
            await messagebus.handle(
                message=command.AddPurchase(**data.dict()),
                uow=unit_of_work.PurchaseSqlAlchemyUnitOfWork(
                    connection=request.app.ctx.db,
                    repository_class=repository.SqlPurchasesRepository,
                ),
            )
        except ValidationError as e:
            return response.json(json.loads(e.json()), status=400)
        return response.json(data.dict(), status=201)

    async def put(self, request, id_):
        q_model = query.PurchaseQueryParamModel(id_=id_)
        purchase_ = abstract.UpdatePurchase(id_=q_model.id_, **request.json)
        if q_model.id_:
            try:
                await messagebus.handle(
                    message=command.UpdatePurchase(**purchase_.dict()),
                    uow=unit_of_work.PurchaseSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.SqlPurchasesRepository,
                    ),
                )
            except ValidationError as e:
                return response.json(json.loads(e.json()), status=400)
            return response.json(purchase_.dict())
        return response.json({"error": "url not found"}, status=400)


async def get_purchase_by_purchase_number(request):
    purchase_no = request.args.get("purchase_no")
    if purchase_no:
        product = await views.get_purchase(request.app.ctx.db, purchase_no, )
        return response.json(jsonable_encoder(product))


async def get_purchase_by_date(request):
    date = request.args.get("date")
    if date:
        product = await views.get_purchase_by_date(date=date, db=request.app.ctx.db, )
        return response.json(jsonable_encoder(product))

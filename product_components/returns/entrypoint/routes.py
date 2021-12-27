from sanic import Blueprint
from product_components.returns.entrypoint import route_handlers

returns = Blueprint("returns", url_prefix="api/v1/")


returns.add_route(
    route_handlers.ReturnView.as_view(),
    "returns/<id_>",
)


returns.add_route(
    route_handlers.get_return_by_reference_no, "return/return_by_reference_no/", methods=["GET"]

)
returns.add_route(
    route_handlers.get_return_by_date, "return/date/", methods=["GET"]

)

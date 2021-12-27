from sanic import Blueprint
from product_components.sale.entrypoint import route_handlers
sale = Blueprint("sale", url_prefix="api/v1/")


sale.add_route(
    route_handlers.SaleView.as_view(),
    "sale/<id_>",
)


sale.add_route(
    route_handlers.get_sale_by_reference_no, "/sale_by_reference_no/<reference_no>", methods=["GET"]

)

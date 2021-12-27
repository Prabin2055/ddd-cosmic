from sanic import Blueprint
from order_components.purchases.entrypoint import route_handlers

purchase = Blueprint("purchase", url_prefix="api/v1/")


purchase.add_route(
    route_handlers.PurchaseView.as_view(),
    "purchase/<id_>",
)


# purchase.add_route(
#     route_handlers.get_purchase_by_purchase_number, "/purchase/<purchase_no>", methods=["GET"]
#
# )

purchase.add_route(
    route_handlers.get_purchase_by_date, "purchase_by_date/", methods=["GET"]

)
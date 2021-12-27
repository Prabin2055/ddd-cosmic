from sanic import Blueprint
from product_components.products.entrypoint import route_handlers


product = Blueprint("product", url_prefix="api/v1/")
batch = Blueprint("batch", url_prefix="api/v1/")


product.add_route(
    route_handlers.ProductView.as_view(),
    "product/<id_>",
)


batch.add_route(
    route_handlers.BatchView.as_view(),
    "batch/<ref>",
)

product.add_route(
    route_handlers.get_product_by_category, "/product_by_category/", methods=["GET"]

)
product.add_route(
    route_handlers.get_product_by_name, "/product_by_name/", methods=["GET"]

)
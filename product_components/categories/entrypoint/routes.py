from sanic import Blueprint
from product_components.categories.entrypoint import route_handlers
categories = Blueprint("categories", url_prefix="api/v1/")


categories.add_route(
    route_handlers.Categoriesiew.as_view(),
    "categories/<id_>",
)

categories.add_route(
    route_handlers.get_categories_by_category, "/categories_by_category/<categories>", methods=["GET"]

)

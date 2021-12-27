from sanic import Sanic

app = Sanic("Ecommerce", register=True)

from product_components.products.entrypoint.routes import product
from product_components.products.entrypoint.routes import batch
from product_components.categories.entrypoint.routes import categories
from product_components.returns.entrypoint.routes import returns
from product_components.sale.entrypoint.routes import sale
from order_components.purchases.entrypoint.routes import purchase
from user_components.user.entrypoints.routes import user
from entrypoint.bootstrap import init_database


async def create_app(settings):
    app.blueprint(purchase)
    app.blueprint(product)
    app.blueprint(categories)
    app.blueprint(returns)
    app.blueprint(sale)
    app.blueprint(batch)
    app.blueprint(user)
    db = init_database(settings)
    app.ctx.settings = settings
    app.ctx.db = db
    return app

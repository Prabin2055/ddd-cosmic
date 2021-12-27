from product_components.products.domain.command import AddProduct, UpdateProduct, AddBatch, UpdateBatch
from product_components.categories.domain.command import AddCategory, UpdateCategory
from order_components.purchases.domain.command import AddPurchase, UpdatePurchase
from product_components.returns.domain.command import AddReturn, UpdateReturn
from product_components.sale.domain.command import AddSale, UpdateSale
from product_components.products.service_layer.handlers import (
    add_product,
    update_product,
    add_batch,
    update_batch,
    batch_added,
    product_added,
)
from product_components.categories.service_layer.handlers import add_category, update_category
from order_components.purchases.service_layer.handlers import add_purchase, update_purchase, purchase_added
from product_components.returns.service_layer.handlers import add_return, update_return
from product_components.sale.service_layer.handlers import add_sale, update_sale
from order_components.purchases.domain.events import PurchaseAdded
from product_components.products.domain.events import BatchAdded, ProductAdded
from user_components.user.domain.command import AddUser
from user_components.user.service_layer.handlers import add_user

COMMAND_HANDLERS = {
    AddProduct: add_product,
    UpdateProduct: update_product,
    AddBatch: add_batch,
    UpdateBatch: update_batch,
    AddUser: add_user,
    AddCategory: add_category,
    UpdateCategory: update_category,
    AddPurchase: add_purchase,
    UpdatePurchase: update_purchase,
    AddSale: add_sale,
    UpdateSale: update_sale,
    AddReturn: add_return,
    UpdateReturn: update_return,

}

EVENT_HANDLERS = {
    BatchAdded: batch_added,
    ProductAdded: product_added,
    PurchaseAdded: purchase_added,

}

from product_components.products.domain import model
from product_components.products.domain import command


async def add_batch(cmd: command.AddBatch) -> model.Batch:
    return await model.batch_factory(
        sku=cmd.sku,
        purchased_quantity=cmd.purchased_quantity,
        eta=cmd.eta,
    )


async def update_batch(cmd: command.UpdateBatchCommand) -> model.Batch:
    if isinstance(cmd, command.UpdateBatch):
        return await cmd.batch.update(
            {
                "sku": cmd.sku,
                "purchased_quantity": cmd.purchased_quantity,
                "eta": cmd.eta
            }
        )


async def add_product(cmd: command.AddProduct) -> model.Product:
    return await model.product_factory(
        product_type=cmd.product_type,
        name=cmd.name,
        code=cmd.code,
        barcode_symbology=cmd.barcode_symbology,
        category=cmd.category,
        cost=cmd.cost,
        price=cmd.price,
        tax_method=cmd.tax_method,
        quantity=cmd.quantity,
        image=cmd.image,
        discription=cmd.discription,
    )


async def update_product(cmd: command.UpdateProductCommand) -> model.Product:
    if isinstance(cmd, command.UpdateProduct):
        return await cmd.product.update(
            {
                "product_type": cmd.product_type,
                "name": cmd.name,
                "code": cmd.code,
                "barcode_symbology": cmd.barcode_symbology,
                "categories": cmd.category,
                "cost": cmd.cost,
                "price": cmd.price,
                "tax_method": cmd.tax_method,
                "quantity": cmd.quantity,
                "image": cmd.image,
                "discription": cmd.discription,


            }
        )
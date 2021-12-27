from __future__ import annotations
from product_components.products.domain import command, handler
from product_components.products.domain import model
from product_components.products.service_layer import unit_of_work
from product_components.products.domain.events import BatchAdded, ProductAdded
from lib import event
from entrypoint.redis_config.redis_eventpublisher import publish


async def add_batch(
        validated_data: command.AddBatch,
        uow: unit_of_work.BatchSqlAlchemyUnitOfWork
):
    async with uow:
        batch = await handler.add_batch(validated_data)
        await uow.repository.add(batch)
        uow.events.add(BatchAdded(
            sku=validated_data.sku,
            purchased_quantity=validated_data.purchased_quantity,

        ))


async def batch_added(event: event.Event):
    await publish("batch_added", event)


async def update_batch(
    validated_data: command.UpdateBatch,
    uow: unit_of_work.BatchSqlAlchemyUnitOfWork,
):
    async with uow:
        batch = await uow.repository.get(validated_data.ref)
        batch = model.Batch(
            ref=batch["ref"],
            sku=batch["sku"],
            purchased_quantity=batch["purchased_quantity"],
            eta=batch["eta"],

        )
        cmd = command.UpdateBatch(
            batch=batch,
            ref=batch.ref,
            sku=validated_data.sku
            if validated_data.sku
            else batch.sku,
            purchased_quantity=validated_data.purchased_quantity
            if validated_data.purchased_quantity
            else batch.purchased_quantity,
            eta=validated_data.eta
            if validated_data.eta
            else batch.eta,
        )
        batch_ = await handler.update_batch(cmd=cmd)
        await uow.repository.update(batch_)


async def add_product(
        validated_data: command.AddProduct,
        uow: unit_of_work.ProductSqlAlchemyUnitOfWork
):
    async with uow:
        product = await handler.add_product(validated_data)
        await uow.repository.add(product)
        uow.events.add(ProductAdded(
            name=validated_data.name,
            quantity=validated_data.quantity,

        ))


async def product_added(event: event.Event):
    await publish("product_added", event)


async def update_product(
    validated_data: command.UpdateProduct,
    uow: unit_of_work.ProductSqlAlchemyUnitOfWork,
):
    async with uow:
        product = await uow.repository.get(validated_data.id_)
        product = model.Product(
            id_=product["id"],
            product_type=product["products_type"],
            name=product["name"],
            code=product["code"],
            barcode_symbology=product["barcodes_symbology"],
            category=product["categories"],
            cost=product["cost"],
            price=product["price"],
            tax_method=product["tax_method"],
            quantity=product["quantity"],
            image=product["image"],
            discription=product["discription"],

        )
        cmd = command.UpdateProduct(
            product=product,
            id_=product.id_,
            product_type=validated_data.product_type
            if validated_data.product_type
            else product.product_type,
            name=validated_data.name
            if validated_data.name
            else product.name,
            code=validated_data.code
            if validated_data.code
            else product.code,
            barcode_symbology=validated_data.barcode_symbology
            if validated_data.barcode_symbology
            else product.barcode_symbology,
            category=validated_data.category if validated_data.category else product.category,
            cost=validated_data.cost if validated_data.cost else product.cost,
            price=validated_data.price if validated_data.price else product.price,
            tax_method=validated_data.tax_method if validated_data.tax_method else product.tax_method,
            quantity=validated_data.quantity if validated_data.quantity else product.quantity,
            image=validated_data.image if validated_data.image else product.image,
            discription=validated_data.discription if validated_data.discription else product.discription,

        )
        product_ = await handler.update_product(cmd=cmd)
        await uow.repository.update(product_)

from __future__ import annotations
from product_components.sale.domain import command, handler
from product_components.sale.domain import model
from product_components.sale.service_layer import unit_of_work
from product_components.sale.domain.events import SalesAdded
from lib import event
from entrypoint.redis_config.redis_eventpublisher import publish


async def add_sale(
        validated_data: command.AddSale,
        uow: unit_of_work.SaleSqlAlchemyUnitOfWork
):
    async with uow:
        sale = await handler.add_sale(validated_data)
        await uow.repository.add(sale)


async def update_sale(
    validated_data: command.UpdateSale,
    uow: unit_of_work.SaleSqlAlchemyUnitOfWork,
):
    async with uow:
        sale = await uow.repository.get(validated_data.id_)
        sale = model.Sale(
            id_=sale["id"],
            date=sale["date"],
            reference_no=sale["reference_no"],
            biller=sale["sale_biller"],
            customer=sale["customer"],
            order_tax=sale["tax"],
            order_discount=sale["order_discount"],
            shipping=sale["shipping"],
            attach_document=sale["attach_document"],
            sales_status=sale["sale_status"],
            payment_status=sale["payments_status"],
            sales_note=sale["sales_note"],

        )
        cmd = command.UpdateSale(
            sale=sale,
            id_=sale.id_,
            date=validated_data.date
            if validated_data.date
            else sale.date,
            reference_no=validated_data.reference_no
            if validated_data.reference_no
            else sale.reference_no,
            biller=validated_data.biller
            if validated_data.biller
            else sale.biller,
            customer=validated_data.customer
            if validated_data.customer
            else sale.customer,
            order_tax=validated_data.order_tax if validated_data.order_tax else sale.order_tax,
            order_discount=validated_data.order_discount if validated_data.order_discount else sale.order_discount,
            shipping=validated_data.shipping if validated_data.shipping else sale.shipping,
            attach_document=validated_data.attach_document if validated_data.attach_document else sale.attach_document,
            sales_status=validated_data.sales_status if validated_data.sales_status else sale.sales_status,
            payment_status=validated_data.payment_status if validated_data.payment_status else sale.payment_status,
            sales_note=validated_data.sales_note if validated_data.sales_note else sale.sales_note,

        )
        sale_ = await handler.update_sale(cmd=cmd)
        await uow.repository.update(sale_)

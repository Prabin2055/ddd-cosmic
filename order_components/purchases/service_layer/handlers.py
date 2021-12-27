from __future__ import annotations
from order_components.purchases.domain import command, handler, model
from order_components.purchases.service_layer import unit_of_work
from order_components.purchases.domain.events import PurchaseAdded
from lib import event
from entrypoint.redis_config.redis_eventpublisher import publish


async def add_purchase(
        validated_data: command.AddPurchase,
        uow: unit_of_work.PurchaseSqlAlchemyUnitOfWork
):
    async with uow:
        purchase = await handler.add_purchase(validated_data)
        await uow.repository.add(purchase)
        uow.events.add(PurchaseAdded(
            purchase_no=validated_data.purchase_no,
            date=validated_data.date,

        ))


async def purchase_added(event: event.Event):
    await publish("purchase_added", event)


async def update_purchase(
    validated_data: command.UpdatePurchase,
    uow: unit_of_work.PurchaseSqlAlchemyUnitOfWork,
):
    async with uow:
        purchase = await uow.repository.get(validated_data.id_)
        purchase = model.Purchase(
            id_=purchase["id"],
            date=purchase["date"],
            purchase_no=purchase["purchase_no"],
            supplier=purchase["supplier"],
            received=purchase["received"],
            order_tax=purchase["order_taxes"],
            discount=purchase["discount"],
            shipping=purchase["shipping"],
            payment=purchase["payment"],
            note=purchase["note"],
        )
        cmd = command.UpdatePurchase(
            purchase=purchase,
            id_=purchase.id_,
            date=validated_data.date
            if validated_data.date
            else purchase.date,
            purchase_no=validated_data.purchase_no
            if validated_data.purchase_no
            else purchase.purchase_no,
            supplier=validated_data.supplier
            if validated_data.supplier
            else purchase.supplier,
            received=validated_data.received
            if validated_data.received
            else purchase.received,
            order_tax=validated_data.order_tax if validated_data.order_tax else purchase.order_tax,
            discount=validated_data.discount if validated_data.discount else purchase.discount,
            shipping=validated_data.shipping if validated_data.shipping else purchase.shipping,
            payment=validated_data.payment if validated_data.payment else purchase.payment,
            note=validated_data.note if validated_data.note else purchase.note,
        )
        purchase_ = await handler.update_purchase(cmd=cmd)
        await uow.repository.update(purchase_)

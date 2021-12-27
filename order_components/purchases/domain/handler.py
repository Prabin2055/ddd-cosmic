from order_components.purchases.domain import command, model


async def add_purchase(cmd: command.AddPurchase) -> model.Purchase:
    return await model.purchase_factory(
        date=cmd.date,
        purchase_no=cmd.purchase_no,
        supplier=cmd.supplier,
        received=cmd.received,
        order_tax=cmd.order_tax,
        discount=cmd.discount,
        shipping=cmd.shipping,
        payment=cmd.payment,
        note=cmd.note,
    )


async def update_purchase(cmd: command.UpdatePurchaseCommand) -> model.Purchase:
    if isinstance(cmd, command.UpdatePurchase):
        return await cmd.purchase.update(
            {
                "date": cmd.date,
                "purchase_no": cmd.purchase_no,
                "supplier": cmd.supplier,
                "received": cmd.received,
                "order_tax": cmd.order_tax,
                "discount": cmd.discount,
                "shipping": cmd.shipping,
                "payment": cmd.payment,
                "note": cmd.note,
            }
        )

from product_components.returns.domain import model
from product_components.returns.domain import command


async def add_return(cmd: command.AddReturn) -> model.Return:
    return await model.return_factory(
        date=cmd.date,
        reference_no=cmd.reference_no,
        biller=cmd.biller,
        customer=cmd.customer,
        order_tax=cmd.order_tax,
        order_discount=cmd.order_discount,
        shipping=cmd.shipping,
        attach_document=cmd.attach_document,
        return_note=cmd.return_note,
    )


async def update_return(cmd: command.UpdateReturnCommand) -> model.Return:
    if isinstance(cmd, command.UpdateReturn):
        return await cmd.returns.update(
            {
                "date": cmd.date,
                "reference_no": cmd.reference_no,
                "biller": cmd.biller,
                "customer": cmd.customer,
                "order_tax": cmd.order_tax,
                "order_discount": cmd.order_discount,
                "shipping": cmd.shipping,
                "attach_document": cmd.attach_document,
                "return_note": cmd.return_note,
            }
        )

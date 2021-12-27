from product_components.sale.domain import model
from product_components.sale.domain import command


async def add_sale(cmd: command.AddSale) -> model.Sale:
    return await model.sale_factory(
        date=cmd.date,
        reference_no=cmd.reference_no,
        biller=cmd.biller,
        customer=cmd.customer,
        order_tax=cmd.order_tax,
        order_discount=cmd.order_discount,
        shipping=cmd.shipping,
        attach_document=cmd.attach_document,
        sales_status=cmd.sales_status,
        payment_status=cmd.payment_status,
        sales_note=cmd.sales_note,
    )


async def update_sale(cmd: command.UpdateSaleCommand) -> model.Sale:
    if isinstance(cmd, command.UpdateSale):
        return await cmd.sale.update(
            {
                "date": cmd.date,
                "reference_no": cmd.reference_no,
                "biller": cmd.biller,
                "customer": cmd.customer,
                "order_tax": cmd.order_tax,
                "order_discount": cmd.order_discount,
                "shipping": cmd.shipping,
                "attach_document": cmd.attach_document,
                "sales_status": cmd.sales_status,
                "payment_status": cmd.payment_status,
                "sales_note": cmd.sales_note,
            }
        )

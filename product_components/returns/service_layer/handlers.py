from __future__ import annotations
from product_components.returns.domain import command, handler
from product_components.returns.domain import model
from product_components.returns.service_layer import unit_of_work
from product_components.returns.domain.events import ReturnAdded
from lib import event
from entrypoint.redis_config.redis_eventpublisher import publish


async def add_return(
        validated_data: command.AddReturn,
        uow: unit_of_work.ReturnSqlAlchemyUnitOfWork
):
    async with uow:
        return_ = await handler.add_return(validated_data)
        await uow.repository.add(return_)


async def update_return(
    validated_data: command.UpdateReturn,
    uow: unit_of_work.ReturnSqlAlchemyUnitOfWork,
):
    async with uow:
        return_ = await uow.repository.get(validated_data.id_)
        return_ = model.Return(
            id_=return_["id"],
            date=return_["date"],
            reference_no=return_["reference_no"],
            biller=return_["return_biller"],
            customer=return_["customer"],
            order_tax=return_["order_tax"],
            order_discount=return_["order_discount"],
            shipping=return_["shipping"],
            attach_document=return_["attach_document"],
            return_note=return_["return_note"],

        )
        cmd = command.UpdateReturn(
            returns=return_,
            id_=return_.id_,
            date=validated_data.date
            if validated_data.date
            else return_.date,
            reference_no=validated_data.reference_no
            if validated_data.reference_no
            else return_.reference_no,
            biller=validated_data.biller
            if validated_data.biller
            else return_.biller,
            customer=validated_data.customer
            if validated_data.customer
            else return_.customer,
            order_tax=validated_data.order_tax if validated_data.order_tax else return_.order_tax,
            order_discount=validated_data.order_discount if validated_data.order_discount else return_.order_discount,
            shipping=validated_data.shipping if validated_data.shipping else return_.shipping,
            attach_document=validated_data.attach_document if validated_data.attach_document else return_.attach_document,
            return_note=validated_data.return_note if validated_data.return_note else return_.return_note,

        )
        returns_ = await handler.update_return(cmd=cmd)
        await uow.repository.update(returns_)

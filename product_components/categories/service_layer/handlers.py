from __future__ import annotations
from product_components.categories.domain import command, handler
from product_components.categories.domain import model
from product_components.categories.service_layer import unit_of_work
from product_components.categories.domain.events import CategoryAdded
from lib import event
from entrypoint.redis_config.redis_eventpublisher import publish


async def add_category(
        validated_data: command.AddCategory,
        uow: unit_of_work.CategorySqlAlchemyUnitOfWork
):
    async with uow:
        batch = await handler.add_category(validated_data)
        await uow.repository.add(batch)
        uow.events.add(CategoryAdded(
            category=validated_data.category,
            product_name=validated_data.product_name,

        ))


async def category_added(event: event.Event):
    await publish("category_added", event)


async def update_category(
    validated_data: command.UpdateCategory,
    uow: unit_of_work.CategorySqlAlchemyUnitOfWork,
):
    async with uow:
        category_ = await uow.repository.get(validated_data.id_)
        category_ = model.Category(
            id_=category_["id"],
            image=category_["image"],
            product_name=category_["product_name"],
            category=category_["category"],
            code=category_["code"],

        )
        cmd = command.UpdateCategory(
            categories=category_,
            id_=category_.id_,
            image=validated_data.image
            if validated_data.image
            else category_.image,
            product_name=validated_data.product_name
            if validated_data.product_name
            else category_.product_name,
            category=validated_data.category
            if validated_data.category else category_.category,
            code=validated_data.code
            if validated_data.code
            else category_.code,
        )
        category_ = await handler.update_category(cmd=cmd)
        await uow.repository.update(category_)

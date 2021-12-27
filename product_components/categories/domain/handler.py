from product_components.categories.domain import model
from product_components.categories.domain import command


async def add_category(cmd: command.AddCategory) -> model.Category:
    return await model.category_factory(
        image=cmd.image,
        product_name=cmd.product_name,
        category=cmd.category,
        code=cmd.code,

    )


async def update_category(cmd: command.UpdateCategoryCommand) -> model.Category:
    if isinstance(cmd, command.UpdateCategory):
        return await cmd.categories.update(
            {
                "image": cmd.image,
                "product_name": cmd.product_name,
                "category": cmd.category,
                "code": cmd.code,



            }
        )
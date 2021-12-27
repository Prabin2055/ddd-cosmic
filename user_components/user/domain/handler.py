from user_components.user.domain import command, model


async def add_user(cmd: command.AddUser):
    return await model.user_factory(
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        user_name=cmd.user_name,
        password=cmd.password,
        phone_number=cmd.phone_number,
        is_admin=cmd.is_admin,
        is_client=cmd.is_client,
    )


async def change_password(cmd: command.ChangeUserPassword) -> model.User:
    if isinstance(cmd, command.ChangePassword):
        return await cmd.user.update(
            {
                "password": cmd.new_password,
            }
        )
    if isinstance(cmd, command.ForgetPasswordUpdate):
        return await cmd.user.update({"password": cmd.password_new})

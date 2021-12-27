from lib.command import Command
from user_components.user.domain import model


class AddUser(Command):
    first_name: str
    last_name: str
    email: str
    user_name: str
    password: str
    phone_number: str
    is_admin: bool
    is_client: bool


class ActivateUser(Command):
    email: str
    otp: str


class LoginUser(Command):
    email: str
    password: str


class ChangeUserPassword(Command):
    user: model.User = None


class ChangePassword(ChangeUserPassword):
    email: str
    password: str
    new_password: str
    new_password_re: str


class ForgetPassword(ChangeUserPassword):
    email: str


class ForgetPasswordUpdate(ChangeUserPassword):
    email: str
    otp: str
    password_new: str
    password_new_re: str

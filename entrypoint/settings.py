import os
import typing
from pydantic import PostgresDsn
from dotenv import load_dotenv, find_dotenv
from lib.settings import AbstractSettings


load_dotenv(find_dotenv())
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_HOST = os.environ.get("HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "postgres")


class Settings(AbstractSettings):
    pg_dsn: PostgresDsn
    redis_settings: typing.Dict
    components: typing.List[str]
    alembic_config: str
    secret_key: str


def settings_factory() -> Settings:
    return Settings(
        pg_dsn=typing.cast(
            PostgresDsn,
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        ),
        redis_settings={"host": "0.0.0.0", "port": "6379"},
        components=[
            "product_components.products",
            "product_components.categories",
            "order_components.purchases",
        ],
        alembic_config="alembic.ini",
        secret_key="2#$%^&SDFGHJKLOIUYTR@#$%^&*987654#$%^&*kJHGF3$%^&*"
        "(kertyujnb345678$%^&*NBVCVBNJHGF$%^&*(JH",

    )

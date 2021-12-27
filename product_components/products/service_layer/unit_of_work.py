import typing
from lib import unit_of_work
from lib.db_connection import DbConnection
from lib import repository


class ProductSqlAlchemyUnitOfWork(unit_of_work.SqlAlchemyUnitOfWork):
    def __init__(
            self,
            connection: DbConnection,
            repository_class: typing.Type[repository.SqlAlchemyRepository],
    ):
        super().__init__(connection, repository_class)


class BatchSqlAlchemyUnitOfWork(unit_of_work.SqlAlchemyUnitOfWork):
    def __init__(
            self,
            connection: DbConnection,
            repository_class: typing.Type[repository.SqlAlchemyRepository],
    ):
        super().__init__(connection, repository_class)

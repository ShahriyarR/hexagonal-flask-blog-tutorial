from sqlite3 import Connection
from src.domain.ports.repository import RepositoryInterface
from typing import Callable, Any


class UserRepository(RepositoryInterface):

    def __init__(self, db_conn: Callable[[], Connection]) -> None:
        self.db_conn = db_conn()

    def execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        result = self.db_conn.execute(query, data)
        if commit:
            self.commit()
        return result

    def commit(self) -> None:
        self.db_conn.commit()

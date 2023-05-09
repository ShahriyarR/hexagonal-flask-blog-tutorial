from sqlite3 import Connection
from typing import Any, Callable

from blog.domain.ports.repositories.repository import RepositoryInterface


class UserRepository(RepositoryInterface):
    def __init__(self, db_conn: Callable[[], Connection]) -> None:
        self.db_conn = db_conn()

    def _execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        result = self.db_conn.execute(query, data)
        if commit:
            self.commit()
        return result

    def _commit(self) -> None:
        self.db_conn.commit()

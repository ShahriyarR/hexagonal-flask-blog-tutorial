from sqlite3 import Connection
from typing import Any, Callable

from src.blog.domain.ports.repositories.repository import RepositoryInterface


class PostRepository(RepositoryInterface):
    def __init__(self, db_conn: Callable[[], Connection]) -> None:
        self.db_conn = db_conn()

    def execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        result = self.db_conn.execute(query, data)
        if commit:
            self.commit()
        return result

    def commit(self) -> None:
        self.db_conn.commit()

from abc import ABC, abstractmethod
from sqlite3 import Connection
from typing import Any, Callable


class RepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, db_conn: Callable[[], Connection]) -> None:
        self.db = db_conn

    def execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        return self._execute(query, data, commit)

    def commit(self) -> None:
        return self._commit()

    @abstractmethod
    def _execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        raise NotImplementedError

    @abstractmethod
    def _commit(self) -> None:
        raise NotImplementedError

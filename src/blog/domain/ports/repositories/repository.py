from abc import ABC, abstractmethod
from sqlite3 import Connection
from typing import Any, Callable


class RepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, db_conn: Callable[[], Connection]) -> None:
        self.db = db_conn

    @abstractmethod
    def execute(self, query: str, data: tuple[Any, ...], commit: bool = False) -> Any:
        ...

    @abstractmethod
    def commit(self) -> None:
        ...

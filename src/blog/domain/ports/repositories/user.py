from abc import ABC, abstractmethod
from typing import Any, Optional

from src.blog.domain.model import model


class UserRepositoryInterface(ABC):
    def add(self, user: model.User) -> None:
        self._add(user)

    def get_by_uuid(self, uuid: str) -> Optional[model.User]:
        return self._get_by_uuid(uuid)

    def get_user_by_user_name(self, user_name: str) -> Optional[model.User]:
        return self._get_user_by_user_name(user_name)

    def get_all(self) -> list[model.User]:
        return self._get_all()

    def execute(self, query: str, data: tuple[Any, ...]) -> Any:
        return self._execute(query, data)

    @abstractmethod
    def _add(self, post: model.User) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get_by_uuid(self, uuid: str) -> model.User:
        raise NotImplementedError

    @abstractmethod
    def _get_user_by_user_name(self, user_name: str) -> Optional[model.User]:
        raise NotImplementedError

    @abstractmethod
    def _get_all(self) -> list[model.User]:
        raise NotImplementedError

    @abstractmethod
    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        raise NotImplementedError

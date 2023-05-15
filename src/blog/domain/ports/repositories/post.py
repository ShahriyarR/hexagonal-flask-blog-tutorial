from abc import ABC, abstractmethod
from typing import Any, Optional

from src.blog.domain.model import model


class PostRepositoryInterface(ABC):
    def add(self, post: model.Post) -> None:
        self._add(post)

    def get_by_uuid(self, uuid: str) -> model.Post:
        return self._get_by_uuid(uuid)

    def get_all(self) -> Optional[list[model.Post]]:
        return self._get_all()

    def update_by_uuid(self, uuid: str, title: str, body: str) -> model.Post:
        return self._update_by_uuid(uuid, title, body)

    def delete(self, uuid: str) -> None:
        return self._delete(uuid)

    def execute(self, query: str, data: tuple[Any, ...]) -> Any:
        return self._execute(query, data)

    @abstractmethod
    def _add(self, post: model.Post) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get_by_uuid(self, uuid: str) -> model.Post:
        raise NotImplementedError

    @abstractmethod
    def _get_all(self) -> Optional[list[model.Post]]:
        raise NotImplementedError

    @abstractmethod
    def _update_by_uuid(self, uuid: str, title: str, body: str) -> model.Post:
        raise NotImplementedError

    @abstractmethod
    def _delete(self, uuid: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        raise NotImplementedError

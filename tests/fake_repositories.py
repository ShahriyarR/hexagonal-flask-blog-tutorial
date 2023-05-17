import random
from typing import Any

from blog.domain.model import model
from blog.domain.ports.repositories.post import PostRepositoryInterface
from blog.domain.ports.repositories.user import UserRepositoryInterface


class FakeUserRepository(UserRepositoryInterface):
    def __init__(self):
        super().__init__()
        self.database = {}

    def _add(self, user: model.User):
        id_ = random.randint(10, 100)
        self.database[id_] = user

    def _get_by_uuid(self, uuid: str) -> model.User:
        for val in self.database.values():
            if val.uuid == uuid:
                return val

    def _get_user_by_user_name(self, user_name: str) -> model.User:
        for val in self.database.values():
            if val.user_name == user_name:
                return val

    def _get_all(self) -> list[model.User]:
        return self.database

    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        # We do not need the actual execute here
        pass


class FakePostRepository(PostRepositoryInterface):
    def __init__(self):
        super().__init__()
        self.database = {}

    def _add(self, post: model.Post):
        id_ = random.randint(10, 100)
        self.database[id_] = post

    def _get_by_uuid(self, uuid: str) -> model.Post:
        for val in self.database.values():
            if val.uuid == uuid:
                return val

    def _get_all(self) -> list[model.Post]:
        return self.database

    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        # We do not need the actual execute here
        pass

    def _update_by_uuid(self, uuid: str, title: str, body: str) -> model.Post:
        for val in self.database.values():
            if val.uuid == uuid:
                val.title = title
                val.body = body
                return val

    def _delete(self, uuid: str) -> None:
        found_key = None
        for key, val in self.database.items():
            if val.uuid == uuid:
                found_key = key

        del self.database[found_key]

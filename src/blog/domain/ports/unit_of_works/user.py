from abc import ABC, abstractmethod

from blog.domain.ports.repositories.user import UserRepositoryInterface


class UserUnitOfWorkInterface(ABC):
    user: UserRepositoryInterface

    def __enter__(self) -> "UserUnitOfWorkInterface":
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.rollback()

    def commit(self):
        self._commit()

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

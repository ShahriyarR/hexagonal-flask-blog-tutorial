from abc import ABC, abstractmethod
from typing import Optional

from blog.domain.model.model import User
from blog.domain.model.schemas import RegisterUserInputDto
from blog.domain.ports.unit_of_works.user import UserUnitOfWorkInterface


class UserServiceInterface(ABC):
    @abstractmethod
    def __init__(self, uow: UserUnitOfWorkInterface) -> None:
        raise NotImplementedError

    def create(self, user: RegisterUserInputDto) -> User:
        return self._create(user)

    def get_user_by_user_name(self, user_name: str) -> Optional[User]:
        return self._get_user_by_user_name(user_name)

    def get_user_by_id(self, uuid: str) -> Optional[User]:
        return self._get_user_by_uuid(uuid)

    @abstractmethod
    def _create(self, user: RegisterUserInputDto) -> User:
        raise NotImplementedError

    @abstractmethod
    def _get_user_by_user_name(self, user_name: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def _get_user_by_uuid(self, uuid: str) -> Optional[User]:
        raise NotImplementedError

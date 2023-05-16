from typing import Optional

from blog.domain.model.model import User, user_factory
from blog.domain.model.schemas import RegisterUserInputDto
from blog.domain.ports.services.user import UserServiceInterface
from blog.domain.ports.unit_of_works.user import UserUnitOfWorkInterface


class UserService(UserServiceInterface):
    def __init__(self, uow: UserUnitOfWorkInterface) -> None:
        self.uow = uow

    def _create(self, user: RegisterUserInputDto) -> User:
        user = user_factory(
            uuid=user.uuid, user_name=user.user_name, password=user.password
        )
        with self.uow:
            self.uow.user.add(user)
            self.uow.commit()
            return user

    def _get_user_by_user_name(self, user_name: str) -> Optional[User]:
        with self.uow:
            user = self.uow.user.get_user_by_user_name(user_name)
        return user

    def _get_user_by_uuid(self, uuid: str) -> Optional[User]:
        with self.uow:
            return self.uow.user.get_by_uuid(uuid)

from typing import Optional, Any
from . import RegisterUserInputDto
from ..model import user_factory, User
from .repository import RepositoryInterface


class UserDBOperationError(Exception):
    ...


class UserService:

    def __init__(self, user_repo: RepositoryInterface) -> None:
        self.user_repo = user_repo

    def create(self, user: RegisterUserInputDto) -> User:
        user = user_factory(user_name=user.user_name, password=user.password)
        data = (user.id_, user.user_name, user.password)
        query = "INSERT INTO user (id_, username, password) VALUES (?, ?, ?)"
        try:
            self.user_repo.execute(query, data, commit=True)
        except Exception as err:
            raise UserDBOperationError(err) from err
        return user

    def get_user_by_user_name(self, user_name: str) -> Optional[tuple[Any, ...]]:
        data = (user_name, )
        query = "SELECT * FROM user WHERE username = ?"
        try:
            return self.user_repo.execute(query, data).fetchone()
        except Exception as err:
            raise UserDBOperationError() from err

    def get_user_by_id(self, id_: int) -> Optional[tuple[Any, ...]]:
        data = (id_,)
        query = "SELECT * FROM user WHERE id = ?"
        try:
            return self.user_repo.execute(query, data).fetchone()
        except Exception as err:
            raise UserDBOperationError() from err


from typing import Any, Optional

from werkzeug.security import generate_password_hash

from blog.domain.model import model
from blog.domain.ports.repositories.exceptions import UserDBOperationError
from blog.domain.ports.repositories.user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        return self.session.execute(query, data)

    def _add(self, user: model.User) -> None:
        data = (user.uuid, user.user_name, user.password)
        query = "INSERT INTO user (uuid, username, password) VALUES (?, ?, ?)"
        try:
            self.execute(query, data)
        except Exception as err:
            raise UserDBOperationError(err) from err

    def _get_user_by_user_name(self, user_name: str) -> Optional[model.User]:
        data = (user_name,)
        query = "SELECT * FROM user WHERE username = ?"
        try:
            return self.execute(query, data).fetchone()
        except Exception as err:
            raise UserDBOperationError() from err

    def _get_by_uuid(self, uuid: str) -> Optional[model.User]:
        data = (uuid,)
        query = "SELECT * FROM user WHERE uuid = ?"
        try:
            return self.execute(query, data).fetchone()
        except Exception as err:
            raise UserDBOperationError() from err

    def _get_all(self) -> list[model.User]:
        data = ()
        query = "SELECT * FROM user"
        try:
            return self.execute(query, data).fetchall()
        except Exception as err:
            raise UserDBOperationError() from err

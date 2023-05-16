from typing import Any, Callable

from blog.adapters.repositories.user import UserRepository
from blog.domain.ports.unit_of_works.user import UserUnitOfWorkInterface


class UserUnitOfWork(UserUnitOfWorkInterface):
    def __init__(self, session_factory: Callable[[], Any]):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        # self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

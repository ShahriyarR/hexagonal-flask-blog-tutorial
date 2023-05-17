from blog.domain.ports.unit_of_works.user import UserUnitOfWorkInterface
from tests.fake_repositories import FakeUserRepository


class FakeUserUnitOfWork(UserUnitOfWorkInterface):
    def __init__(self):
        self.committed = False

    def __enter__(self):
        self.user = FakeUserRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.committed = True

    def rollback(self):
        # because we don't care
        pass

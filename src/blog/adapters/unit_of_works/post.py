from typing import Any, Callable

from blog.adapters.repositories.post import PostRepository
from blog.domain.ports.unit_of_works.post import PostUnitOfWorkInterface


class PostUnitOfWork(PostUnitOfWorkInterface):
    def __init__(self, session_factory: Callable[[], Any]):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.post = PostRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        # self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

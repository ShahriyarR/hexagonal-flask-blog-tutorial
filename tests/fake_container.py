import sqlite3
from typing import Callable

from dependency_injector import containers, providers

from blog.adapters.services.post import PostService
from blog.adapters.services.user import UserService
from blog.adapters.unit_of_works.post import PostUnitOfWork
from blog.adapters.unit_of_works.user import UserUnitOfWork
from blog.configurator.config import get_db


def _get_db() -> Callable[[], sqlite3.Connection]:
    db = sqlite3.connect(
        "hexagonal_test.db",
        detect_types=sqlite3.PARSE_DECLTYPES,
        check_same_thread=False,
    )

    db.row_factory = sqlite3.Row
    # Solution for -> TypeError: cannot pickle 'sqlite3.Connection' object
    return lambda: db


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["blog.adapters.entrypoints.app.blueprints"]
    )
    db_connection = _get_db()

    post_uow = providers.Singleton(PostUnitOfWork, session_factory=db_connection)
    post_service = providers.Factory(PostService, uow=post_uow)

    user_uow = providers.Singleton(UserUnitOfWork, session_factory=db_connection)
    user_service = providers.Factory(UserService, uow=user_uow)

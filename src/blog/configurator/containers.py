from dependency_injector import containers, providers

from blog.adapters.services.post import PostService
from blog.adapters.services.user import UserService
from blog.adapters.unit_of_works.post import PostUnitOfWork
from blog.adapters.unit_of_works.user import UserUnitOfWork
from blog.configurator.config import get_db


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["blog.adapters.entrypoints.app.blueprints"]
    )
    db_connection = get_db()

    post_uow = providers.Singleton(PostUnitOfWork, session_factory=db_connection)
    post_service = providers.Factory(PostService, uow=post_uow)

    user_uow = providers.Singleton(UserUnitOfWork, session_factory=db_connection)
    user_service = providers.Factory(UserService, uow=user_uow)

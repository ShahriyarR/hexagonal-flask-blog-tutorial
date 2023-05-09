from dependency_injector import containers, providers

from blog.adapters.repositories.post import PostRepository
from blog.adapters.repositories.user import UserRepository
from blog.adapters.services.post import PostService
from blog.adapters.services.user import UserService
from blog.configurator.config import get_db


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["blog.adapters.entrypoints.app.blueprints"]
    )
    db_connection = get_db()

    post_repository = providers.Singleton(PostRepository, db_conn=db_connection)

    post_service = providers.Factory(PostService, post_repo=post_repository)

    user_repository = providers.Singleton(UserRepository, db_conn=db_connection)

    user_service = providers.Factory(UserService, user_repo=user_repository)

from dependency_injector import containers, providers

from src.blog.adapters.repositories.user import UserRepository
from src.blog.adapters.services.user import UserService


class UserContainer(containers.DeclarativeContainer):
    db_conn = providers.Dependency()

    user_repository = providers.Singleton(UserRepository, db_conn=db_conn)

    user_service = providers.Factory(UserService, user_repo=user_repository)

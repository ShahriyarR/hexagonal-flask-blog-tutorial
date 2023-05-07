from dependency_injector import containers, providers
from src.blog.adapters.repositories.user_repository import UserRepository
from src.blog.domain.ports.services.user_service import UserService


class UserContainer(containers.DeclarativeContainer):

    db_conn = providers.Dependency()

    user_repository = providers.Singleton(
        UserRepository,
        db_conn=db_conn
    )

    user_service = providers.Factory(
        UserService,
        user_repo=user_repository
    )

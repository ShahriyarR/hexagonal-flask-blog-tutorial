from dependency_injector import containers, providers

from src.blog.adapters.repositories.post_repository import PostRepository
from src.blog.domain.ports.services.post_service import PostService


class PostContainer(containers.DeclarativeContainer):
    db_conn = providers.Dependency()

    post_repository = providers.Singleton(PostRepository, db_conn=db_conn)

    post_service = providers.Factory(PostService, post_repo=post_repository)

from dependency_injector import containers, providers

from src.main.config import get_db
from src.main.user_containers import UserContainer
from src.main.post_containers import PostContainer


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.adapters.app.blueprints"])
    db_connection = get_db()

    user_package = providers.Container(
        UserContainer,
        db_conn=db_connection
    )

    blog_package = providers.Container(
        PostContainer,
        db_conn=db_connection
    )

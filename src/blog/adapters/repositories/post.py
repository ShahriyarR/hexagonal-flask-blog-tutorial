from typing import Any, Optional

from blog.domain.model import model
from blog.domain.ports.repositories.exceptions import BlogDBOperationError
from blog.domain.ports.repositories.post import PostRepositoryInterface


class PostRepository(PostRepositoryInterface):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, post: model.Post) -> None:
        data = (post.uuid, post.title, post.body, post.author_id, post.created)
        query = ("INSERT INTO post (uuid, title, body, author_id, created)"
                 " VALUES (?, ?, ?, ?, ?)")
        try:
            self.execute(query, data)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def _update_by_uuid(self, uuid: str, title: str, body: str) -> model.Post:
        data = (title, body, uuid)
        query = """UPDATE post SET title = ?, body = ? WHERE uuid = ?"""
        try:
            return self.execute(query, data)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def _delete(self, uuid: str) -> None:
        data = (uuid,)
        query = "DELETE FROM post WHERE uuid = ?"
        try:
            self.execute(query, data)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def _get_all(self) -> Optional[list[model.Post]]:
        data = ()
        query = """SELECT p.id, p.uuid, title, body, created, author_id, username
                 FROM post p JOIN user u ON p.author_id = u.uuid
                 ORDER BY created DESC"""
        try:
            return self.execute(query, data).fetchall()
        except Exception as err:
            raise BlogDBOperationError() from err

    def _get_by_uuid(self, uuid: str) -> model.Post:
        data = (uuid,)
        query = """SELECT p.id, p.uuid, title, body, created, author_id, username
                     FROM post p JOIN user u ON p.author_id = u.uuid
                    WHERE p.uuid = ?"""

        return self.execute(query, data).fetchone()

    def _execute(self, query: str, data: tuple[Any, ...]) -> Any:
        return self.session.execute(query, data)

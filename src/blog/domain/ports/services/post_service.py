from typing import Any, Optional

from flask import abort, g

from src.blog.domain.model.post import Post, post_factory
from src.blog.domain.ports import (
    CreatePostInputDto,
    DeletePostInputDto,
    UpdatePostInputDto,
)
from src.blog.domain.ports.repositories.repository import RepositoryInterface


class BlogDBOperationError(Exception):
    ...


class PostService:
    def __init__(self, post_repo: RepositoryInterface) -> None:
        self.post_repo = post_repo

    def create(self, post: CreatePostInputDto) -> Optional[Post]:
        _post = post_factory(author_id=post.author_id, title=post.title, body=post.body)
        data = (_post.id_, _post.title, _post.body, _post.author_id)
        query = "INSERT INTO post (id_, title, body, author_id) VALUES (?, ?, ?, ?)"
        try:
            return self.post_repo.execute(query, data, commit=True)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def update(self, post: UpdatePostInputDto):
        data = (post.title, post.body, post.id)
        query = """UPDATE post SET title = ?, body = ? WHERE id = ?"""
        try:
            return self.post_repo.execute(query, data, commit=True)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def delete(self, post: DeletePostInputDto):
        data = (post.id,)
        query = "DELETE FROM post WHERE id = ?"
        try:
            return self.post_repo.execute(query, data, commit=True)
        except Exception as err:
            raise BlogDBOperationError(err) from err

    def get_all_blogs(self) -> Optional[list[Any]]:
        data = ()
        query = """SELECT p.id, title, body, created, author_id, username
         FROM post p JOIN user u ON p.author_id = u.id
         ORDER BY created DESC"""
        try:
            return self.post_repo.execute(query, data).fetchall()
        except Exception as err:
            raise BlogDBOperationError() from err

    def get_post_by_id(self, _id: int, check_author: bool = True) -> Post:
        data = (_id,)
        query = """SELECT p.id, title, body, created, author_id, username
             FROM post p JOIN user u ON p.author_id = u.id
            WHERE p.id = ?"""

        post = self.post_repo.execute(query, data).fetchone()

        if post is None:
            abort(404, f"Post id {id} doesn't exist.")

        if check_author and post["author_id"] != g.user["id"]:
            abort(403)

        return post

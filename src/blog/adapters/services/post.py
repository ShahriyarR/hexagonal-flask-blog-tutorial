from typing import Optional

from flask import abort, g

from blog.domain.model import model
from blog.domain.model.model import Post, post_factory
from blog.domain.model.schemas import (
    CreatePostInputDto,
    DeletePostInputDto,
    UpdatePostInputDto,
)
from blog.domain.ports.services.post import PostServiceInterface
from blog.domain.ports.unit_of_works.post import PostUnitOfWorkInterface


class PostService(PostServiceInterface):
    def __init__(self, uow: PostUnitOfWorkInterface) -> None:
        self.uow = uow

    def _create(self, post: CreatePostInputDto) -> Optional[Post]:
        _post = post_factory(
            uuid=str(post.uuid),
            author_id=post.author_id,
            title=post.title,
            body=post.body,
            created=post.created,
        )

        with self.uow:
            self.uow.post.add(_post)
            self.uow.commit()


    def _update(self, post: UpdatePostInputDto):
        with self.uow:
            self.uow.post.update_by_uuid(post.uuid, post.title, post.body)
            self.uow.commit()

    def _delete(self, post: DeletePostInputDto):
        with self.uow:
            self.uow.post.delete(post.uuid)
            self.uow.commit()

    def _get_all_blogs(self) -> Optional[list[model.Post]]:
        with self.uow:
            return self.uow.post.get_all()

    def _get_post_by_uuid(self, uuid: str, check_author: bool = True) -> Post:
        with self.uow:
            post = self.uow.post.get_by_uuid(uuid)
            if post is None:
                abort(404, f"Post uuid {uuid} doesn't exist.")

            if check_author and post["author_id"] != g.user["id"]:
                abort(403)
            return post

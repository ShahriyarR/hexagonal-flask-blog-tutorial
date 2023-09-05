from abc import ABC, abstractmethod
from typing import Any, Optional

from blog.domain.model.model import Post
from blog.domain.model.schemas import (
    CreatePostInputDto,
    DeletePostInputDto,
    UpdatePostInputDto,
)
from blog.domain.ports.unit_of_works.post import PostUnitOfWorkInterface


class PostServiceInterface(ABC):
    @abstractmethod
    def __init__(self, uow: PostUnitOfWorkInterface) -> None:
        raise NotImplementedError

    def create(self, post: CreatePostInputDto) -> Optional[Post]:  # pragma: no cover
        return self._create(post)

    def update(self, post: UpdatePostInputDto):  # pragma: no cover
        return self._update(post)

    def delete(self, post: DeletePostInputDto):  # pragma: no cover
        return self._delete(post)

    def get_all_blogs(self) -> Optional[list[Any]]:  # pragma: no cover
        return self._get_all_blogs()

    def get_post_by_uuid(
        self, uuid: str, check_author: bool = True
    ) -> Post:  # pragma: no cover
        return self._get_post_by_uuid(uuid, check_author)

    @abstractmethod
    def _create(self, post: CreatePostInputDto) -> Optional[Post]:
        raise NotImplementedError

    @abstractmethod
    def _update(self, post: UpdatePostInputDto):
        raise NotImplementedError

    @abstractmethod
    def _delete(self, post: DeletePostInputDto):
        raise NotImplementedError

    @abstractmethod
    def _get_all_blogs(self) -> Optional[list[Any]]:
        raise NotImplementedError

    @abstractmethod
    def _get_post_by_uuid(self, uuid: str, check_author: bool = True) -> Post:
        raise NotImplementedError

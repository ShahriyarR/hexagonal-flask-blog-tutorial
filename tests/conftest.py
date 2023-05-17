from uuid import uuid4

import pytest

from blog.domain.model.model import post_factory, user_factory
from blog.domain.model.schemas import create_post_factory, register_user_factory
from tests.fake_repositories import FakePostRepository, FakeUserRepository
from tests.fake_uows import FakeUserUnitOfWork


@pytest.fixture(scope="module")
def get_fake_user_repository():
    return FakeUserRepository()


@pytest.fixture(scope="module")
def get_fake_post_repository():
    return FakePostRepository()


@pytest.fixture(scope="module")
def get_fake_user_uow():
    return FakeUserUnitOfWork()


@pytest.fixture(scope="module")
def get_user_model_object():
    user_schema = register_user_factory(user_name="Shako", password="12345")
    return user_factory(
        uuid=user_schema.uuid,
        user_name=user_schema.user_name,
        password=user_schema.password,
    )


@pytest.fixture(scope="module")
def get_post_model_object():
    post_schema = create_post_factory(
        title="awesome title", body="mysterious body", author_id=uuid4()
    )
    return post_factory(
        uuid=str(post_schema.uuid),
        created=post_schema.created,
        author_id=str(post_schema.author_id),
        title=post_schema.title,
        body=post_schema.body,
    )

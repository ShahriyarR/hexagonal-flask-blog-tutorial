import pytest

from blog.domain.model.model import user_factory
from blog.domain.model.schemas import register_user_factory
from tests.fake_repository import FakeUserRepository


@pytest.fixture(scope="module")
def get_fake_user_repository():
    return FakeUserRepository()


@pytest.fixture(scope="module")
def get_user_model_object():
    user_schema = register_user_factory(user_name="Shako", password="12345")
    return user_factory(
        uuid=user_schema.uuid,
        user_name=user_schema.user_name,
        password=user_schema.password,
    )

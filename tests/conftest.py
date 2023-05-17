import pytest

from tests.fake_repository import FakeUserRepository


@pytest.fixture(scope="module")
def get_fake_user_repository():
    return FakeUserRepository()
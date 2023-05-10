import datetime

import pytest
from pydantic import ValidationError

from blog.domain.model.model import User, post_factory, user_factory
from blog.domain.model.schemas import (
    create_post_dto_factory,
    delete_post_factory,
    update_post_factory,
)


def test_if_can_create_with_post_factory():
    post = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post.author_id == 1


def test_if_two_posts_are_equal():
    post_1 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    post_2 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post_1 == post_2


def test_if_two_posts_are_not_equal():
    post_1 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    post_2 = post_factory(
        1,
        "Architecture",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post_1 != post_2


def test_if_posts_are_created_using_create_dto():
    post_dto = create_post_dto_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
    )
    assert post_dto.author_id == 1
    post = post_factory(post_dto.author_id, post_dto.title, post_dto.body)
    assert post.id_
    assert post.created


def test_if_posts_are_created_using_create_dto_with_wrong_types():
    with pytest.raises(ValidationError):
        _ = create_post_dto_factory(
            1,
            [],
            "Introduce patterns for Pythonistas",
        )


def test_if_update_posts_dto_is_created():
    update_dto = update_post_factory(1, "Awesome title", "Fit body")
    assert update_dto.id == 1


def test_if_update_posts_dto_is_created_with_wrong_types():
    with pytest.raises(ValidationError):
        _ = update_post_factory(object, "Awesome title", "Fit body")


def test_if_delete_post_dto_is_created():
    delete_dto = delete_post_factory(id_=1)
    assert delete_dto.id == 1


def test_if_delete_post_dto_is_created_with_wrong_type():
    with pytest.raises(ValidationError):
        _ = delete_post_factory(id_="")


def test_if_can_create_user_with_user_factory():
    user = user_factory("Shako", "AzePUG")
    assert user.id_
    assert isinstance(user, User)

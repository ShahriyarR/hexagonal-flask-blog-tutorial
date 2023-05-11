from datetime import datetime

import pytest
from pydantic import ValidationError

from blog.domain.model.model import Post, User, post_factory, user_factory
from blog.domain.model.schemas import (
    RegisterUserInputDto,
    create_post_dto_factory,
    delete_post_factory,
    register_user_factory,
    update_post_factory,
)


#  Tests that a Post object can be created with valid parameters. Tags: [happy path]
def test_create_post_valid_parameters():
    post = Post(
        id_="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert isinstance(post, Post)


#  Tests that two Post objects with the same author_id and title are equal. Tags: [happy path]
def test_compare_same_author_id_and_title():
    post1 = Post(
        id_="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    post2 = Post(
        id_="2",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert post1 == post2


#  Tests that two Post objects with different author_id and title are not equal. Tags: [edge case]
def test_compare_different_author_id_and_title():
    post1 = Post(
        id_="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    post2 = Post(
        id_="2",
        author_id=456,
        title="Different Title",
        body="Different Body",
        created=datetime.now(),
    )
    assert post1 != post2


#  Tests that a Post object cannot be compared with a non-Post object. Tags: [edge case]
def test_compare_with_non_post_object():
    post = Post(
        id_="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert post != "not a post object"


#  Tests the string representation of a Post object. Tags: [general behavior]
def test_string_representation():
    post = Post(
        id_="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert str(post) == "Post('Test Title')"


#  Tests that a Post object cannot be hashed with a non-integer author_id. Tags: [edge case]
def test_hash_with_non_integer_author_id():
    with pytest.raises(TypeError):
        post = Post(
            id_="1",
            author_id="not an integer",
            title="Test Title",
            body="Test Body",
            created=datetime.now(),
        )
        hash(post)


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

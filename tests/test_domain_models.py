from datetime import datetime
from uuid import uuid4

import pytest

from blog.domain.model.model import Post, post_factory


#  Tests that a Post object can be created with valid parameters. Tags: [happy path]
def test_create_post_valid_parameters():
    post = Post(
        uuid="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert isinstance(post, Post)


#  Tests that two Post objects with the same author_id and title are equal. Tags: [happy path]
def test_compare_same_author_id_and_title():
    post1 = Post(
        uuid="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    post2 = Post(
        uuid="2",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert post1 == post2


#  Tests that two Post objects with different author_id and title are not equal. Tags: [edge case]
def test_compare_different_author_id_and_title():
    post1 = Post(
        uuid="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    post2 = Post(
        uuid="2",
        author_id=456,
        title="Different Title",
        body="Different Body",
        created=datetime.now(),
    )
    assert post1 != post2


#  Tests that a Post object cannot be compared with a non-Post object. Tags: [edge case]
def test_compare_with_non_post_object():
    post = Post(
        uuid="1",
        author_id=123,
        title="Test Title",
        body="Test Body",
        created=datetime.now(),
    )
    assert post != "not a post object"


#  Tests the string representation of a Post object. Tags: [general behavior]
def test_string_representation():
    post = Post(
        uuid="1",
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


#  Tests that the function returns a Post object with a unique id and created datetime when
#  valid input parameters are provided.
#  Tags: [happy path]
def test_valid_input_parameters():
    post = post_factory(uuid4(), 1, "Test Title", "Test Body", datetime.now())
    assert isinstance(post, Post)
    assert post.author_id == 1
    assert post.title == "Test Title"
    assert post.body == "Test Body"
    assert isinstance(post.created, datetime)
    assert post.uuid != ""


#  Tests that the function raises an error when an empty string is provided for the title parameter. Tags: [edge case]
def test_empty_string_title():
    with pytest.raises(ValueError):
        post_factory(uuid4(), 1, "", "Test Body", datetime.now())


#  Tests that the function raises an error when an empty string is provided for the body parameter. Tags: [edge case]
def test_empty_string_body():
    with pytest.raises(ValueError):
        post_factory(uuid4(), 1, "Test Title", "", datetime.now())


#  Tests that the function raises an error when a non-integer value is provided for the author_id parameter.
#  Tags: [edge case]
def test_non_integer_author_id():
    with pytest.raises(TypeError):
        post_factory(
            uuid4(), "not_an_integer", "Test Title", "Test Body", datetime.now()
        )


#  Tests that the function raises an error when an invalid datetime format is provided for the created parameter.
#  Tags: [edge case]
def test_invalid_datetime_format():
    with pytest.raises(TypeError):
        post_factory(uuid4(), 1, "Test Title", "Test Body", "invalid_datetime_format")

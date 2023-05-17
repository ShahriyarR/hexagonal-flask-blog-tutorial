from datetime import datetime
from uuid import uuid4

import pytest

from blog.domain.model.model import Post, User, post_factory, user_factory


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
    author_id = str(uuid4())
    post = post_factory(str(uuid4()), author_id, "Test Title", "Test Body", datetime.now())
    assert isinstance(post, Post)
    assert post.author_id == author_id
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
    with pytest.raises(ValueError):
        post_factory(
            uuid4(), "not_an_integer", "Test Title", "Test Body", datetime.now()
        )


#  Tests that the function raises an error when an invalid datetime format is provided for the created parameter.
#  Tags: [edge case]
def test_invalid_datetime_format():
    with pytest.raises(TypeError):
        post_factory(uuid4(), uuid4(), "Test Title", "Test Body", "invalid_datetime_format")


#  Tests that a User object can be created with valid uuid, user_name, and password. Tags: [happy path]
def test_creating_user_object_with_valid_data():
    user = User(uuid="1234", user_name="test_user", password="password")
    assert user.uuid == "1234"
    assert user.user_name == "test_user"
    assert user.password == "password"


#  Tests that two User objects with the same user_name are equal. Tags: [happy path]
def test_comparing_two_user_objects_with_same_user_name():
    user1 = User(uuid="1234", user_name="test_user", password="password")
    user2 = User(uuid="5678", user_name="test_user", password="password2")
    assert user1 == user2


#  Tests that a User object cannot be created with an empty uuid, user_name, or password. Tags: [edge case]
def test_creating_user_object_with_empty_data():
    with pytest.raises(ValueError):
        user_factory(uuid="", user_name="", password="")


#  Tests that a User object cannot be created with a uuid, user_name, or password that exceeds the maximum length. Tags: [edge case]
def test_creating_user_object_with_exceeding_data():
    with pytest.raises(ValueError):
        user_factory(
            uuid="12345678901234567890123456789012345678901234567890123456789012345",
            user_name="test_user",
            password="password",
        )


#  Tests that hashing a User object with an empty uuid raises an error. Tags: [edge case]
def test_hashing_user_object_with_empty_uuid():
    user = User(uuid="", user_name="test_user", password="password")
    with pytest.raises(TypeError):
        hash(user)


#  Tests that comparing a User object with a non-User object returns False. Tags: [edge case]
def test_comparing_user_object_with_non_user_object():
    user = User(uuid="1234", user_name="test_user", password="password")
    assert user != "not a user object"


#  Tests that the function returns a User instance with valid input values for uuid, user_name, and password. Tags: [happy path]
def test_invalid_uuid():
    # Arrange
    uuid = "1234-5678"
    user_name = "testuser"
    password = "pass"

    # Act
    with pytest.raises(ValueError):
        _ = user_factory(uuid, user_name, password)


#  Tests that the function raises a ValueError when uuid has length greater than 16. Tags: [edge case]
def test_long_uuid():
    # Arrange
    uuid = "12345678901234567"
    user_name = "testuser"
    password = "pass"

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)


#  Tests that the function raises a ValueError when user_name has length greater than 8. Tags: [edge case]
def test_long_user_name():
    # Arrange
    uuid = "1234-5678"
    user_name = "testusername"
    password = "pass"

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)


#  Tests that the __str__ method of the User class returns the expected string representation. Tags: [general behavior]
def test_str_representation():
    # Arrange
    user = User(uuid="1234-5678", user_name="testuser", password="pass")

    # Act
    str_repr = str(user)

    # Assert
    assert str_repr == "User('testuser')"


#  Tests that the function raises a ValueError when password has length greater than 5. Tags: [edge case]
def test_long_password():
    # Arrange
    uuid = "1234-5678"
    user_name = "testuser"
    password = "password"

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)


#  Tests that the function raises a ValueError when uuid, user_name, or password is empty or None. Tags: [edge case]
def test_empty_values():
    # Arrange
    uuid = ""
    user_name = "testuser"
    password = "pass"

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)

    uuid = "1234-5678"
    user_name = ""
    password = "pass"

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)

    uuid = "1234-5678"
    user_name = "testuser"
    password = ""

    # Act & Assert
    with pytest.raises(ValueError):
        user_factory(uuid, user_name, password)

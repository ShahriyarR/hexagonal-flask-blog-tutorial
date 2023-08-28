import datetime
from uuid import uuid4

import pytest

from blog.domain.model.schemas import create_post_factory, CreatePostInputDto


#  Tests that valid input values are accepted and returned as expected. Tags: [happy path]
def test_valid_input_accepted():
    # Arrange
    input_data = {
        "uuid": uuid4(),
        "author_id": uuid4(),
        "title": "Test Title",
        "body": "Test Body",
        "created": datetime.datetime.now(),
    }
    expected_output = CreatePostInputDto(**input_data)

    # Act
    result = CreatePostInputDto(**input_data)

    # Assert
    assert result == expected_output


#  Tests that empty string values for title and body are accepted. Tags: [edge case]
def test_empty_strings_are_not_accepted():
    # Arrange
    input_data = {"author_id": uuid4(), "title": "", "body": ""}
    with pytest.raises(ValueError):
        _ = CreatePostInputDto(**input_data)


#  Tests that BaseModel validation errors are raised for invalid input values. Tags: [general behavior]
def test_invalid_input_raises_error():
    # Arrange
    input_data = {"author_id": "not an integer", "title": 123, "body": True}

    # Act & Assert
    with pytest.raises(ValueError):
        CreatePostInputDto(**input_data)


#  Tests that Unicode characters for title and body are accepted. Tags: [edge case]
def test_unicode_characters_accepted():
    # Arrange
    input_data = {
        "uuid": uuid4(),
        "author_id": uuid4(),
        "title": "Test Title with Unicode: こんにちは",
        "body": "Test Body with Unicode: 你好",
        "created": datetime.datetime.now(),
    }
    expected_output = CreatePostInputDto(**input_data)

    # Act
    result = CreatePostInputDto(**input_data)

    # Assert
    assert result == expected_output


#  Tests that BaseModel can be subclassed to add custom validators. Tags: [general behavior]
def test_custom_validator():
    # Arrange
    input_data = {"author_id": -1, "title": "Test Title", "body": "Test Body"}

    # Act & Assert
    with pytest.raises(ValueError):
        CreatePostInputDto(**input_data)


#  Tests that providing valid title, body, and author_id should return a CreatePostInputDto object. Tags: [happy path]
def test_create_post_factory_valid_input():
    # Arrange
    title = "Test Title"
    body = "Test Body"
    author_id = uuid4()

    # Act
    result = create_post_factory(title, body, author_id)

    # Assert
    assert isinstance(result, CreatePostInputDto)
    assert result.title == title
    assert result.body == body
    assert result.author_id == author_id


#  Tests that providing an empty string for title should raise a validation error. Tags: [edge case]
def test_create_post_factory_empty_title():
    # Arrange
    title = ""
    body = "Test Body"
    author_id = 1

    # Act & Assert
    with pytest.raises(ValueError):
        create_post_factory(title, body, author_id)


#  Tests that providing an empty string for body should raise a validation error. Tags: [edge case]
def test_create_post_factory_empty_body():
    # Arrange
    title = "Test Title"
    body = ""
    author_id = 1

    # Act & Assert
    with pytest.raises(ValueError):
        create_post_factory(title, body, author_id)


#  Tests that providing a title that exceeds the maximum length should raise a validation error. Tags: [general behavior]
def test_create_post_factory_max_length_title():
    # Arrange
    title = "a" * 201
    body = "Test Body"
    author_id = 1

    # Act & Assert
    with pytest.raises(ValueError):
        create_post_factory(title, body, author_id)


#  Tests that providing a negative value for author_id should raise a validation error. Tags: [edge case]
def test_create_post_factory_negative_author_id():
    # Arrange
    title = "Test Title"
    body = "Test Body"
    author_id = -1

    # Act & Assert
    with pytest.raises(ValueError):
        create_post_factory(title, body, author_id)


#  Tests that providing a body that exceeds the maximum length should raise a validation error. Tags: [general behavior]
def test_create_post_factory_max_length_body():
    # Arrange
    title = "Test Title"
    body = "a" * 10001
    author_id = 1

    # Act & Assert
    with pytest.raises(ValueError):
        create_post_factory(title, body, author_id)

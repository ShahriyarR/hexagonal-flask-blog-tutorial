from dataclasses import dataclass
from datetime import datetime

from blog.domain.model.validators import valid_uuid


@dataclass
class Post:
    uuid: str
    author_id: str
    title: str
    body: str
    created: datetime

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return self.author_id == other.author_id and self.title == other.title

    def __hash__(self):
        return hash(self.author_id)

    def __str__(self):
        return f"Post('{self.title}')"


def post_factory(
    uuid: str, author_id: str, title: str, body: str, created: datetime
) -> Post:
    # data validation should happen here
    if not valid_uuid(author_id):
        raise ValueError("Failed to verify if the string is valid UUID4")
    if not isinstance(created, datetime):
        raise TypeError("created should be a datetime type")
    if not body:
        raise ValueError("we do not accept empty body")
    if not title:
        raise ValueError("we do not accept empty title")

    return Post(uuid=uuid, author_id=author_id, title=title, body=body, created=created)


@dataclass
class User:
    uuid: str
    user_name: str
    password: str

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.user_name == other.user_name

    def __hash__(self):
        if isinstance(self.uuid, str) and self.uuid:
            return hash(self.uuid)
        else:
            raise TypeError("uuid must not be empty or other type than str")

    def __str__(self):
        return f"User('{self.user_name}')"


def user_factory(uuid: str, user_name: str, password: str) -> User:
    # data validation should happen here
    if not valid_uuid(uuid):
        raise ValueError("Failed to verify if the string is valid UUID4")
    if len(user_name) > 8:
        raise ValueError("User name should be maximum of 8 characters length")

    if not uuid or not user_name or not password:
        raise ValueError(
            "Mandatory fields of uuid, user_name and password can not be empty or None"
        )

    return User(uuid=uuid, user_name=user_name, password=password)

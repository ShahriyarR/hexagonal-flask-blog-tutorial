from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Post:
    id_: str
    author_id: int
    title: str
    body: str
    created: datetime

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return self.author_id == other.author_id and self.title == other.title

    def __hash__(self):
        if not isinstance(self.author_id, int):
            raise TypeError("author id should be integer")
        return hash(self.author_id)

    def __str__(self):
        return f"Post('{self.title}')"


def post_factory(
    uuid: UUID, author_id: int, title: str, body: str, created: datetime
) -> Post:
    # data validation should happen here
    if not isinstance(created, datetime):
        raise TypeError("created should be a datetime type")
    if not isinstance(author_id, int):
        raise TypeError("author id should be integer")
    if not body:
        raise ValueError("we do not accept empty body")
    if not title:
        raise ValueError("we do not accept empty title")
    if not isinstance(uuid, UUID):
        raise ValueError("failed to generate uuid")

    return Post(
        id_=str(uuid), author_id=author_id, title=title, body=body, created=created
    )


@dataclass
class User:
    id_: str
    user_name: str
    password: str


def user_factory(user_name: str, password: str) -> User:
    # data validation should happen here
    return User(id_=str(uuid4()), user_name=user_name, password=password)

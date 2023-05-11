from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


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
    author_id: int, title: str, body: str, created: datetime = None
) -> Post:
    # data validation should happen here
    _created = created or datetime.now()
    return Post(
        id_=str(uuid4()), author_id=author_id, title=title, body=body, created=_created
    )


@dataclass
class User:
    id_: str
    user_name: str
    password: str


def user_factory(user_name: str, password: str) -> User:
    # data validation should happen here
    return User(id_=str(uuid4()), user_name=user_name, password=password)

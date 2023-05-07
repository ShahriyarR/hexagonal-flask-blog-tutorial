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


def post_factory(
    author_id: int, title: str, body: str, created: datetime = None
) -> Post:
    # data validation should happen here
    _created = created or datetime.now()
    return Post(
        id_=str(uuid4()), author_id=author_id, title=title, body=body, created=_created
    )

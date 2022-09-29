from uuid import UUID, uuid4
from dataclasses import dataclass, field


@dataclass
class User:
    id_: str
    user_name: str
    password: str


def user_factory(user_name: str, password: str) -> User:
    # data validation should happen here
    return User(id_=str(uuid4()), user_name=user_name, password=password)
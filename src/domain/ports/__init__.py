from dataclasses import dataclass, asdict
from werkzeug.security import generate_password_hash


@dataclass
class RegisterUserInputDto:
    user_name: str
    password: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def register_user_factory(user_name: str, password: str) -> RegisterUserInputDto:
    return RegisterUserInputDto(user_name=user_name, password=generate_password_hash(password))


@dataclass
class CreatePostInputDto:
    title: str
    body: str
    author_id: int

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def create_post_factory(title: str, body: str, author_id: int) -> CreatePostInputDto:
    return CreatePostInputDto(title=title, body=body, author_id=author_id)


@dataclass
class UpdatePostInputDto:
    id: int
    title: str
    body: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def update_post_factory(id: int, title: str, body: str) -> UpdatePostInputDto:
    return UpdatePostInputDto(id=id, title=title, body=body)


@dataclass
class DeletePostInputDto:
    id: int

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def delete_post_factory(id: int) -> DeletePostInputDto:
    return DeletePostInputDto(id=id)
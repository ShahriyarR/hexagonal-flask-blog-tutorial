from pydantic import BaseModel
from werkzeug.security import generate_password_hash


class RegisterUserInputDto(BaseModel):
    user_name: str
    password: str


def register_user_factory(user_name: str, password: str) -> RegisterUserInputDto:
    return RegisterUserInputDto(
        user_name=user_name, password=generate_password_hash(password)
    )


class CreatePostInputDto(BaseModel):
    title: str
    body: str
    author_id: int


def create_post_factory(title: str, body: str, author_id: int) -> CreatePostInputDto:
    return CreatePostInputDto(title=title, body=body, author_id=author_id)


class UpdatePostInputDto(BaseModel):
    id: int
    title: str
    body: str


def update_post_factory(id_: int, title: str, body: str) -> UpdatePostInputDto:
    return UpdatePostInputDto(id=id_, title=title, body=body)


class DeletePostInputDto(BaseModel):
    id: int


def delete_post_factory(id_: int) -> DeletePostInputDto:
    return DeletePostInputDto(id=id_)

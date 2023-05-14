from pydantic import BaseModel, PositiveInt
from pydantic.class_validators import validator
from werkzeug.security import generate_password_hash


class RegisterUserInputDto(BaseModel):
    user_name: str
    password: str


def register_user_factory(user_name: str, password: str) -> RegisterUserInputDto:
    return RegisterUserInputDto(
        user_name=user_name, password=generate_password_hash(password)
    )


class CreatePostInputDto(BaseModel):
    author_id: PositiveInt
    title: str
    body: str

    # Possible place for custom validators, or it can be delegated to factory

    @validator("body")
    def body_length(cls, v):
        if len(v) > 10000:
            raise ValueError("Body length should be maximum of 10000 characters")
        return v

    @validator("title")
    def title_length(cls, v):
        if len(v) > 100:
            raise ValueError("Title length should be maximum of 100 characters")
        return v

    @validator("title", "body")
    def title_and_body_should_not_be_empty(cls, v):
        if not v:
            raise ValueError("Title and body should not be empty or None")
        return v

    # @validator("body")
    # def body_should_not_be_empty(cls, v):
    #     if not v:
    #         raise ValueError("Body should not be empty or None")
    #     return v


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

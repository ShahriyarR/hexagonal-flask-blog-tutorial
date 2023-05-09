import datetime

from blog.domain.model.model import post_factory


def test_if_can_create_with_post_factory():
    post = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post.author_id == 1


def test_if_two_posts_are_equal():
    post_1 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    post_2 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post_1 == post_2


def test_if_two_posts_are_not_equal():
    post_1 = post_factory(
        1,
        "Awesome Architectures",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    post_2 = post_factory(
        1,
        "Architecture",
        "Introduce patterns for Pythonistas",
        created=datetime.datetime.now(),
    )
    assert post_1 != post_2

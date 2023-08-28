from copy import deepcopy

import pytest


@pytest.mark.integration
def test_add_post(get_fake_container, get_post_model_object, get_user_model_object):
    post_uow = get_fake_container.post_uow()
    user_uow = get_fake_container.user_uow()
    with user_uow:
        user_uow.user.add(get_user_model_object)
        user_uow.commit()
        users = user_uow.user.get_all()
        uuid_ = users[0]["uuid"]

    with post_uow:
        get_post_model_object.author_id = uuid_
        post_uow.post.add(get_post_model_object)
        post_uow.commit()
        all_ = post_uow.post.get_all()
        assert len(all_) == 1
        assert all_[0]["title"] == "awesome title"


@pytest.mark.integration
def test_get_post_by_uuid(get_fake_container, get_post_model_object):
    post_uow = get_fake_container.post_uow()
    with post_uow:
        # post_uow.post.add(get_post_model_object)
        all_ = post_uow.post.get_all()
        # get the dictionary values
        uuid = all_[0]["uuid"]
        result = post_uow.post.get_by_uuid(uuid)
        assert result["title"] == "awesome title"


@pytest.mark.integration
def test_get_all_posts(get_fake_container, get_post_model_object):
    post_uow = get_fake_container.post_uow()
    with post_uow:
        all_ = post_uow.post.get_all()
        values = list(all_)
        assert len(values) == 1


@pytest.mark.integration
def test_update_by_uuid(get_fake_container, get_post_model_object):
    post_uow = get_fake_container.post_uow()
    with post_uow:
        all_ = post_uow.post.get_all()
        old_post = all_[0]
        uuid_ = old_post["uuid"]
        post_uow.post.update_by_uuid(uuid_, "awesome_title", "new_body")
        post_uow.commit()
        new_post = post_uow.post.get_by_uuid(uuid_)
        assert old_post["uuid"] == new_post["uuid"]
        assert old_post["title"] != new_post["title"]


@pytest.mark.integration
def test_delete_by_uuid(get_fake_container, get_post_model_object):
    post_uow = get_fake_container.post_uow()
    with post_uow:
        all_ = post_uow.post.get_all()
        post = all_[0]
        post_uow.post.delete(post["uuid"])
        post_uow.commit()
        all_ = post_uow.post.get_all()
        assert not all_

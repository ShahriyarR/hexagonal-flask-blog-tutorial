from copy import deepcopy


def test_add_post(get_fake_post_uow, get_post_model_object):
    with get_fake_post_uow:
        get_fake_post_uow.post.add(get_post_model_object)
        all_ = get_fake_post_uow.post.get_all()
        # get the dictionary values
        values = list(all_.values())
        assert len(values) == 1
        assert values[0].title == "awesome title"


def test_get_post_by_uuid(get_fake_post_uow, get_post_model_object):
    with get_fake_post_uow:
        get_fake_post_uow.post.add(get_post_model_object)
        all_ = get_fake_post_uow.post.get_all()
        # get the dictionary values
        values = list(all_.values())
        uuid = values[0].uuid
        result = get_fake_post_uow.post.get_by_uuid(uuid)
        assert result.title == "awesome title"


def test_get_all_posts(get_fake_post_uow, get_post_model_object):
    with get_fake_post_uow:
        get_fake_post_uow.post.add(get_post_model_object)
        all_ = get_fake_post_uow.post.get_all()
        values = list(all_.values())
        assert len(values) == 1


def test_update_by_uuid(get_fake_post_uow, get_post_model_object):
    with get_fake_post_uow:
        get_fake_post_uow.post.add(get_post_model_object)
        all_ = get_fake_post_uow.post.get_all()
        values = list(all_.values())
        post = deepcopy(values[0])
        uuid_ = post.uuid
        new_post = get_fake_post_uow.post.update_by_uuid(
            uuid_, "awesome_title", "new_body"
        )
        assert post.uuid == new_post.uuid
        assert post.title != new_post.title


def test_delete_by_uuid(get_fake_post_uow, get_post_model_object):
    with get_fake_post_uow:
        get_fake_post_uow.post.add(get_post_model_object)
        all_ = get_fake_post_uow.post.get_all()
        values = list(all_.values())
        post = values[0]
        get_fake_post_uow.post.delete(post.uuid)
        all_ = get_fake_post_uow.post.get_all()
        values = list(all_.values())
        assert not values

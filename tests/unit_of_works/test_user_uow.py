def test_add_user(get_fake_user_uow, get_user_model_object):
    with get_fake_user_uow:
        get_fake_user_uow.user.add(get_user_model_object)
        all_ = get_fake_user_uow.user.get_all()
        # get the dictionary values
        values = list(all_.values())
        assert len(values) == 1
        assert values[0].user_name == "Shako"


def test_get_user_by_uuid(get_fake_user_uow, get_user_model_object):
    with get_fake_user_uow:
        get_fake_user_uow.user.add(get_user_model_object)
        all_ = get_fake_user_uow.user.get_all()
        # get the dictionary values
        values = list(all_.values())
        uuid = values[0].uuid
        result = get_fake_user_uow.user.get_by_uuid(uuid)
        assert result.user_name == "Shako"


def test_get_user_by_user_name(get_fake_user_uow, get_user_model_object):
    with get_fake_user_uow:
        get_fake_user_uow.user.add(get_user_model_object)
        result = get_fake_user_uow.user.get_user_by_user_name("Shako")
        assert result.user_name == "Shako"


def test_get_all_users(get_fake_user_uow, get_user_model_object):
    with get_fake_user_uow:
        get_fake_user_uow.user.add(get_user_model_object)
        all_ = get_fake_user_uow.user.get_all()
        values = list(all_.values())
        assert len(values) == 1

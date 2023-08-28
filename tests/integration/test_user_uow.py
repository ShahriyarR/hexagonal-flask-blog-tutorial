import pytest


@pytest.mark.integration
def test_add_user(get_fake_container, get_user_model_object):
    uow = get_fake_container.user_uow()
    with uow:
        uow.user.add(get_user_model_object)
        uow.commit()
        all_ = uow.user.get_all()
        # get the dictionary values
        assert len(all_) == 1
        assert all_[0]["username"] == "Shako"


@pytest.mark.integration
def test_get_user_by_uuid(get_fake_container, get_user_model_object):
    uow = get_fake_container.user_uow()
    with uow:
        all_ = uow.user.get_all()
        # get the dictionary values
        uuid = all_[0]["uuid"]
        result = uow.user.get_by_uuid(uuid)
        assert result["username"] == "Shako"


@pytest.mark.integration
def test_get_user_by_user_name(get_fake_container, get_user_model_object):
    uow = get_fake_container.user_uow()
    with uow:
        result = uow.user.get_user_by_user_name("Shako")
        assert result["username"] == "Shako"


@pytest.mark.integration
def test_get_all_users(get_fake_container, get_user_model_object):
    uow = get_fake_container.user_uow()
    with uow:
        all_ = uow.user.get_all()
        assert len(all_) == 1

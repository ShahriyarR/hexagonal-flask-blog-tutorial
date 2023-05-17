def test_add_calculation(get_fake_user_repository, get_user_model_object):
    get_fake_user_repository.add(get_user_model_object)
    all_ = get_fake_user_repository.get_all()
    # get the dictionary values
    values = list(all_.values())
    assert len(values) == 1
    assert values[0].user_name == "Shako"


def test_get_calculation_by_uuid(get_fake_user_repository):
    all_ = get_fake_user_repository.get_all()
    # get the dictionary values
    values = list(all_.values())
    uuid = values[0].uuid
    result = get_fake_user_repository.get_by_uuid(uuid)
    assert result.user_name == "Shako"


def test_get_calculation_by_action(get_fake_user_repository):
    result = get_fake_user_repository.get_user_by_user_name("Shako")
    assert result.user_name == "Shako"


def test_get_all_calculations(get_fake_user_repository):
    all_ = get_fake_user_repository.get_all()
    values = list(all_.values())
    assert len(values) == 1

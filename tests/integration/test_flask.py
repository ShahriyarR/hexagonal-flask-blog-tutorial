from flask import session


def test_register_user(get_fake_container, get_flask_client, get_flask_app):
    fake_user_service = get_fake_container.user_service()
    user_uow = get_fake_container.user_uow()
    with get_flask_app.container.user_service.override(fake_user_service):
        response = get_flask_client.post(
            "/auth/register",
            follow_redirects=True,
            data={
                "username": "Rauf",
                "password": "12345",
            },
        )
        assert len(response.history) == 1
        assert response.request.path == "/auth/login"
        with get_flask_client:
            response = get_flask_client.post(
                "/auth/login",
                follow_redirects=True,
                data={
                    "username": "Rauf",
                    "password": "12345",
                },
            )

            assert len(response.history) == 1
            assert response.request.path == "/"

            with user_uow:
                users = user_uow.user.get_all()
                assert users[0]["username"] == "Rauf"
                uuid = users[0]["uuid"]
            assert session["user_id"] == uuid


def test_create_blog_post(get_fake_container, get_flask_client, get_flask_app):
    fake_user_service = get_fake_container.user_service()
    fake_post_service = get_fake_container.post_service()
    post_uow = get_fake_container.post_uow()
    with get_flask_app.container.user_service.override(fake_user_service):
        with get_flask_app.container.post_service.override(fake_post_service):
            response = get_flask_client.post(
                "/create",
                follow_redirects=True,
                data={
                    "title": "test1",
                    "body": "test2",
                },
            )
            assert response.status_code == 200
            assert len(response.history) == 1
            assert response.request.path == "/"

            with post_uow:
                posts = post_uow.post.get_all()
                assert posts[0]["title"] == "test1"





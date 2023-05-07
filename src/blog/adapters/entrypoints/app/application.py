from flask import Flask

from src.blog.configurator.containers import Container
from src.blog.configurator.config import init_app
from .blueprints.blog import blueprint as blog_blueprint
from .blueprints.auth import blueprint as user_blueprint


def create_app() -> Flask:
    container = Container()
    app = Flask(__name__)
    app.secret_key = "Awesome Secret Key which is going to be hacked."
    app.container = container
    with app.app_context():
        init_app(app)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(user_blueprint)
    app.add_url_rule("/", endpoint="index")
    return app

import functools

from dependency_injector.wiring import Provide, inject
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash

from src.blog.adapters.services.user import UserDBOperationError, UserService
from src.blog.configurator.containers import Container
from src.blog.domain.ports import register_user_factory

blueprint = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@blueprint.before_app_request
@inject
def load_logged_in_user(
    user_service: UserService = Provide[Container.user_package.user_service],
):
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = user_service.get_user_by_id(user_id)


@blueprint.route("/register", methods=("GET", "POST"))
@inject
def register(user_service: UserService = Provide[Container.user_package.user_service]):
    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]
        error = None
        if not user_name:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        user_ = register_user_factory(user_name=user_name, password=password)
        if not error:
            try:
                user_service.create(user_)
            except UserDBOperationError as err:
                print(err)
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for("auth.login"))
        flash(error)

    return render_template("auth/register.html")


@blueprint.route("/login", methods=("GET", "POST"))
@inject
def login(user_service: UserService = Provide[Container.user_package.user_service]):
    if request.method == "POST":
        user_name = request.form["username"]
        password = request.form["password"]

        error = None
        user = user_service.get_user_by_user_name(user_name=user_name)
        if not user:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if not error:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@blueprint.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))

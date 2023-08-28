import functools

from dependency_injector.wiring import inject, Provide
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

from blog.adapters.services.user import UserService
from blog.domain.model.schemas import register_user_factory
from blog.domain.ports.repositories.exceptions import UserDBOperationError

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
    user_service: UserService = Provide["user_service"],
):
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = user_service.get_user_by_uuid(user_id)


@blueprint.route("/register", methods=("GET", "POST"))
@inject
def register(user_service: UserService = Provide["user_service"]):
    error = None
    if request.method == "POST":
        error, password, user_name = _check_user_name_password(error)
        user_ = register_user_factory(user_name=user_name, password=password)
        if not error:
            try:
                user_service.create(user_)
            except UserDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for("auth.login"))
        flash(error)

    return render_template("auth/register.html")


def _check_user_name_password(error):
    user_name = request.form["username"]
    password = request.form["password"]
    if not user_name:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    return error, password, user_name


@blueprint.route("/login", methods=("GET", "POST"))
@inject
def login(user_service: UserService = Provide["user_service"]):
    error = None
    if request.method == "POST":
        error, user = _validate_user_name_and_password(error, user_service)
        if not error:
            session.clear()
            session["user_id"] = user["uuid"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


def _validate_user_name_and_password(error, user_service):
    user_name = request.form["username"]
    password = request.form["password"]
    user = user_service.get_user_by_user_name(user_name=user_name)
    if not user:
        error = "Incorrect username."
    elif not check_password_hash(user["password"], password):
        error = "Incorrect password."
    return error, user


@blueprint.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))

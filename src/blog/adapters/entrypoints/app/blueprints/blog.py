from dependency_injector.wiring import Provide, inject
from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from blog.domain.ports.repositories.exceptions import BlogDBOperationError
from src.blog.adapters.entrypoints.app.blueprints.auth import login_required
from src.blog.adapters.services.post import PostService
from src.blog.domain.model.schemas import (
    create_post_factory,
    delete_post_factory,
    update_post_factory,
)

blueprint = Blueprint("post", __name__)


@blueprint.route("/")
@inject
def index(post_service: PostService = Provide["post_service"]):
    posts = post_service.get_all_blogs()
    return render_template("post/index.html", posts=posts)


@blueprint.route("/create", methods=("GET", "POST"))
@login_required
@inject
def create(post_service: PostService = Provide["post_service"]):
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        post = create_post_factory(author_id=g.user["uuid"], title=title, body=body)
        if not error:
            try:
                post_service.create(post)
            except BlogDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for("post.index"))
        flash(error)

    return render_template("post/create.html")


@blueprint.route("/update/<string:uuid>", methods=("GET", "POST"))
@login_required
@inject
def update(uuid, post_service: PostService = Provide["post_service"]):
    post = post_service.get_post_by_uuid(uuid)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        _post = update_post_factory(uuid=uuid, title=title, body=body)

        if not error:
            try:
                post_service.update(_post)
            except BlogDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for("post.index"))
        flash(error)

    return render_template("post/update.html", post=post)


@blueprint.route("/delete/<string:uuid>", methods=("POST",))
@login_required
@inject
def delete(uuid, post_service: PostService = Provide["post_service"]):
    post_service.get_post_by_uuid(uuid)
    _post = delete_post_factory(uuid=uuid)
    try:
        post_service.delete(_post)
    except BlogDBOperationError as err:
        error = f"Something went wrong with database operation {err}"
    else:
        return redirect(url_for("post.index"))
    flash(error)

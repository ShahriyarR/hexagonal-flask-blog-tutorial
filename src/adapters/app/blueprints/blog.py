from flask import Blueprint, render_template, request, flash, g, redirect, url_for
from dependency_injector.wiring import inject, Provide

from src.adapters.app.blueprints.auth import login_required
from src.domain.ports import create_post_factory, update_post_factory, delete_post_factory
from src.domain.ports.post_service import PostService, BlogDBOperationError
from src.main.containers import Container

blueprint = Blueprint('post', __name__)


@blueprint.route('/')
@inject
def index(post_service: PostService = Provide[Container.blog_package.post_service]):
    posts = post_service.get_all_blogs()
    return render_template('post/index.html', posts=posts)


@blueprint.route('/create', methods=('GET', 'POST'))
@login_required
@inject
def create(post_service: PostService = Provide[Container.blog_package.post_service]):
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        post = create_post_factory(author_id=g.user["id"], title=title, body=body)
        if not error:
            try:
                post_service.create(post)
            except BlogDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for('post.index'))
        flash(error)

    return render_template('post/create.html')


@blueprint.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
@inject
def update(id, post_service: PostService = Provide[Container.blog_package.post_service]):
    post = post_service.get_post_by_id(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        _post = update_post_factory(id=id, title=title, body=body)

        if not error:
            try:
                post_service.update(_post)
            except BlogDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for('post.index'))
        flash(error)

    return render_template('post/update.html', post=post)


@blueprint.route('/<int:id>/delete', methods=('POST',))
@login_required
@inject
def delete(id, post_service: PostService = Provide[Container.blog_package.post_service]):
    post_service.get_post_by_id(id)
    _post = delete_post_factory(id=id)
    try:
        post_service.delete(_post)
    except BlogDBOperationError as err:
        error = f"Something went wrong with database operation {err}"
    else:
        return redirect(url_for('post.index'))
    flash(error)

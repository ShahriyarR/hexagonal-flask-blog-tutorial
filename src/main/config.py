import sqlite3
import click
from flask import current_app
from typing import Callable


def get_db() -> Callable[[], sqlite3.Connection]:
    db = sqlite3.connect(
        "hexagonal",
        detect_types=sqlite3.PARSE_DECLTYPES,
        check_same_thread=False
    )

    db.row_factory = sqlite3.Row
    # Solution for -> TypeError: cannot pickle 'sqlite3.Connection' object
    return lambda: db


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db().executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def close_db(db: Callable[[], sqlite3.Connection], e=None):
    if db is not None:
        db().close()


def init_app(app):
    app.cli.add_command(init_db_command)

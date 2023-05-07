# Hexagonal Architecture with Flask and Dependency Injector

## This project is a complete rewritten version of official Flask tutorial using Hexagonal Architecture

[Flask Blog tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/)

[Flask Blog tutorial code base](https://github.com/pallets/flask/tree/main/examples/tutorial/flaskr)

### About project dependencies

The project has 2 main dependencies:

[Dependency Injector](https://github.com/ets-labs/python-dependency-injector)

[Flask](https://github.com/pallets/flask)

### About Hexagonal Architecture

You can read it from original author:

[The Pattern: Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture/)

## How to install for development?

Use virtualenv as:

* `python3 -m venv .venv`
* `source .venv/bin/activate`

We use flit for the installation:

Install flit:

* `pip install flit==3.7.1`

Install using make command:

`make install-dev`

* Init the database

`flask --app src.adapters.app.application init-db`

* Start development service:

`flask --app src.adapters.app.application --debug run`
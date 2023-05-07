PYTHON=./.venv/bin/python

PHONY = help install install-dev build test test-cov format lint type-check secure run


help:
	@echo "---------------HELP-----------------"
	@echo "To install the project type -> make install"
	@echo "To install the project for development type -> make install-dev"
	@echo "To build the application"
	@echo "To run application -> make run"
	@echo "To test the project type [exclude slow tests] -> make test"
	@echo "To test with coverage [all tests] -> make test-cov"
	@echo "To format code type -> make format"
	@echo "To check linter type -> make lint"
	@echo "To run type checker -> make type-check"
	@echo "To run all security related commands -> make secure"
	@echo "------------------------------------"

install:
	${PYTHON} -m flit install --env --deps=develop

install-dev:
	${PYTHON} -m flit install --env --deps=develop --symlink

build:
	${PYTHON} -m flit build --format wheel
	${PYTHON} -m pip install dist/*.whl
	${PYTHON} -c 'import blog; print(blog.__version__)'

test:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv -m "not slow and not integration" tests

test-cov:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv --cov-report html --cov=src tests

format:
	${PYTHON} -m isort src tests --force-single-line-imports
	${PYTHON} -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
	${PYTHON} -m black src tests --config pyproject.toml
	${PYTHON} -m isort src tests

lint:
	${PYTHON} -m flake8 --max-complexity 5 --max-cognitive-complexity=3 src
	${PYTHON} -m black src tests --check --diff --config pyproject.toml
	${PYTHON} -m isort src tests --check --diff

type-check:
	${PYTHON} -m pytype --config=pytype.cfg src

secure:
	${PYTHON} -m bandit -r src --config pyproject.toml

clean_app:
	rm -rf venv .out .pytest_cache .tox  dist build analysis
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

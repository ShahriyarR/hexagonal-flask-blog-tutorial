ifdef OS
	PYTHON ?= .venv/Scripts/python.exe
	TYPE_CHECK_COMMAND ?= echo Pytype package doesn't support Windows OS
else
	PYTHON ?= .venv/bin/python
	TYPE_CHECK_COMMAND ?= ${PYTHON} -m pytype --config=pytype.cfg src
endif

SETTINGS_FILENAME = pyproject.toml

PHONY = help install install-dev build format lint type-check secure test install-flit enable-pre-commit-hooks run

help:
	@echo "--------------- HELP ---------------"
	@echo "To install the project -> make install"
	@echo "To install the project using symlinks (for development) -> make install-dev"
	@echo "To build the wheel package -> make build"
	@echo "To test the project -> make test"
	@echo "To test with coverage [all tests] -> make test-cov"
	@echo "To format code -> make format"
	@echo "To check linter -> make lint"
	@echo "To run type checker -> make type-check"
	@echo "To run all security related commands -> make secure"
	@echo "------------------------------------"

install:
	${PYTHON} -m flit install --env --deps=production

install-dev:
	${PYTHON} -m flit install -s --env --deps=develop --symlink

install-flit:
	${PYTHON} -m pip install flit==3.8.0

enable-pre-commit-hooks:
	${PYTHON} -m pre_commit install

build:
	${PYTHON} -m flit build --format wheel
	${PYTHON} -m pip install dist/*.whl
	${PYTHON} -c 'import pyremoveme; print(pyremoveme.__version__)'

format:
	${PYTHON} -m isort src tests --force-single-line-imports --settings-file ${SETTINGS_FILENAME}
	${PYTHON} -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
	${PYTHON} -m black src tests --config ${SETTINGS_FILENAME}
	${PYTHON} -m isort src tests --settings-file ${SETTINGS_FILENAME}

lint:
	${PYTHON} -m flake8 --toml-config ${SETTINGS_FILENAME} --max-complexity 5 --max-cognitive-complexity=5 src
	${PYTHON} -m black src tests --check --diff --config ${SETTINGS_FILENAME}
	${PYTHON} -m isort src tests --check --diff --settings-file ${SETTINGS_FILENAME}

type-check:
	@$(TYPE_CHECK_COMMAND)

secure:
	${PYTHON} -m bandit -r src --config ${SETTINGS_FILENAME}
	${PYTHON} -m safety check
	pip-audit .

test:
	${PYTHON} -m pytest -svvv -m "not slow and not integration" tests

test-slow:
	${PYTHON} -m pytest -svvv -m "slow" tests

test-integration:
	${PYTHON} -m pytest -svvv -m "integration" tests

init-db:
	${PYTHON} -m flask --app src.blog.adapters.entrypoints.app.application init-db

run:
	${PYTHON} -m flask --app src.blog.adapters.entrypoints.app.application --debug run --host 0.0.0.0

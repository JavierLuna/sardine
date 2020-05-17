# Development
dependencies:
	poetry install

pre-commit-hooks:
	pre-commit install

development: dependencies pre-commit-hooks

# Static analysis

lint-code:
	poetry run flake8 sardine

lint: lint-code

type-check:
	poetry run mypy -p sardine

# Docs
docs:
	mkdocs serve

# Packaging

build: tests lint
	poetry build

publish: build
	poetry publish
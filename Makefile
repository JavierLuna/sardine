# Development
dependencies:
	poetry install


development: dependencies

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
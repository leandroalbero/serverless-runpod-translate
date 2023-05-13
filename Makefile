.PHONY: freeze
freeze:
	cd requirements/production; pip-compile --resolver=backtracking
	cd requirements/development; pip-compile --resolver=backtracking

.PHONY: lint-local
lint-local:
	isort src tests
	black src tests
	flake8 src tests
	mypy src tests

.PHONY: lint-ci
lint-ci:
	isort --check src tests
	black --check src tests
	flake8 src tests
	mypy src tests

.PHONY: test-local
test-local: export ENVIRONMENT=test
test-local:
	pytest -s tests
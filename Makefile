.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pipenv install --dev

.PHONY: test
test:  ## Locally run unit tests
	@PIPENV_VERBOSITY=-1 pipenv run pytest

.PHONY: test-watch
test-watch:  ## Locally run unit tests in watch mode
	@PIPENV_VERBOSITY=-1 pipenv run ptw

.PHONY: lint
lint:  ## Lint and fix code
	@PIPENV_VERBOSITY=-1
	@pipenv run black --target-version=py312 .
	@pipenv run pylint --recursive=y .
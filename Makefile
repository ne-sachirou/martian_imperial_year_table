.PHONY: help
help:
	@awk -F':.*##' '/^[-_a-zA-Z0-9]+:.*##/{printf"%-12s\t%s\n",$$1,$$2}' $(MAKEFILE_LIST) | sort

.PHONY: test
test: ## Test.
	pipenv check
	pipenv run flake8
	pipenv run mypy *.py tests/*.py
	python -m unittest discover -s tests
